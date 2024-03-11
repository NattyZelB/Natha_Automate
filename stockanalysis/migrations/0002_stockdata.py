# Generated by Django 4.2 on 2024-03-09 14:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stockanalysis', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StockData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_price', models.CharField(blank=True, max_length=25, null=True)),
                ('price_changed', models.CharField(blank=True, max_length=25, null=True)),
                ('previous_close', models.CharField(blank=True, max_length=25, null=True)),
                ('week_52_high', models.CharField(blank=True, max_length=25, null=True)),
                ('week_52_low', models.CharField(blank=True, max_length=25, null=True)),
                ('market_cap', models.CharField(blank=True, max_length=25, null=True)),
                ('pe_ratio', models.CharField(blank=True, max_length=25, null=True)),
                ('dividend_yield', models.CharField(blank=True, max_length=25, null=True)),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stockanalysis.stock')),
            ],
        ),
    ]
