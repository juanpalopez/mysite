# Generated by Django 2.0.6 on 2018-06-04 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='choiche_text',
            field=models.CharField(max_length=210),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_text',
            field=models.CharField(max_length=210),
        ),
    ]
