from django.contrib.auth.models import User
from django.core.paginator import Paginator
from article.models import article, articleLike, articleCollect
from django.http.response import JsonResponse
from django.db.models import Q
import json
from rest_framework.views import APIView
from article.serializers import articleSerializer, articleCollectSerializer
from comment.models import comment, commentLike
from comment.serializers import commentSerializer, commentLikeSerializer
from tags.models import tag
from users.models import userProfile, follow
from notifications.signals import notify

from users.serializers import userProfileSerializer


def addArticle(request):
    data = json.loads(request.body.decode('utf-8'))
    nowUser = userProfile.objects.get(user=User.objects.filter(username=request.session.get('username')).first())
    nowArticle = article()
    nowArticle.title = data['title']
    nowArticle.content = data['content']
    nowArticle.postMan = nowUser
    nowArticle.save()  # 要先save才能关联
    nowUser.increase_articles()
    if data['tagIdList']:
        for item in data['tagIdList']:
            nowTag = tag.objects.filter(pk=item).first()
            nowArticle.articleTags.add(nowTag)
    data = {'code': 200, 'msg': '发布成功'}
    return JsonResponse(data)


def deleteArticle(request):
    nowUser = userProfile.objects.filter(
        user=User.objects.get(username=request.session.get('username'))).first()
    nowArticle = article.objects.get(pk=request.GET.get('articleId'))
    nowArticle.delete()
    nowUser.decrease_articles()
    data = {'code': 200, 'msg': '删除成功'}
    return JsonResponse(data)


def modifyArticle(request):
    pass


def likeArticle(request):
    nowArticle = article.objects.filter(pk=request.GET.get('articleId')).first()
    sender = userProfile.objects.filter(user=User.objects.get(username=request.session.get('username'))).first()
    reciever = nowArticle.postMan
    nowArticleLike = articleLike.objects.filter(Q(likeMan=sender) & Q(likeArticle=nowArticle))
    if (nowArticleLike):
        nowArticleLike.delete()
        nowArticle.decrease_likes()
        reciever.decrease_likes()
        # nowArticleLikeMessage =reciever.user.notifications.get(Q(actor=sender) & Q(verb='点赞了你的文章：') & Q(action_object=nowArticle))
        # nowArticleLikeMessage = notifications.objects.filter(
        #     Q(actor=sender) & Q(recipient=reciever) & Q(verb='点赞了你的文章：') & Q(action_object=nowArticle)).first()
        # nowArticleLikeMessage.delete()
        data = {'code': 200, 'msg': '取消点赞', 'nowArticleLikeFlag': '0', 'nowArticleLikeNumber': nowArticle.likes}
    else:
        nowArticleLike = articleLike()
        nowArticleLike.likeMan = sender
        nowArticleLike.likeArticle = nowArticle
        nowArticleLike.save()
        nowArticle.increase_likes()
        reciever.increase_likes()
        notify.send(sender, recipient=reciever.user, verb='点赞了你的文章：', target=nowArticle)
        data = {'code': 200, 'msg': '点赞成功', 'nowArticleLikeFlag': '1', 'nowArticleLikeNumber': nowArticle.likes}
    return JsonResponse(data)


def collectArticle(request):
    nowArticle = article.objects.filter(pk=request.GET.get('articleId')).first()
    sender = userProfile.objects.filter(user=User.objects.get(username=request.session.get('username'))).first()
    reciever = nowArticle.postMan
    nowArticleCollect = articleCollect.objects.filter(Q(collectMan=sender) & Q(collectArticle=nowArticle))
    if (nowArticleCollect):
        nowArticleCollect.delete()
        nowArticle.decrease_collects()
        reciever.decrease_collects()
        # nowArticleCollectMessage = notifications.objects.filter(
        #     Q(actor=sender) & Q(recipient=reciever) & Q(verb='收藏了你的文章：') & Q(action_object=nowArticle)).first()
        # nowArticleCollectMessage.delete()
        data = {'code': 200, 'msg': '取消收藏', 'nowArticleCollectFlag': '0',
                'nowArticleCollectNumber': nowArticle.collects}
    else:
        nowArticleCollect = articleCollect()
        nowArticleCollect.collectMan = sender
        nowArticleCollect.collectArticle = nowArticle
        nowArticleCollect.save()
        nowArticle.increase_collects()
        reciever.increase_collects()
        notify.send(sender, recipient=reciever.user, verb='收藏了你的文章：', target=nowArticle)
        reciever.increase_articles()
        data = {'code': 200, 'msg': '收藏成功', 'nowArticleCollectFlag': '1',
                'nowArticleCollectNumber': nowArticle.collects}
    return JsonResponse(data)


