# Generated by Django 2.0.2 on 2018-04-02 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swingtime', '0007_auto_20180402_1739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeslot',
            name='slots_available',
            field=models.CharField(default='lol', max_length=150),
        ),
    ]
