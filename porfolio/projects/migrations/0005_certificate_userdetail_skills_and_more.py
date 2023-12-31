# Generated by Django 4.2.6 on 2023-12-18 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_alter_projectdetail_pro_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cert_img', models.FileField(upload_to='certificates')),
                ('crt_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='userdetail',
            name='skills',
            field=models.TextField(default='None', max_length=150),
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='user_img',
            field=models.ImageField(upload_to='user_imgs'),
        ),
    ]
