# Generated by Django 4.1.1 on 2022-12-13 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pharmacy', '0004_employeepanel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeepanel',
            name='ID',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='employeepanel',
            name='number',
            field=models.IntegerField(),
        ),
    ]