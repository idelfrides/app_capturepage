# Generated by Django 2.2.2 on 2019-06-05 20:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_page_cap_img', '0005_auto_20190605_1739'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pagecapimage',
            old_name='imgage_position',
            new_name='image_position',
        ),
    ]
