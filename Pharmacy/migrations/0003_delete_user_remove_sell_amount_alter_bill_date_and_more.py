# Generated by Django 4.1.1 on 2022-10-26 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pharmacy', '0002_bill_drugs_employee_order_pre_book_sell_storage_user_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
        migrations.RemoveField(
            model_name='sell',
            name='Amount',
        ),
        migrations.AlterField(
            model_name='bill',
            name='Date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='bill',
            name='Time',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='drugs',
            name='Drug_Link',
            field=models.URLField(),
        ),
    ]