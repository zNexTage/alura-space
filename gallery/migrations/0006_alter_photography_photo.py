# Generated by Django 4.1.5 on 2023-01-25 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0005_rename_created_at_photography_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photography',
            name='photo',
            field=models.ImageField(blank=True, upload_to='fotos/%Y/%M/%d/'),
        ),
    ]