# Generated by Django 2.2.2 on 2019-06-05 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_page_cap_img', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagecapimage',
            name='imgPosition',
            field=models.CharField(choices=[('E', 'Esquesda'), ('D', 'Direita')], default='Esquerda', max_length=50),
        ),
    ]
