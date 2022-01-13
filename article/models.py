from django.db import models
from datetime import datetime


class articleLike(models.Model):
    likeMan = models.ForeignKey("users.userProfile", on_delete=models.CASCADE, default='')
    likeTime = models.DateTimeField(default=datetime.now)
    likeArticle = models.ForeignKey("article.article", on_delete=models.CASCADE, default='')

    def __str__(self):
        return self.likeMan

    class Meta:
        db_table = 'articleLike'


class articleCollect(models.Model):
    collectMan = models.ForeignKey("users.userProfile", on_delete=models.CASCADE, default='')
    collectTime = models.DateTimeField(default=datetime.now)
    collectArticle = models.ForeignKey("article.article", on_delete=models.CASCADE, default='')

    def __str__(self):
        return self.collectMan

    class Meta:
        db_table = 'articleCollect'


class articleView(models.Model):
    viewMan = models.ForeignKey("users.userProfile", on_delete=models.CASCADE)
    viewTime = models.DateTimeField(default=datetime.now)
    viewArticle = models.ForeignKey("article.article", on_delete=models.CASCADE, default='',
                                    related_name='viewArticle')

    def __str__(self):
        return self.viewMan

    class Meta:
        db_table = 'articleView'


class article(models.Model):
    title = models.CharField(max_length=500, null=True)
    content = models.TextField(null=True)
    # text = models.TextField(null=False, default='')
    createTime = models.DateTimeField(default=datetime.now)
    postMan = models.ForeignKey("users.userProfile", on_delete=models.CASCADE)
    views = models.PositiveIntegerField(default=0, editable=False)
    likes = models.PositiveIntegerField(default=0, editable=False)
    collects = models.PositiveIntegerField(default=0, editable=False)
    comments = models.PositiveIntegerField(default=0, editable=False)
    articleTags = models.ManyToManyField("tags.tag", related_name='articleTags')

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])

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

    def increase_comments(self):
        self.comments += 1
        self.save(update_fields=['comments'])

    def decrease_comments(self):
        self.comments -= 1
        self.save(update_fields=['comments'])

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'article'
        ordering = ['-createTime']
