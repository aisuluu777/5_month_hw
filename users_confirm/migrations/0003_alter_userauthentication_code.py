# Generated by Django 5.1.6 on 2025-03-28 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_confirm', '0002_alter_userauthentication_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userauthentication',
            name='code',
            field=models.CharField(),
        ),
    ]
