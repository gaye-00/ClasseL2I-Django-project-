# Generated by Django 4.1 on 2022-10-03 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('face', '0002_alter_cours_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cours',
            name='cover',
            field=models.ImageField(default='image/default.jpg', null=True, upload_to='image/', verbose_name='Veuiller mettre une image pour embellir le cours'),
        ),
    ]
