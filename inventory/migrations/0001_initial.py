# Generated by Django 3.0.7 on 2020-06-30 13:49

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import inventory.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', inventory.models.VarCharField(verbose_name='title')),
                ('slug', models.SlugField(verbose_name='slug')),
                ('attributes', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True, verbose_name='attributes')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='updated')),
            ],
            options={
                'verbose_name': 'product',
                'verbose_name_plural': 'products',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(help_text='Positive numbers mean incoming stock, negative numbers mean outgoing', verbose_name='quantity')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='updated')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Product', verbose_name='product')),
            ],
            options={
                'verbose_name': 'order',
                'verbose_name_plural': 'orders',
                'ordering': ['-created'],
            },
        ),
    ]
