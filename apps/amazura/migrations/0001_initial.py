# Generated by Django 2.0.7 on 2018-12-10 10:10

import apps.amazura.models
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='comum', max_length=50)),
                ('code', models.CharField(blank=True, max_length=250)),
                ('is_visible', models.BooleanField(default=False)),
                ('created', models.DateField(auto_now_add=True)),
                ('slug', models.SlugField(blank=True, default='Comum', max_length=250)),
            ],
            options={
                'verbose_name_plural': 'albuns',
                'ordering': ['-created'],
            },
            managers=[
                ('default', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=250)),
                ('image', models.ImageField(upload_to=apps.amazura.models.photo_path_album)),
                ('is_public', models.BooleanField(default=False)),
                ('valor', models.DecimalField(decimal_places=2, default=5.69, max_digits=3)),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='date added')),
                ('album', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='amazura.Album', verbose_name='album')),
            ],
            options={
                'verbose_name': 'photo',
                'verbose_name_plural': 'photos',
                'get_latest_by': 'date_added',
                'ordering': ['-date_added'],
            },
            managers=[
                ('default', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Terapeuta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('code', models.CharField(blank=True, max_length=250)),
                ('created', models.DateField(auto_now_add=True)),
                ('capa', models.ImageField(upload_to=apps.amazura.models.photo_path_terapeuta)),
                ('slug', models.SlugField(blank=True, default='', max_length=250)),
                ('telefone', models.CharField(blank=True, max_length=15)),
                ('peso', models.IntegerField(blank=True)),
                ('altura', models.DecimalField(blank=True, decimal_places=2, max_digits=3)),
                ('idade', models.IntegerField(blank=True)),
                ('is_working', models.BooleanField(default=False)),
                ('texto', models.TextField(default='')),
            ],
            options={
                'verbose_name': 'terapeuta',
                'verbose_name_plural': 'terapeutas',
                'ordering': ['created'],
            },
            managers=[
                ('default', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='album',
            name='terapeuta',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='albuns', to='amazura.Terapeuta', verbose_name='terapeuta'),
        ),
    ]
