# Generated by Django 4.2.19 on 2025-03-08 06:23

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
            name='BannerModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('author', models.CharField(max_length=50)),
                ('body', models.TextField()),
                ('is_publish', models.BooleanField(default=False)),
                ('like', models.IntegerField(default=0)),
                ('create_at', models.DateField(auto_now_add=True)),
                ('category', models.CharField(blank=True, max_length=200)),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/')),
            ],
        ),
        migrations.CreateModel(
            name='ConatactList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('contact', models.CharField(max_length=325)),
                ('url', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('phone', models.CharField(max_length=50)),
                ('subject', models.CharField(max_length=200)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='PostModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('body', models.TextField()),
                ('is_publish', models.BooleanField(default=False)),
                ('like', models.IntegerField(default=0)),
                ('create_at', models.DateField(auto_now_add=True)),
                ('category', models.CharField(blank=True, max_length=200)),
                ('image', models.ImageField(null=True, upload_to='')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
