# Generated by Django 4.1.1 on 2022-09-16 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('globalgeo', '0005_remove_post_post_img_post_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]