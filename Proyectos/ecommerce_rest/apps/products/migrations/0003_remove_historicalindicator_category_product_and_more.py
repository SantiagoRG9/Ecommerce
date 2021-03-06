# Generated by Django 4.0.1 on 2022-01-28 20:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_historicalproduct_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicalindicator',
            name='category_product',
        ),
        migrations.RemoveField(
            model_name='historicalindicator',
            name='history_user',
        ),
        migrations.RemoveField(
            model_name='historicalmeasureunit',
            name='history_user',
        ),
        migrations.RemoveField(
            model_name='historicalproduct',
            name='category_product',
        ),
        migrations.RemoveField(
            model_name='historicalproduct',
            name='history_user',
        ),
        migrations.RemoveField(
            model_name='historicalproduct',
            name='measure_unit',
        ),
        migrations.DeleteModel(
            name='HistoricalCategoryProduct',
        ),
        migrations.DeleteModel(
            name='HistoricalIndicator',
        ),
        migrations.DeleteModel(
            name='HistoricalMeasureUnit',
        ),
        migrations.DeleteModel(
            name='HistoricalProduct',
        ),
    ]
