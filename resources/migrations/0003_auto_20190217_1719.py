# Generated by Django 2.0.9 on 2019-02-17 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20190116_1249'),
        ('resources', '0002_auto_20190215_1410'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='author',
        ),
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.ManyToManyField(related_name='book', to='users.Profile'),
        ),
    ]
