# Generated by Django 3.1.3 on 2020-11-20 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accouts', '0006_auto_20201120_0934'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='tag',
        ),
        migrations.AddField(
            model_name='product',
            name='tag',
            field=models.ManyToManyField(to='accouts.Tag'),
        ),
    ]
