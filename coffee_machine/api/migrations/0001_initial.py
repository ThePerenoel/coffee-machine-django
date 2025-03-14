# Generated by Django 5.1.7 on 2025-03-13 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DrinkOrder',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('drink_type', models.CharField(max_length=255)),
                ('number_of_sugars', models.IntegerField()),
                ('is_extra_hot', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
