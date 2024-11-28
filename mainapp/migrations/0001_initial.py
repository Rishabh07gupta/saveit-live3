# Generated by Django 3.1.8 on 2021-08-27 19:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, null=True)),
                ('phone', models.CharField(max_length=12, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True, null=True, verbose_name='date added')),
                ('due', models.CharField(blank=True, max_length=10, null=True)),
                ('Address', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DebitCollection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('debit', models.IntegerField(null=True)),
                ('debitdate', models.DateField(blank=True, null=True)),
                ('debitdescription', models.CharField(max_length=500, null=True)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='DebitCollection', to='mainapp.customer')),
            ],
        ),
        migrations.CreateModel(
            name='CreditCollection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('credit', models.IntegerField(null=True)),
                ('creditdate', models.DateField(blank=True, null=True)),
                ('creditdescription', models.CharField(max_length=500, null=True)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='CreditCollection', to='mainapp.customer')),
            ],
        ),
    ]