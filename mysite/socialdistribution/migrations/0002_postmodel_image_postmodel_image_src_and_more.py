# Generated by Django 4.0.2 on 2022-03-20 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialdistribution', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodel',
            name='image',
            field=models.ImageField(null=True, upload_to='', verbose_name='post_image'),
        ),
        migrations.AddField(
            model_name='postmodel',
            name='image_src',
            field=models.CharField(blank=True, max_length=2000),
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='content',
            field=models.CharField(blank=True, max_length=2000),
        ),
    ]