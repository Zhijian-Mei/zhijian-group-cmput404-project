# Generated by Django 4.0.2 on 2022-03-03 06:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('socialdistribution', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LikeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('at_context', models.CharField(max_length=200)),
                ('object', models.CharField(max_length=200)),
                ('summary', models.CharField(max_length=200)),
                ('actor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='actor', to='socialdistribution.authormodel')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to='socialdistribution.authormodel')),
            ],
        ),
        migrations.DeleteModel(
            name='LikedModel',
        ),
    ]
