# Generated by Django 4.0.2 on 2022-02-21 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_basequesmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='chemQuesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=400, null=True)),
                ('questionid', models.CharField(max_length=50, null=True)),
                ('op1', models.CharField(max_length=400, null=True)),
                ('op2', models.CharField(max_length=400, null=True)),
                ('op3', models.CharField(max_length=400, null=True)),
                ('op4', models.CharField(max_length=400, null=True)),
                ('ans', models.CharField(max_length=400, null=True)),
                ('dif', models.FloatField(null=True)),
                ('dis', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='engQuesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=400, null=True)),
                ('questionid', models.CharField(max_length=50, null=True)),
                ('op1', models.CharField(max_length=400, null=True)),
                ('op2', models.CharField(max_length=400, null=True)),
                ('op3', models.CharField(max_length=400, null=True)),
                ('op4', models.CharField(max_length=400, null=True)),
                ('ans', models.CharField(max_length=400, null=True)),
                ('dif', models.FloatField(null=True)),
                ('dis', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='mathQuesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=400, null=True)),
                ('questionid', models.CharField(max_length=50, null=True)),
                ('op1', models.CharField(max_length=400, null=True)),
                ('op2', models.CharField(max_length=400, null=True)),
                ('op3', models.CharField(max_length=400, null=True)),
                ('op4', models.CharField(max_length=400, null=True)),
                ('ans', models.CharField(max_length=400, null=True)),
                ('dif', models.FloatField(null=True)),
                ('dis', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='phyQuesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=400, null=True)),
                ('questionid', models.CharField(max_length=50, null=True)),
                ('op1', models.CharField(max_length=400, null=True)),
                ('op2', models.CharField(max_length=400, null=True)),
                ('op3', models.CharField(max_length=400, null=True)),
                ('op4', models.CharField(max_length=400, null=True)),
                ('ans', models.CharField(max_length=400, null=True)),
                ('dif', models.FloatField(null=True)),
                ('dis', models.FloatField(null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='QuesModel',
        ),
    ]