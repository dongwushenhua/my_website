# from django.db import models
#
# # Create your models here.
# from users.models import newUser
#
#
# class Website_views(models.Model):
#     """
#     网站访问量统计表：字段ID、总访问量
#     """
#     nid = models.AutoField(primary_key=True)
#     views = models.IntegerField()
#
#
# class view_ip(models.Model):
#     """
#     最近访问用户IP：字段ID、用户IP
#     """
#     nid = models.AutoField(primary_key=True)
#     user_ip = models.CharField(max_length=15, null=False)
#     create_time = models.DateTimeField(auto_now_add=True)
#
#
# # class userLatestArticleNumber(models.Model):
# #     user = models.ForeignKey(to=newUser, on_delete=models.DO_NOTHING, null=True)
# #     L0 = models.IntegerField(default=0)
# #     L1 = models.IntegerField(default=0)
# #     L2 = models.IntegerField(default=0)
# #     L3 = models.IntegerField(default=0)
# #     L4 = models.IntegerField(default=0)
# #     L5 = models.IntegerField(default=0)
# #     L6 = models.IntegerField(default=0)
# #     def __str__(self):
# #         return self.L0
# #
# #     class Meta:
# #         db_table = 'userLatestArticleNumber'
