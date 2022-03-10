# Generated by Django 4.0.2 on 2022-02-23 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0006_chemquesmodel_engquesmodel_mathquesmodel_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='basephyQuesModel',
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
            name='baseQuesModel',
        ),
        migrations.DeleteModel(
            name='chemQuesModel',
        ),
        migrations.DeleteModel(
            name='engQuesModel',
        ),
        migrations.DeleteModel(
            name='mathQuesModel',
        ),
        migrations.DeleteModel(
            name='phyQuesModel',
        ),
    ]