# Generated by Django 4.2 on 2023-04-14 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mypro', '0003_rename_result_patient_classification_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female')], default='male', max_length=6),
        ),
        migrations.AlterField(
            model_name='patient',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female')], default='male', max_length=6),
        ),
    ]
