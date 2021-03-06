# Generated by Django 4.0.4 on 2022-04-19 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Podcast',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('link', models.URLField()),
                ('added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('-added',),
            },
        ),
    ]
