# Generated by Django 3.2.5 on 2022-08-23 11:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangouploads', '0006_rename_doc_name_drink_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='drink',
            name='description',
        ),
    ]
