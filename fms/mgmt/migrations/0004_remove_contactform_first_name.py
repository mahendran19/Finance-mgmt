# Generated by Django 3.0.3 on 2020-05-21 05:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mgmt', '0003_remove_contactform_totalsalary'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactform',
            name='first_name',
        ),
    ]