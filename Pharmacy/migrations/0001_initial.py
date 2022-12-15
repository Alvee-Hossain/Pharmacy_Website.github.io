# Generated by Django 4.1.1 on 2022-10-26 15:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('Cart_ID', models.BigAutoField(primary_key=True, serialize=False)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='edit_profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='publish',
            fields=[
                ('Book_id', models.IntegerField(primary_key=True, serialize=False)),
                ('Book_name', models.CharField(max_length=100)),
                ('Author', models.CharField(max_length=100)),
                ('file_upload', models.FileField(null=True, upload_to='')),
                ('language', models.CharField(max_length=50)),
                ('edition', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=50)),
                ('price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='user_review',
            fields=[
                ('review_id', models.IntegerField(primary_key=True, serialize=False)),
                ('Book_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pharmacy.publish')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birth_date', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=200)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('Pay_ID', models.BigAutoField(primary_key=True, serialize=False)),
                ('Pay_type', models.CharField(max_length=100)),
                ('amount', models.FloatField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Author', models.CharField(max_length=50)),
                ('current_price', models.FloatField()),
                ('After_discount', models.FloatField()),
                ('Book_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pharmacy.publish')),
            ],
        ),
        migrations.CreateModel(
            name='delete',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('review', models.FloatField()),
                ('reason', models.CharField(max_length=500)),
                ('author', models.CharField(max_length=100)),
                ('Book_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pharmacy.publish')),
            ],
        ),
        migrations.CreateModel(
            name='categories',
            fields=[
                ('c_id', models.IntegerField(primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=200)),
                ('Book_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pharmacy.publish')),
            ],
        ),
        migrations.CreateModel(
            name='Cart_item',
            fields=[
                ('CartItems_ID', models.BigAutoField(primary_key=True, serialize=False)),
                ('Book_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pharmacy.publish')),
                ('Cart_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pharmacy.cart')),
            ],
        ),
        migrations.CreateModel(
            name='admin_reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Book_Name', models.CharField(max_length=200)),
                ('Book_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pharmacy.publish')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='admin_accounts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bkash_id', models.IntegerField()),
                ('nagad_id', models.IntegerField()),
                ('dbbl_id', models.IntegerField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]