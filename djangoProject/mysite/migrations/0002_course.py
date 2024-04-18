# Generated by Django 5.0.2 on 2024-03-02 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('description', models.CharField(max_length=2000)),
                ('thumbnail_url', models.CharField(max_length=1000)),
                ('video_url', models.CharField(max_length=1000)),
                ('type', models.CharField(choices=[('free', 'free'), ('paid', 'paid')], default='free', max_length=20)),
                ('course_length', models.CharField(max_length=100)),
            ],
        ),
    ]