# Generated by Django 2.0 on 2018-02-19 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Diary',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('publish_date', models.DateTimeField(verbose_name='event date')),
                ('public', models.BooleanField(default=True)),
                ('text', models.CharField(max_length=10000)),
            ],
        ),
    ]
