from django.contrib.auth.models import User
from django.db.models import Q
from django.http import JsonResponse
from notifications.signals import notify

from article.models import article
from comment.models import comment, commentLike
from comment.serializers import commentSerializer
from users.models import userProfile
from rest_framework.views import APIView


class addComment(APIView):
    def get(self, request):
        nowArticle = article.objects.filter(pk=request.GET.get('articleId')).first()
        reciever = nowArticle.postMan
        sender = userProfile.objects.filter(user=User.objects.get(username=request.session.get('username'))).first()
        newComment = comment()
        newComment.commentContent = request.GET.get('commentContent')
        newComment.article = article.objects.filter(pk=request.GET.get('articleId')).first()
        newComment.user = sender
        newComment.article = nowArticle
        if request.GET.get('parentId'):
            parentComment = comment.objects.get(pk=request.GET.get('parentId'))
            # 若回复层级超过二级，则转换为二级
            newComment.parent_id = parentComment.get_root().id
            # 被回复人
            newComment.reply_to = parentComment.user
            notify.send(sender, recipient=parentComment.user.user, verb='评论了你的评论，在：', target=nowArticle)
        else:
            notify.send(sender, recipient=reciever.user, verb='评论了你的文章：', target=nowArticle)
        newComment.save()
        commentList = comment.objects.filter(article=nowArticle).all()
        nowCommentsSerializer = commentSerializer(commentList, many=True)
        data = {'code': 200, 'msg': '评论成功', 'nowCommentsSerializer': nowCommentsSerializer.data}
        return JsonResponse(data)


class deleteComment(APIView):
    def get(self, request):
        nowComment = comment.objects.get(pk=request.GET.get('commentId'))
        nowArticle = nowComment.article
        nowComment.delete()
        nowComments = comment.objects.filter(article=nowArticle).all()
        nowCommentsSerializer = commentSerializer(nowComments, many=True)
        data = {'code': 200, 'msg': '删除成功', 'nowCommentsSerializer': nowCommentsSerializer.data}
        return JsonResponse(data)


class likeComment(APIView):
    def get(self, request):
        nowComment = comment.objects.filter(pk=request.GET.get('likeCommentId')).first()
        reciever = nowComment.user
        sender = userProfile.objects.filter(user=User.objects.get(username=request.session.get('username'))).first()
        nowCommentLike = commentLike.objects.filter(Q(likeMan=sender) & Q(likeComment=nowComment)).first()
        if (nowCommentLike):
            nowCommentLike.delete()
            nowComment.decrease_commentLikes()
        else:
            favour = commentLike()
            favour.likeMan = sender
            favour.likeComment = nowComment
            favour.parentArticle = nowComment.article
            favour.save()
            nowComment.increase_commentLikes()
        nowComments = comment.objects.filter(article=nowComment.article).all()
        nowCommentsSerializer = commentSerializer(nowComments, many=True)
        notify.send(sender, recipient=reciever.user, verb='点赞了你的评论，在：', target=nowComment.article)
        data = {'code': 200, 'msg': '操作成功', 'nowCommentsSerializer': nowCommentsSerializer.data}
        return JsonResponse(data)
