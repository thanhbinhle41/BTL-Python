# Generated by Django 3.2.8 on 2021-11-11 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageFolder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img0', models.ImageField(upload_to='')),
                ('img1', models.ImageField(upload_to='')),
                ('img2', models.ImageField(upload_to='')),
                ('img3', models.ImageField(upload_to='')),
                ('img4', models.ImageField(upload_to='')),
                ('img5', models.ImageField(upload_to='')),
                ('img6', models.ImageField(upload_to='')),
                ('img7', models.ImageField(upload_to='')),
                ('img8', models.ImageField(upload_to='')),
            ],
        ),
    ]
