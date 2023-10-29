# Generated by Django 4.2.5 on 2023-10-27 18:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='userProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('catName', models.CharField(max_length=100)),
                ('catAge', models.CharField(max_length=100)),
                ('catBreed', models.CharField(max_length=100)),
                ('profilePic', models.ImageField(blank=True, null=True, upload_to='profileImages/')),
                ('catImg', models.ImageField(blank=True, null=True, upload_to='catImages/')),
            ],
            options={
                'db_table': 'UserProfile',
            },
        ),
        migrations.CreateModel(
            name='vets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vName', models.CharField(max_length=100)),
                ('vAddress', models.CharField(max_length=300)),
                ('vPhone', models.CharField(max_length=15)),
                ('vLocation', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'vets',
            },
        ),
    ]