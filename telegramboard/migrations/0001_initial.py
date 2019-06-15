# Generated by Django 2.0.9 on 2019-06-15 21:16

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
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, max_length=255, null=True, upload_to='')),
                ('file', models.FileField(blank=True, null=True, upload_to='')),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('telegram_id', models.CharField(default=0, max_length=100)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
