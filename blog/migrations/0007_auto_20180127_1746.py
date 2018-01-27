# Generated by Django 2.0.1 on 2018-01-27 17:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20180127_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='publication date'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='publication date'),
        ),
    ]
