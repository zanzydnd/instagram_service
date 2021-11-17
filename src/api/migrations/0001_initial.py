# Generated by Django 3.2.8 on 2021-11-17 08:54

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BloggerState',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
            options={
                'db_table': 'blogger_state',
            },
        ),
        migrations.CreateModel(
            name='ExtraData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('data', models.JSONField()),
                ('name', models.CharField(max_length=100)),
                ('comments', models.TextField()),
            ],
            options={
                'db_table': 'extra_data',
            },
        ),
        migrations.CreateModel(
            name='SocialNetworkType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
            options={
                'db_table': 'social_network_type',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('data', models.JSONField()),
                ('priority', models.IntegerField()),
                ('fields', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=50), size=None)),
            ],
            options={
                'db_table': 'task',
            },
        ),
        migrations.CreateModel(
            name='TaskStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
            options={
                'db_table': 'task_status',
            },
        ),
        migrations.CreateModel(
            name='TaskType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
            options={
                'db_table': 'task_type',
            },
        ),
        migrations.CreateModel(
            name='TaskResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('link', models.FileField(upload_to='')),
                ('comment', models.TextField(null=True)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.task')),
            ],
            options={
                'db_table': 'task_result',
            },
        ),
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.taskstatus'),
        ),
        migrations.AddField(
            model_name='task',
            name='task_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.tasktype'),
        ),
        migrations.CreateModel(
            name='SocialNetworkUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('social_id', models.CharField(max_length=100)),
                ('parsed_at', models.DateTimeField()),
                ('account_created_date', models.DateField(null=True)),
                ('birth_date', models.DateField(null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('social_login', models.CharField(max_length=100, null=True)),
                ('full_name', models.CharField(max_length=150, null=True)),
                ('additional_content', models.TextField(null=True)),
                ('phone', models.CharField(max_length=20, null=True)),
                ('subscribed_ids', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), null=True, size=None)),
                ('followers', models.BigIntegerField(null=True)),
                ('following', models.BigIntegerField(null=True)),
                ('contents', models.BigIntegerField(null=True)),
                ('social_network_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.socialnetworktype')),
                ('task', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.task')),
            ],
            options={
                'db_table': 'social_network_user',
            },
        ),
        migrations.CreateModel(
            name='SocialNetworkContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_id', models.CharField(max_length=100)),
                ('photo', models.TextField(null=True)),
                ('likes', models.IntegerField(null=True)),
                ('comments', models.IntegerField(null=True)),
                ('task', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.task')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.socialnetworkuser')),
            ],
            options={
                'db_table': 'social_network_content',
            },
        ),
        migrations.CreateModel(
            name='Blogger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('login', models.CharField(max_length=150, null=True)),
                ('social_id', models.CharField(max_length=100)),
                ('subscribers_count', models.BigIntegerField(null=True)),
                ('content_count', models.BigIntegerField(null=True)),
                ('following', models.BigIntegerField(null=True)),
                ('categories', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=50), null=True, size=None)),
                ('age', models.IntegerField(null=True)),
                ('another_socials', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), null=True, size=None)),
                ('another_links', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=250), null=True, size=None)),
                ('social_network_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.socialnetworktype')),
                ('state', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.bloggerstate')),
                ('task', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.task')),
            ],
            options={
                'db_table': 'blogger',
            },
        ),
    ]
