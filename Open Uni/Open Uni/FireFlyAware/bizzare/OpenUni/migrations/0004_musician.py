# Generated by Django 3.2.12 on 2024-06-05 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OpenUni', '0003_auto_20240605_0715'),
    ]

    operations = [
        migrations.CreateModel(
            name='Musician',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
            ],
        ),
    ]