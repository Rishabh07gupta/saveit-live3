# Generated by Django 3.1.8 on 2021-08-31 17:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0007_collection_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collection',
            name='user',
        ),
        migrations.AlterField(
            model_name='collection',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainapp.customer'),
        ),
    ]
