# Generated by Django 4.0.1 on 2022-01-27 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_page_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=32)),
                ('date_created', models.DateField()),
                ('date_approved', models.DateField()),
                ('date_refused', models.DateField()),
                ('state', models.CharField(choices=[('draft', 'Draft'), ('approved', 'Approved'), ('refused', 'Refused')], default='draft', max_length=32)),
            ],
        ),
    ]