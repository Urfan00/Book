# Generated by Django 5.0.6 on 2024-07-05 16:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0002_alter_slider_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='slider',
            options={'verbose_name': 'SliderTek', 'verbose_name_plural': 'SliderCut'},
        ),
        migrations.RenameField(
            model_name='slider',
            old_name='describtion',
            new_name='description',
        ),
    ]