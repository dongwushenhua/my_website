# from __future__ import unicode_literals  # 版本兼容
from datetime import datetime
from django.contrib.auth.models import User
from django.db import models


class userProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user', default='')
    icon = models.ImageField(upload_to='uploads/%Y/%m/%d/', verbose_name='头像', default='static/default.jpg')
    sex = models.CharField(max_length=2, verbose_name='性别', null=True)
    contact = models.CharField(max_length=50, verbose_name='联系方式', null=True)
    signature = models.CharField(max_length=100, verbose_name='个性签名', null=True)
    school = models.CharField(max_length=20, verbose_name='学校', null=True)
    networkTime = models.IntegerField(default=0)
    active = models.PositiveIntegerField(default=0, editable=False)
    followeds = models.PositiveIntegerField(default=0, editable=False)
    followings = models.PositiveIntegerField(default=0, editable=False)
    articles = models.PositiveIntegerField(default=0, editable=False)
    comments = models.PositiveIntegerField(default=0, editable=False)
    likes = models.PositiveIntegerField(default=0, editable=False)
    collects = models.PositiveIntegerField(default=0, editable=False)
    directMessages = models.PositiveIntegerField(default=0, editable=False)
    messages = models.PositiveIntegerField(default=0, editable=False)
    views = models.PositiveIntegerField(default=0, editable=False)

    def increase_followeds(self):
        self.followeds += 1
        self.save(update_fields=['followeds'])

    def decrease_followeds(self):
        self.followeds -= 1
        self.save(update_fields=['followeds'])

    def increase_followings(self):
        self.followings += 1
        self.save(update_fields=['followings'])

    def decrease_followings(self):
        self.followings -= 1
        self.save(update_fields=['followings'])

    def increase_articles(self):
        self.articles += 1
        self.save(update_fields=['articles'])

    def decrease_articles(self):
        self.articles -= 1
        self.save(update_fields=['articles'])

    def increase_comments(self):
        self.comments += 1
        self.save(update_fields=['comments'])

    def decrease_comments(self):
        self.comments -= 1
        self.save(update_fields=['comments'])

    def increase_likes(self):
        self.likes += 1
        self.save(update_fields=['likes'])

    def decrease_likes(self):
        self.likes -= 1
        self.save(update_fields=['likes'])

    def increase_collects(self):
        self.collects += 1
        self.save(update_fields=['collects'])

    def decrease_collects(self):
        self.collects -= 1
        self.save(update_fields=['collects'])

    def increase_messages(self):
        self.messages += 1
        self.save(update_fields=['messages'])

    def decrease_messages(self):
        self.messages -= 1
        self.save(update_fields=['messages'])

    def increase_directMessages(self):
        self.directMessages += 1
        self.save(update_fields=['directMessages'])

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    # def rollback_newFlag(self):
    #     self.newFlag = "1"
    #     self.save(update_fields=['newFlag'])

    # def __str__(self):
    #     return self.user

    class Meta:
        db_table = 'userProfile'


#
#
# class newUser(models.Model):
#     userName = models.CharField(max_length=64, null=False, verbose_name='用户名', error_messages={'yonghuming': '长度必须为'})
#     passWord = models.CharField(max_length=100, verbose_name='密码', null=False)
#     createTime = models.DateTimeField(verbose_name='创建时间', default=datetime.now)
#     icon = models.ImageField(upload_to='uploads/%Y/%m/%d/', verbose_name='头像', default='static/default.jpg')
#     sex = models.CharField(max_length=2, verbose_name='性别', null=True)
#     contact = models.CharField(max_length=11, verbose_name='联系方式', null=True)
#     signature = models.CharField(max_length=11, verbose_name='个性签名', null=True)
#     school = models.CharField(max_length=11, verbose_name='学校', null=True)
#     recentLogTime = models.CharField(max_length=50, default="")
#     followedNumber = models.IntegerField(default=0)
#     followingNumber = models.IntegerField(default=0)
#     articleNumber = models.IntegerField(default=0)
#     commentNumber = models.IntegerField(default=0)
#     likesNumber = models.IntegerField(default=0)
#     collectNumber = models.IntegerField(default=0)
#     directMessageNumber = models.IntegerField(default=0)
#     messageNumber = models.IntegerField(default=0)
#     viewsNumber = models.IntegerField(default=0)
#     networkTime = models.IntegerField(default=0)
#     active = models.IntegerField(default=0)
#
#
# # collectArticle = models.ManyToManyField(to=article, related_name='collectArticle')
# def recentLogIn(self):
#     self.recentLogTime = timezone.now().strftime("%Y-%m-%d %H:%M:%S")
#     self.save(update_fields=['recentLogTime'])
#
#
# def __str__(self):
#     return self.id
#
#
# class Meta:
#     db_table = 'user'
#     verbose_name = '用户'  # 给后台看的
#     verbose_name_plural = verbose_name  # 后台用来加载的
#
#
# class userMessage(models.Model):
#     messageSender = models.ForeignKey(to=newUser, on_delete=models.DO_NOTHING, null=True, related_name="messageSender")
#     messageObject = models.CharField(max_length=5, verbose_name='消息对象', null=False, default="")
#     # 用户1文章2评论3关注者4
#     messageType = models.CharField(max_length=5, verbose_name='消息类型', null=False, default="")
#     # 点赞1评论2收藏3关注4留言5浏览6私信7
#     messageContent = models.CharField(max_length=500, null=False, default="")
#     # messageId = models.CharField(max_length=20, null=False, default='-1')
#     messageCreateTime = models.DateTimeField(verbose_name='创建时间', default=datetime.now)
#     messageReciever = models.ForeignKey(to=newUser, on_delete=models.DO_NOTHING, null=True,
#                                         related_name="messageReciever")
#
#     def __str__(self):
#         return self.messageType
#
#     class Meta:
#         db_table = 'userMessage'
#
#
class follow(models.Model):
    followTime = models.DateTimeField(default=datetime.now)
    followed = models.ForeignKey(to=userProfile, on_delete=models.DO_NOTHING, null=True, related_name="followed")
    following = models.ForeignKey(to=userProfile, on_delete=models.DO_NOTHING, null=True, related_name="following")
    message = models.CharField(max_length=2, default="22")

    def __str__(self):
        return self.message

    class Meta:
        db_table = 'follow'


class messageContent(models.Model):
    message = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.message

    class Meta:
        db_table = 'messageContent'
#
#
# class visitorMessage(models.Model):
#     time = models.DateTimeField(default=datetime.now)
#     message = models.CharField(max_length=100, null=True)
#     to = models.CharField(max_length=64, null=False)
#     visitor = models.ForeignKey(to=newUser, on_delete=models.DO_NOTHING, null=True)
#
#     def __str__(self):
#         return self.message
#
#     class Meta:
#         db_table = 'visitorMessage'
#
#
# class directMessages(models.Model):
#     time = models.DateTimeField(default=datetime.now)
#     message = models.CharField(max_length=100, null=True)
#     to = models.CharField(max_length=64, null=False)
#     visitor = models.ForeignKey(to=newUser, on_delete=models.DO_NOTHING, null=True)
#
#     def __str__(self):
#         return self.message
#
#     class Meta:
#         db_table = 'directMessages'
