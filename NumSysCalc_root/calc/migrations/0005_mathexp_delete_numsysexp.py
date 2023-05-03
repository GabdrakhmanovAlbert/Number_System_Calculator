# Generated by Django 4.1.5 on 2023-04-02 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0004_alter_numsysexp_initial_ss_alter_numsysexp_next_ss'),
    ]

    operations = [
        migrations.CreateModel(
            name='MathExp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('initial_num', models.CharField(default='0', max_length=50)),
                ('initial_ss', models.IntegerField(default=0)),
                ('next_ss', models.IntegerField(default=0)),
                ('next_num', models.CharField(default='0', max_length=50)),
                ('dt', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name='NumSysExp',
        ),
    ]
