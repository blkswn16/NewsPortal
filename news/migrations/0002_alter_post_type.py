# Generated by Django 4.1.7 on 2023-04-03 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='type',
            field=models.CharField(choices=[('AR', 'Статья'), ('NE', 'Новость')], default='NE', max_length=2),
        ),
    ]