# Generated by Django 3.2.4 on 2021-06-19 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=40)),
                ('address', models.TextField()),
                ('tax_id', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=3)),
                ('phone', models.CharField(max_length=30)),
            ],
        ),
    ]