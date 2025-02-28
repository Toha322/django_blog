# Generated by Django 5.1.1 on 2024-11-02 14:57

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0008_postviewscount'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created_at'], 'verbose_name': 'Пост', 'verbose_name_plural': 'Посты'},
        ),
        migrations.CreateModel(
            name='Dislike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Dislikes', to='blog_app.post')),
                ('user', models.ManyToManyField(related_name='Dislikes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='blog_app.post')),
                ('user', models.ManyToManyField(related_name='likes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
