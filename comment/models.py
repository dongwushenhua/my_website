from datetime import datetime
from django.db import models
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class comment(MPTTModel):
    article = models.ForeignKey("article.article", on_delete=models.CASCADE, related_name='commentArticle')
    user = models.ForeignKey("users.userProfile", on_delete=models.CASCADE, related_name='commentUser')
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='commentParent')
    reply_to = models.ForeignKey("users.userProfile", null=True, blank=True, on_delete=models.CASCADE,
                                 related_name='replyTo')
    commentContent = models.TextField(null=False, default='')
    commentTime = models.DateTimeField(default=datetime.now)
    commentLikes = models.PositiveIntegerField(default=0, editable=False)

    def increase_commentLikes(self):
        self.commentLikes += 1
        self.save(update_fields=['commentLikes'])

    def decrease_commentLikes(self):
        self.commentLikes -= 1
        self.save(update_fields=['commentLikes'])

    class MPTTMeta:
        order_insertion_by = ['commentTime']
        db_table = 'comment'

    def __str__(self):
        return self.commentContent


class commentLike(models.Model):
    likeMan = models.ForeignKey("users.userProfile", on_delete=models.CASCADE, related_name='commentLikeUser',
                                default='')
    likeTime = models.DateTimeField(default=datetime.now)
    likeComment = models.ForeignKey("comment", on_delete=models.CASCADE, related_name='likeComment',
                                    default='')
    parentArticle = models.ForeignKey("article.article", on_delete=models.CASCADE, related_name='parentArticle',
                                      default='')

    def __str__(self):
        return self.likeMan

    class Meta:
        db_table = 'commentLike'
