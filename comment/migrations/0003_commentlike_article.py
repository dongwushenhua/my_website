# Generated by Django 2.2.24 on 2021-10-20 00:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_auto_20211014_2338'),
        ('comment', '0002_auto_20211019_2335'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentlike',
            name='article',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='commentLikeArticle', to='article.article'),
        ),
    ]
