# Generated by Django 4.0.5 on 2022-06-19 16:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hood', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=144)),
                ('email', models.EmailField(max_length=144)),
                ('profile_pic', models.ImageField(default='media/images/default.jpeg', upload_to='images/')),
                ('neighbourhood', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='hood.neighbourhood')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
