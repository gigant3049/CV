# Generated by Django 5.0.1 on 2024-02-05 11:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/articles/')),
                ('content', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('bio', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/articles/')),
            ],
        ),
        migrations.CreateModel(
            name='SubArticle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.article')),
            ],
        ),
    ]
