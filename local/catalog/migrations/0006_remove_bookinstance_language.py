# Generated by Django 4.1.6 on 2023-03-06 12:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_alter_bookinstance_language'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookinstance',
            name='language',
        ),
    ]
