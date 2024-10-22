# Generated by Django 3.1 on 2024-07-05 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('image', models.ImageField(blank=True, upload_to='photos/about_me')),
                ('birth', models.CharField(max_length=250)),
                ('age', models.IntegerField()),
                ('website', models.CharField(max_length=255)),
                ('degree', models.CharField(max_length=250)),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('city', models.CharField(max_length=255)),
                ('available', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('back_image', models.ImageField(blank=True, upload_to='photos/about_me')),
                ('name', models.CharField(max_length=250)),
                ('tag1', models.CharField(max_length=250)),
                ('tag2', models.CharField(max_length=250)),
                ('tag3', models.CharField(max_length=250)),
                ('facebook', models.CharField(max_length=255)),
                ('linkdin', models.CharField(max_length=255)),
                ('github', models.CharField(max_length=255)),
                ('instagram', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sk1', models.CharField(max_length=255)),
                ('sk2', models.CharField(max_length=255)),
                ('sk3', models.CharField(max_length=255)),
                ('sk4', models.CharField(max_length=255)),
                ('sk5', models.CharField(max_length=255)),
                ('sk6', models.CharField(max_length=255)),
                ('sk7', models.CharField(max_length=255)),
                ('sk8', models.CharField(max_length=255)),
                ('sk9', models.CharField(max_length=255)),
            ],
        ),
    ]
