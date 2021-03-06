# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-13 04:31
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
            ],
            options={
                'verbose_name': 'Author',
                'db_table': 'author',
                'verbose_name_plural': 'Authors',
            },
        ),
        migrations.CreateModel(
            name='BComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commented_time', models.DateTimeField(auto_now_add=True)),
                ('ip_address', models.GenericIPAddressField()),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('isbn_number', models.CharField(max_length=15)),
                ('language', models.CharField(max_length=100)),
                ('programing_language', models.CharField(max_length=40)),
                ('file', models.FileField(upload_to='resources/books/')),
            ],
            options={
                'verbose_name': 'Books',
                'db_table': 'books',
                'verbose_name_plural': 'Books',
            },
        ),
        migrations.CreateModel(
            name='BooksCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_type', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Book Category',
                'verbose_name_plural': 'Book Categories',
            },
        ),
        migrations.CreateModel(
            name='Reader',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resources.Book')),
                ('reader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='VComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commented_time', models.DateTimeField(auto_now_add=True)),
                ('ip_address', models.GenericIPAddressField()),
                ('text', models.TextField()),
                ('commentor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_title', models.CharField(max_length=150)),
                ('_desc', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='VideosCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_type', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Video Category',
                'verbose_name_plural': 'Video Categories',
            },
        ),
        migrations.CreateModel(
            name='Viewer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='resources.Video')),
                ('viewer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='viewers', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='video',
            name='video_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='resources.VideosCategory'),
        ),
        migrations.AddField(
            model_name='vcomment',
            name='video',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='resources.Video'),
        ),
        migrations.AddField(
            model_name='bcomment',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='resources.Book'),
        ),
        migrations.AddField(
            model_name='bcomment',
            name='commentor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='author',
            name='book',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='authors', to='resources.Book'),
        ),
    ]
