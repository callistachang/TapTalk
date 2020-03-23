# Generated by Django 3.0.3 on 2020-03-22 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_type',
            field=models.CharField(choices=[('E', 'Expert'), ('U', 'User')], default='U', max_length=1),
        ),
    ]