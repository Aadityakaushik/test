# Generated by Django 4.2.4 on 2023-08-12 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_lis_uname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sign',
            old_name='uname',
            new_name='name',
        ),
        migrations.AddField(
            model_name='sign',
            name='email',
            field=models.CharField(default='', max_length=122),
        ),
    ]