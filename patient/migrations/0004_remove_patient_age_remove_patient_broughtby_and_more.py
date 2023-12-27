# Generated by Django 4.1.13 on 2023-12-23 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0003_remove_patient_city_remove_patient_taluka_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='Age',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='BroughtBy',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='CareOfPerson',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='Case',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='CityTaluka',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='ConditionDuringArrival',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='Country',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='MiddleName',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='ModeOfArrival',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='PinCode',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='ReferredBy',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='RelationWithPatient',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='Religion',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='State',
        ),
        migrations.AlterField(
            model_name='patient',
            name='Email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='patient',
            name='Gender',
            field=models.CharField(max_length=10),
        ),
    ]
