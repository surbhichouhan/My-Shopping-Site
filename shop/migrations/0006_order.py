# Generated by Django 2.2.3 on 2020-01-17 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_Id', models.AutoField(primary_key=True, serialize=False)),
                ('itemJson', models.CharField(max_length=500)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=90)),
                ('state', models.CharField(max_length=70)),
                ('Zip', models.CharField(max_length=70)),
                ('city', models.CharField(max_length=70)),
                ('address', models.CharField(max_length=100)),
                ('phone', models.CharField(default='', max_length=50)),
            ],
        ),
    ]
