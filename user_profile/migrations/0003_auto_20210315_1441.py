# Generated by Django 3.1.5 on 2021-03-15 09:11

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0002_diet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diet',
            name='nutrients',
            field=jsonfield.fields.JSONField(default=''),
        ),
    ]
