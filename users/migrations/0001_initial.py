# Generated by Django 4.2.7 on 2023-11-15 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user_type', models.CharField(choices=[('COMUM', 'Comum'), ('LOJISTA', 'Lojista')], default='COMUM', max_length=50)),
                ('name', models.CharField(max_length=200)),
                ('registration', models.CharField(max_length=30, unique=True)),
                ('email', models.CharField(max_length=200, unique=True)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
    ]
