# Generated by Django 4.0.1 on 2022-01-13 18:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_book_publisher'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField()),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.book')),
            ],
        ),
    ]