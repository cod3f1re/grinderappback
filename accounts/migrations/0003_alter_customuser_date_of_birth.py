# Generated by Django 4.1.7 on 2023-03-02 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_customuser_direction_customuser_num_purchases_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='date_of_birth',
            field=models.DateField(blank=True, default='2023-08-23', null=True),
        ),
    ]
