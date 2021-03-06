# Generated by Django 2.2.24 on 2021-10-05 23:46

import datetime
from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('article', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='commentLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('likeMan', models.CharField(default='', max_length=20)),
                ('likeTime', models.DateTimeField(default=datetime.datetime.now)),
                ('likeCommentId', models.CharField(default='-1', max_length=20)),
            ],
            options={
                'db_table': 'commentLike',
            },
        ),
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parentArticleId', models.CharField(default='-1', max_length=20)),
                ('commentContent', models.TextField(default='')),
                ('commentTime', models.DateTimeField(default=datetime.datetime.now)),
                ('nowCommentLikeFlag', models.CharField(default='0', max_length=20)),
                ('nowCommentLikeNumber', models.IntegerField(default=0)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commentArticle', to='article.article')),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='commentParent', to='comment.comment')),
                ('reply_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replyTo', to='users.userProfile')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commentUser', to='users.userProfile')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
