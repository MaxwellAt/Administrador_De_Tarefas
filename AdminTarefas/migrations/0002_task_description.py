# Generated by Django 4.1.7 on 2023-04-14 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminTarefas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='description',
            field=models.TextField(default=None, max_length=200),
            preserve_default=False,
        ),
    ]