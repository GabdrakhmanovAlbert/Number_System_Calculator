# Generated by Django 4.1.5 on 2023-03-30 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0002_rename_mathexpression_mathexp'),
    ]

    operations = [
        migrations.CreateModel(
            name='NumSysExp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('initial_num', models.CharField(default='0', max_length=50)),
                ('initial_ss', models.IntegerField()),
                ('next_ss', models.IntegerField()),
                ('next_num', models.CharField(default='0', max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='MathExp',
        ),
    ]
