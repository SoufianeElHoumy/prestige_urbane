# Generated by Django 5.0.6 on 2024-06-29 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_post_created_at_post_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='id',
        ),
        migrations.AddField(
            model_name='post',
            name='item_id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
    ]
