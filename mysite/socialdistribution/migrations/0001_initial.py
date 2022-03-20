# Generated by Django 3.0.6 on 2022-03-04 19:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthorModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('host', models.CharField(default='http://127.0.0.1:8000/', max_length=200)),
                ('displayName', models.CharField(max_length=200)),
                ('github', models.CharField(max_length=200)),
                ('profileImage', models.ImageField(null=True, upload_to='', verbose_name='profile_image')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='InboxModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='LoginInformationModel',
            fields=[
                ('username', models.CharField(max_length=30, verbose_name='username')),
                ('password', models.CharField(max_length=30, verbose_name='password')),
                ('id', models.CharField(max_length=300, primary_key=True, serialize=False, verbose_name='id')),
            ],
            options={
                'db_table': 'LoginInformation',
            },
        ),
        migrations.CreateModel(
            name='PostModel',
            fields=[
                ('title', models.CharField(max_length=200)),
                ('id', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('source', models.CharField(blank=True, max_length=200)),
                ('origin', models.CharField(blank=True, max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('contentType', models.CharField(max_length=200)),
                ('content', models.CharField(max_length=2000)),
                ('categories', models.CharField(max_length=200)),
                ('like_count', models.IntegerField(default=0)),
                ('comments', models.CharField(blank=True, max_length=200)),
                ('published', models.DateTimeField(auto_now=True)),
                ('visibility', models.CharField(max_length=200)),
                ('unlisted', models.BooleanField()),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='post', to='socialdistribution.AuthorModel')),
            ],
        ),
        migrations.CreateModel(
            name='LikeModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('at_context', models.CharField(max_length=200)),
                ('object', models.CharField(max_length=200)),
                ('summary', models.CharField(max_length=200)),
                ('actor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='actor', to='socialdistribution.AuthorModel')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to='socialdistribution.AuthorModel')),
            ],
        ),
        migrations.CreateModel(
            name='FollowRequestModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summary', models.CharField(max_length=200)),
                ('accept', models.BooleanField(default=False)),
                ('actor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follower', to='socialdistribution.AuthorModel')),
                ('object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followee', to='socialdistribution.AuthorModel')),
            ],
        ),
        migrations.CreateModel(
            name='FollowersModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items', models.ManyToManyField(to='socialdistribution.AuthorModel')),
            ],
        ),
        migrations.CreateModel(
            name='CommentModel',
            fields=[
                ('id', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('comment', models.CharField(max_length=2000)),
                ('contentType', models.CharField(max_length=200)),
                ('published', models.CharField(max_length=200)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_name', to='socialdistribution.AuthorModel')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments_set', to='socialdistribution.PostModel')),
            ],
        ),
    ]
