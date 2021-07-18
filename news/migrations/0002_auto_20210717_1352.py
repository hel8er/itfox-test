# Generated by Django 3.2.5 on 2021-07-17 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name_plural': 'news'},
        ),
        migrations.RemoveField(
            model_name='news',
            name='timestamp',
        ),
        migrations.AddField(
            model_name='news',
            name='pub_date',
            field=models.DateField(auto_now=True),
        ),
    ]
