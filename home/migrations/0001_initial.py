# Generated by Django 4.0.6 on 2022-07-18 11:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('logo', models.ImageField(upload_to='logo')),
                ('carousel1', models.ImageField(upload_to='carousel')),
                ('carousel2', models.ImageField(upload_to='carousel')),
                ('carousel3', models.ImageField(upload_to='carousel')),
                ('banner', models.ImageField(upload_to='banner')),
                ('favicon', models.ImageField(upload_to='favicon')),
                ('about', models.TextField()),
                ('copyright', models.IntegerField()),
            ],
            options={
                'verbose_name': 'CompanyProfile',
                'verbose_name_plural': 'CompanyProfile',
                'db_table': 'companyprofile',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Type',
                'verbose_name_plural': 'Type',
                'db_table': 'type',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('pix', models.ImageField(upload_to='pix')),
                ('price', models.IntegerField()),
                ('discount_price', models.IntegerField(blank=True, null=True)),
                ('network', models.CharField(max_length=100)),
                ('launch', models.CharField(max_length=100)),
                ('memory', models.CharField(max_length=100)),
                ('camera', models.CharField(max_length=100)),
                ('featured', models.BooleanField(default=False)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.type')),
            ],
            options={
                'verbose_name': 'Phone',
                'verbose_name_plural': 'Phone',
                'db_table': 'phone',
                'managed': True,
            },
        ),
    ]
