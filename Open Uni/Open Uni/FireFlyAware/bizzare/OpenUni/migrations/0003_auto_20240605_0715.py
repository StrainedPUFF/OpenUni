# Generated by Django 3.2.12 on 2024-06-05 07:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('OpenUni', '0002_choice'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Choice',
            new_name='Answer',
        ),
        migrations.RenameField(
            model_name='answer',
            old_name='choice_text',
            new_name='answer_text',
        ),
    ]
