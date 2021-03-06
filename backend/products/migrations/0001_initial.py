# Generated by Django 4.0.3 on 2022-03-11 10:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('batch', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=1000)),
                ('product_quantity', models.BigIntegerField()),
                ('buying_price', models.BigIntegerField()),
                ('selling_price', models.BigIntegerField()),
                ('profit', models.BigIntegerField()),
                ('percentage_profit', models.BigIntegerField()),
                ('batch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='batch.batch')),
            ],
        ),
    ]
