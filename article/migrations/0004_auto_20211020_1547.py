# Generated by Django 2.2.24 on 2021-10-20 15:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_auto_20211014_2338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlecollect',
            name='collectArticle',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='article.article'),
        ),
        migrations.AlterField(
            model_name='articlecollect',
            name='collectMan',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='users.userProfile'),
        ),
        migrations.AlterField(
            model_name='articlelike',
            name='likeArticle',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='article.article'),
        ),
        migrations.AlterField(
            model_name='articlelike',
            name='likeMan',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='users.userProfile'),
        ),
        migrations.AlterField(
            model_name='articleview',
            name='viewArticle',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='viewArticle', to='article.article'),
        ),
        migrations.AlterField(
            model_name='articleview',
            name='viewMan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.userProfile'),
        ),
    ]
