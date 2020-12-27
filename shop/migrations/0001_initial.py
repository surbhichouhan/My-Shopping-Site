# Generated by Django 2.2.3 on 2019-12-31 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('desc', models.CharField(max_length=300)),
                ('pub_date', models.CharField(max_length=50)),
            ],
        ),
    ]
