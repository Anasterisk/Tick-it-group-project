# Generated by Django 4.1.4 on 2022-12-19 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickit', '0002_alter_venue_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='ASL_interpreter',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='alcohol_served',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='date',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='photo_url',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='venue',
            name='capacity',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='venue',
            name='onsite_parking',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='venue',
            name='photo_url',
            field=models.TextField(max_length=500, null=True),
        ),
    ]
