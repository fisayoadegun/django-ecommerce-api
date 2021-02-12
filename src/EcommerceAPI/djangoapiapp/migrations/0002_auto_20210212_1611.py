# Generated by Django 3.1.6 on 2021-02-12 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapiapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categories'},
        ),
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.CharField(default=False, max_length=255),
        ),
    ]