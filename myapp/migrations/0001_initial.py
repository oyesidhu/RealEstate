# Generated by Django 2.1.1 on 2018-10-23 15:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cityName', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('countryName', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('propertyTitle', models.CharField(max_length=100)),
                ('propertyStreet', models.CharField(max_length=50)),
                ('propertyPostalCode', models.CharField(max_length=6)),
                ('propertyStreetNumber', models.CharField(max_length=5)),
                ('propertyConstructionDate', models.DateField()),
                ('propertyRegistrationDate', models.DateField()),
                ('propertyNumberOfHalls', models.IntegerField()),
                ('propertyNumberOfRooms', models.IntegerField()),
                ('propertyNumberOfBathrooms', models.FloatField()),
                ('propertyNumberOfFloors', models.IntegerField()),
                ('propertyTotalArea', models.FloatField()),
                ('propertyAskingPrice', models.FloatField()),
                ('propertySellingPrice', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='PropertyCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('propertyCategory', models.CharField(choices=[('Single House', 'Single House'), ('Attached House', 'Attached House'), ('Town House', 'Town House'), ('Apartment', 'Apartment'), ('Store', 'Store'), ('Farm', 'Farm'), ('Factory', 'Factory'), ('Mall', 'Mall'), ('Building', 'Building'), ('Other', 'Other')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='PropertyFacing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('propertyFacing', models.CharField(choices=[('North', 'North'), ('South', 'South'), ('East', 'East'), ('West', 'West'), ('Other', 'Other')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='PropertyImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('propertyImageDescription', models.CharField(max_length=100)),
                ('propertyImage', models.ImageField(blank=True, null=True, upload_to='')),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Property')),
            ],
        ),
        migrations.CreateModel(
            name='PropertySector',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('propertySector', models.CharField(choices=[('Private', 'Private'), ('Residential', 'Residential'), ('Commercial', 'Commercial'), ('Government', 'Government'), ('Rural', 'Rural'), ('Other', 'Other')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('provinceName', models.CharField(max_length=25)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Country')),
            ],
        ),
        migrations.AddField(
            model_name='property',
            name='propertyCategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.PropertyCategory'),
        ),
        migrations.AddField(
            model_name='property',
            name='propertyCity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.City'),
        ),
        migrations.AddField(
            model_name='property',
            name='propertyCountry',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Country'),
        ),
        migrations.AddField(
            model_name='property',
            name='propertyFacing',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.PropertyFacing'),
        ),
        migrations.AddField(
            model_name='property',
            name='propertyProvince',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Province'),
        ),
        migrations.AddField(
            model_name='property',
            name='propertySector',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.PropertySector'),
        ),
        migrations.AddField(
            model_name='city',
            name='province',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Province'),
        ),
    ]
