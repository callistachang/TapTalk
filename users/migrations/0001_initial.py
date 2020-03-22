# Generated by Django 3.0.3 on 2020-03-22 13:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('biography', models.TextField(blank=True, null=True)),
                ('is_taptalk_mode_on', models.BooleanField(blank=True, default=True)),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
        ),
        migrations.CreateModel(
            name='Expert',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='users.User')),
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('is_verified', models.BooleanField(default=False)),
                ('expert_title', models.CharField(max_length=200)),
                ('saved_articles', models.ManyToManyField(blank=True, related_name='experts_who_saved', to='articles.Article')),
            ],
            options={
                'verbose_name': 'Expert',
                'verbose_name_plural': 'Experts',
            },
            bases=('users.user',),
        ),
        migrations.CreateModel(
            name='CommonUser',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='users.User')),
                ('facebook_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('saved_articles', models.ManyToManyField(blank=True, related_name='users_who_saved', to='articles.Article')),
            ],
            options={
                'verbose_name': 'CommonUser',
                'verbose_name_plural': 'CommonUsers',
            },
            bases=('users.user',),
        ),
    ]
