# Generated by Django 3.0.2 on 2020-02-14 10:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('curdapp1', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productdata',
            old_name='cname',
            new_name='Cname',
        ),
        migrations.RenameField(
            model_name='productdata',
            old_name='mobile',
            new_name='Mobile',
        ),
        migrations.RenameField(
            model_name='productdata',
            old_name='price',
            new_name='Price',
        ),
        migrations.RenameField(
            model_name='productdata',
            old_name='product_id',
            new_name='Product_id',
        ),
        migrations.RenameField(
            model_name='productdata',
            old_name='product_name',
            new_name='Product_name',
        ),
    ]
