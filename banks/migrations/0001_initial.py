# Generated by Django 5.0.6 on 2024-06-21 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=10)),
                ('branch_name', models.CharField(max_length=100)),
                ('branch_code', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=200)),
                ('telephone', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Bank',
                'verbose_name_plural': 'Banks',
            },
        ),
    ]