# Generated by Django 2.2.1 on 2019-05-25 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0007_auto_20190526_0106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(max_length=20),
        ),
    ]