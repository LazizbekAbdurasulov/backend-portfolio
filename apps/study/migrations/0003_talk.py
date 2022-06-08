# Generated by Django 4.0.4 on 2022-04-19 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0002_podcast'),
    ]

    operations = [
        migrations.CreateModel(
            name='Talk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=500)),
                ('author', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='talk-images')),
                ('link', models.URLField()),
                ('added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('-added',),
            },
        ),
    ]