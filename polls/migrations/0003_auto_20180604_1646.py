# Generated by Django 2.0.6 on 2018-06-04 16:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20180604_1625'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='choiche_text',
            new_name='choice_text',
        ),
    ]
