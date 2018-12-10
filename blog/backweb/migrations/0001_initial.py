# Generated by Django 2.1.3 on 2018-12-05 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manage_name', models.CharField(db_column='用户名', max_length=10, unique=True, verbose_name='用户名')),
                ('password', models.CharField(db_column='密码', max_length=100, verbose_name='密码')),
                ('create_time', models.DateTimeField(auto_now_add=True, db_column='创建时间', verbose_name='创建时间')),
            ],
            options={
                'db_table': 'manage',
            },
        ),
    ]
