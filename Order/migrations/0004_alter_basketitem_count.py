# Generated by Django 5.0.6 on 2024-09-30 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0003_alter_basketitem_basket'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basketitem',
            name='count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
