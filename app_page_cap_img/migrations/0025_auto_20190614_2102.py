# Generated by Django 2.2.2 on 2019-06-15 00:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_page_cap_img', '0024_leadsemail_timestamp'),
    ]

    operations = [
        migrations.RenameField(
            model_name='configuracao',
            old_name='midea_position',
            new_name='media_position',
        ),
    ]
