# Generated by Django 4.0.4 on 2022-04-30 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_challengename_day30'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='body',
        ),
        migrations.AddField(
            model_name='project',
            name='url',
            field=models.URLField(default='https://abdusamad.uz'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.FileField(upload_to=''),
        ),
    ]
