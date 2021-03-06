# Generated by Django 3.2.5 on 2021-11-30 19:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Website', '0002_delete_appointments'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointments',
            fields=[
                ('doctor', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='Website.doctor')),
                ('date', models.DateField()),
                ('prescription', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'appointments',
                'managed': False,
            },
        ),
    ]
