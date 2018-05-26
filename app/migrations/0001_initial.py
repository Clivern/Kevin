# Generated by Django 2.0.4 on 2018-05-26 14:29

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
            name='Endpoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('route', models.CharField(max_length=100, verbose_name='Route')),
                ('method', models.CharField(choices=[('get', 'GET'), ('post', 'POST'), ('head', 'HEAD'), ('put', 'PUT'), ('delete', 'DELETE'), ('patch', 'PATCH'), ('trace', 'TRACE'), ('options', 'OPTIONS'), ('connect', 'CONNECT'), ('any', 'ANY')], default='any', max_length=20, verbose_name='Method')),
                ('target', models.CharField(choices=[('validate', 'VALIDATE'), ('debug', 'DEBUG'), ('dynamic', 'DYNAMIC')], default='debug', max_length=20, verbose_name='Target')),
                ('route_rules', models.TextField(verbose_name='Route rules')),
                ('headers_rules', models.TextField(verbose_name='Headers rules')),
                ('body_rules', models.TextField(verbose_name='Body rules')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
            ],
        ),
        migrations.CreateModel(
            name='Endpoint_Meta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(db_index=True, max_length=30, verbose_name='Meta key')),
                ('value', models.CharField(max_length=200, verbose_name='Meta value')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('endpoint', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Endpoint', verbose_name='Related endpoint')),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Name')),
                ('status', models.CharField(choices=[('pending', 'PENDING'), ('failed', 'FAILED'), ('passed', 'PASSED'), ('daemon', 'DAEMON'), ('error', 'ERROR')], default='pending', max_length=20, verbose_name='Status')),
                ('last_status', models.CharField(choices=[('pending', 'PENDING'), ('failed', 'FAILED'), ('passed', 'PASSED'), ('daemon', 'DAEMON'), ('error', 'ERROR')], default='pending', max_length=20, verbose_name='Last Status')),
                ('locked', models.BooleanField(default=False, verbose_name='Locked')),
                ('executor', models.CharField(max_length=200, verbose_name='Executor')),
                ('parameters', models.TextField(max_length=30, verbose_name='Parameters')),
                ('interval', models.CharField(max_length=200, verbose_name='Interval')),
                ('retry_count', models.PositiveSmallIntegerField(default=0, verbose_name='Retry Count')),
                ('trials', models.PositiveSmallIntegerField(default=5, verbose_name='Trials')),
                ('priority', models.PositiveSmallIntegerField(verbose_name='Priority')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('run_at', models.DateTimeField(null=True, verbose_name='Run at')),
                ('last_run', models.DateTimeField(null=True, verbose_name='Last Run')),
            ],
        ),
        migrations.CreateModel(
            name='Namespace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('slug', models.SlugField(max_length=60, unique=True, verbose_name='Slug')),
                ('is_public', models.BooleanField(default=False, verbose_name='Is Public')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Related user')),
            ],
        ),
        migrations.CreateModel(
            name='Namespace_Meta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(db_index=True, max_length=30, verbose_name='Meta key')),
                ('value', models.CharField(max_length=200, verbose_name='Meta value')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('namespace', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Namespace', verbose_name='Related namespace')),
            ],
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(db_index=True, max_length=30, verbose_name='Key')),
                ('value', models.CharField(max_length=200, verbose_name='Value')),
                ('autoload', models.BooleanField(default=False, verbose_name='Autoload')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=100, verbose_name='Job Title')),
                ('company', models.CharField(max_length=100, verbose_name='Company')),
                ('address', models.CharField(max_length=100, verbose_name='Address')),
                ('github_url', models.CharField(max_length=100, verbose_name='Github URL')),
                ('facebook_url', models.CharField(max_length=100, verbose_name='Facebook URL')),
                ('twitter_url', models.CharField(max_length=100, verbose_name='Twitter URL')),
                ('access_token', models.CharField(max_length=200, verbose_name='Access token')),
                ('refresh_token', models.CharField(max_length=200, verbose_name='Refresh token')),
                ('access_token_updated_at', models.DateTimeField(null=True, verbose_name='Access token last update')),
                ('refresh_token_updated_at', models.DateTimeField(null=True, verbose_name='Refresh token last update')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Related user')),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('method', models.CharField(choices=[('get', 'GET'), ('post', 'POST'), ('head', 'HEAD'), ('put', 'PUT'), ('delete', 'DELETE'), ('patch', 'PATCH'), ('trace', 'TRACE'), ('options', 'OPTIONS'), ('connect', 'CONNECT')], default='get', max_length=20, verbose_name='Method')),
                ('uri', models.TextField(verbose_name='Uri')),
                ('headers', models.TextField(verbose_name='Headers')),
                ('body', models.TextField(verbose_name='Body')),
                ('status', models.CharField(choices=[('valid', 'VALID'), ('not_valid', 'NOT_VALID'), ('debug', 'DEBUG')], default='debug', max_length=20, verbose_name='Status')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('endpoint', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Endpoint', verbose_name='Related endpoint')),
            ],
        ),
        migrations.CreateModel(
            name='Request_Meta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(db_index=True, max_length=30, verbose_name='Meta key')),
                ('value', models.CharField(max_length=200, verbose_name='Meta value')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Request', verbose_name='Related request')),
            ],
        ),
        migrations.CreateModel(
            name='Reset_Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(db_index=True, max_length=100, verbose_name='Email')),
                ('token', models.CharField(db_index=True, max_length=200, verbose_name='Token')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('expire_at', models.DateTimeField(verbose_name='Expire at')),
                ('messages_count', models.PositiveSmallIntegerField(verbose_name='Messages Count')),
            ],
        ),
        migrations.CreateModel(
            name='User_Meta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(db_index=True, max_length=30, verbose_name='Meta key')),
                ('value', models.CharField(max_length=200, verbose_name='Meta value')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Related User')),
            ],
        ),
        migrations.AddField(
            model_name='endpoint',
            name='namespace',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Namespace', verbose_name='Related namespace'),
        ),
    ]