class searchArticle(APIView):
    pass


class showPersonalArticle(APIView):
    def get(self, request):
        nowUser = userProfile.objects.filter(user=User.objects.get(username=request.session.get('username'))).first()
        personalArticles = article.objects.filter(Q(postMan=nowUser) & ~Q(title='欢迎新人')).all()
        personalArticlesSerializer = articleSerializer(personalArticles, many=True)
        data = {'code': 200, 'msg': '查询个人归档成功', 'personalArticlesSerializer': personalArticlesSerializer.data}
        return JsonResponse(data)


class showVisitorArticle(APIView):
    def get(self, request):
        nowUser = userProfile.objects.filter(user=User.objects.get(username=request.GET.get('userName'))).first()
        personalArticles = article.objects.filter(Q(postMan=nowUser) & ~Q(title='欢迎新人')).all()
        personalArticlesSerializer = articleSerializer(personalArticles, many=True)
        nowUserSerializer = userProfileSerializer(nowUser)
        data = {'code': 200, 'msg': '查询访客文章成功', 'visitorArticlesSerializer': personalArticlesSerializer.data,
                'nowUserSerializer': nowUserSerializer.data}
        return JsonResponse(data)


class showCollectArticle(APIView):
    def get(self, request):
        nowUser = userProfile.objects.filter(user=User.objects.get(username=request.session.get('username'))).first()
        personalCollections = articleCollect.objects.filter(collectMan=nowUser).all()
        personalCollectionsSerializer = articleCollectSerializer(personalCollections, many=True)
        data = {'code': 200, 'msg': '查询个人收藏成功', 'personalCollectionsSerializer': personalCollectionsSerializer.data}
        return JsonResponse(data)


class showAllArticle(APIView):
    def get(self, request):
        nowArticles = article.objects.all()
        p = Paginator(nowArticles, 5)
        data = {'code': 200, 'msg': '查询所有文章成功', "pageNum": p.num_pages,
                "articlesSerializer": articleSerializer(p.page(request.GET.get("page")).object_list, many=True).data}
        return JsonResponse(data)


class showHotArticle(APIView):
    def get(self, request):
        nowArticles = article.objects.exclude(title='欢迎新人').order_by("-views")[0:4]
        nowArticlesSerializer = articleSerializer(nowArticles, many=True)
        data = {'code': 200, 'msg': '查询热门文章成功', 'nowArticlesSerializer': nowArticlesSerializer.data}
        return JsonResponse(data)


class showSpecificArticle(APIView):
    def get(self, request):
        nowArticle = article.objects.filter(pk=request.GET.get('articleId')).first()
        sender = userProfile.objects.filter(
            user=User.objects.filter(username=request.session.get("username")).first()).first()
        reciever = nowArticle.postMan
        reciever.increase_views()
        nowArticle.increase_views()
        nowArticleSerializer = articleSerializer(nowArticle)
        # 点赞
        nowArticleLike = articleLike.objects.filter(Q(likeMan=sender) & Q(likeArticle=nowArticle)).first()
        if (nowArticleLike):
            likeFlag = '1'
        else:
            likeFlag = '0'
        # 收藏
        nowArticleCollect = articleCollect.objects.filter(Q(collectMan=sender) & Q(collectArticle=nowArticle))
        if (nowArticleCollect):
            collectFlag = '1'
        else:
            collectFlag = '0'
        # 评论
        nowComments = comment.objects.filter(article=nowArticle).all()
        nowCommentsSerializer = commentSerializer(nowComments, many=True)
        # 关注
        relationship = follow.objects.filter(Q(following=sender) & Q(followed=reciever))
        if (relationship):
            followFlag = "1"
        else:
            followFlag = "0"
        # notify.send(sender, recipient=reciever, verb='浏览了你的文章：', action_object=nowArticle, )
        data = {'code': 200, 'msg': '查询具体文章成功', 'nowArticleSerializer': nowArticleSerializer.data,
                'nowUser': request.session.get('username'), 'nowCommentsSerializer': nowCommentsSerializer.data,
                'likeFlag': likeFlag, 'collectFlag': collectFlag,
                'followFlag': followFlag}
        return JsonResponse(data)
