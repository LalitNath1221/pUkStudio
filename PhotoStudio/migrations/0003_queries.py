# Generated by Django 3.1.5 on 2021-06-19 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PhotoStudio', '0002_auto_20210325_1535'),
    ]

    operations = [
        migrations.CreateModel(
            name='Queries',
            fields=[
                ('User_id', models.AutoField(primary_key=True, serialize=False)),
                ('User_Name', models.CharField(default=' ', max_length=50)),
                ('User_Email', models.EmailField(max_length=50)),
                ('User_Contact', models.CharField(max_length=10, null=True)),
                ('User_QueryDate', models.DateField(auto_now_add=True)),
                ('User_Discription', models.TextField()),
            ],
        ),
    ]
