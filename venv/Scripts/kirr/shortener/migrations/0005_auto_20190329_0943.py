# Generated by Django 2.1.7 on 2019-03-29 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0004_auto_20190329_0847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kirrurl',
            name='shortcode',
            field=models.CharField(blank='True', max_length=15, unique='True'),
        ),
    ]
