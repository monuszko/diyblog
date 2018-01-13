# Generated by Django 2.0.1 on 2018-01-12 14:22

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthorBio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
            ],
            options={
                'indexes': [],
                'proxy': True,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AlterModelOptions(
            name='blogpost',
            options={'ordering': ['-pub_date']},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['pub_date']},
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Author'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Author'),
        ),
        migrations.AddField(
            model_name='authorbio',
            name='author',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='blog.Author'),
        ),
    ]