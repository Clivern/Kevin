# Generated by Django 2.0.4 on 2018-04-15 17:47

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
                ('target', models.CharField(choices=[('validate', 'VALIDATE'), ('debug', 'DEBUG')], default='debug', max_length=20, verbose_name='Target')),
                ('route_rules', models.TextField(verbose_name='Route_Rules')),
                ('header_rules', models.TextField(verbose_name='Header_Rules')),
                ('body_rules', models.TextField(verbose_name='Body_Rules')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created_at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated_at')),
            ],
        ),
        migrations.CreateModel(
            name='Endpoint_Meta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(db_index=True, max_length=30, verbose_name='Key')),
                ('value', models.CharField(max_length=200, verbose_name='Value')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created_at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated_at')),
                ('endpoint', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Endpoint', verbose_name='Endpoint')),
            ],
        ),
        migrations.CreateModel(
            name='Namespace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('slug', models.SlugField(max_length=60, unique=True, verbose_name='Slug')),
                ('is_public', models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], default='no', max_length=5, verbose_name='Is_Public')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created_at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated_at')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(db_index=True, max_length=30, verbose_name='Key')),
                ('value', models.CharField(max_length=200, verbose_name='Value')),
                ('autoload', models.CharField(choices=[('on', 'On'), ('off', 'Off')], default='off', max_length=5, verbose_name='Autoload')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created_at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated_at')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('access_token', models.CharField(max_length=200, verbose_name='Access_Token')),
                ('refresh_token', models.CharField(max_length=200, verbose_name='Refresh_Token')),
                ('access_token_updated_at', models.DateTimeField(verbose_name='Access_Token_Updated_at')),
                ('refresh_token_updated_at', models.DateTimeField(verbose_name='Refresh_Token_Updated_at')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created_at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated_at')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Request_Meta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(db_index=True, max_length=30, verbose_name='Key')),
                ('value', models.CharField(max_length=200, verbose_name='Value')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created_at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated_at')),
                ('request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Request', verbose_name='Request')),
            ],
        ),
        migrations.AddField(
            model_name='endpoint',
            name='namespace',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Namespace', verbose_name='Namespace'),
        ),
    ]
