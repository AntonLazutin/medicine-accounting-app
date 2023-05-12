# Generated by Django 4.2.1 on 2023-05-08 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('medicine', '0003_alter_medicine_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('medicine', models.ManyToManyField(related_name='medicines_in_order', to='medicine.medicine')),
            ],
        ),
    ]
