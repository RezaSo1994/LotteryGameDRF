# Generated by Django 3.2.9 on 2021-11-29 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BuyTickets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tickets', models.IntegerField(verbose_name=range(0, 100))),
                ('discunt', models.FileField(upload_to='', verbose_name=range(0, 100))),
            ],
        ),
    ]