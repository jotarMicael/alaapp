# Generated by Django 4.1.1 on 2022-12-14 01:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('alaapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('progress', models.FloatField(default=0)),
                ('like_dislike', models.BooleanField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Assignment',
                'verbose_name_plural': 'Assignment',
                'db_table': 'assignment',
            },
        ),
        migrations.CreateModel(
            name='Criteria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
            ],
            options={
                'verbose_name': 'Criteria',
                'verbose_name_plural': 'Criterias',
                'db_table': 'criteria',
            },
        ),
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Day',
                'verbose_name_plural': 'Days',
                'db_table': 'day',
            },
        ),
        migrations.CreateModel(
            name='Scoring',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assessment', models.IntegerField(blank=True, null=True)),
                ('assignment', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='alaapp.assignment')),
                ('criteria', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='alaapp.criteria')),
            ],
            options={
                'verbose_name': 'Scoring',
                'verbose_name_plural': 'Scorings',
                'db_table': 'scoring',
            },
        ),
        migrations.RemoveField(
            model_name='gameelement',
            name='user_completes',
        ),
        migrations.RemoveField(
            model_name='projectarea',
            name='type',
        ),
        migrations.AddField(
            model_name='projectsubarea',
            name='number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='timerestriction',
            name='hour_from',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='timerestriction',
            name='hour_to',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='area',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='alaapp.projectarea'),
        ),
        migrations.AlterField(
            model_name='projectsubarea',
            name='area',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='alaapp.projectarea'),
        ),
        migrations.AlterField(
            model_name='timerestriction',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.DeleteModel(
            name='Progress',
        ),
        migrations.AddField(
            model_name='assignment',
            name='game_element',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='alaapp.gameelement'),
        ),
        migrations.AddField(
            model_name='assignment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='alaapp.user'),
        ),
        migrations.AddField(
            model_name='timerestriction',
            name='days',
            field=models.ManyToManyField(to='alaapp.day'),
        ),
    ]
