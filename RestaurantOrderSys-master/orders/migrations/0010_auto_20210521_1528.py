# Generated by Django 2.2 on 2021-05-21 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_savedcarts'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='DinnerPlatters',
            new_name='Hawka',
        ),
        migrations.DeleteModel(
            name='Sub',
        ),
        migrations.RenameField(
            model_name='hawka',
            old_name='dish_name',
            new_name='hawka',
        ),
        migrations.AddField(
            model_name='userorder',
            name='token',
            field=models.TextField(default='A1'),
        ),
    ]
