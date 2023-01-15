# Generated by Django 3.2.4 on 2021-09-15 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImageUploadModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('imag', models.ImageField(upload_to='uploads')),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
