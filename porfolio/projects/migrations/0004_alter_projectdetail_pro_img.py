# Generated by Django 4.2.6 on 2023-12-12 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_projectdetail_project_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectdetail',
            name='pro_img',
            field=models.FileField(upload_to='project_imgs/'),
        ),
    ]
