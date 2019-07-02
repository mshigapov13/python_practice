# Generated by Django 2.2.3 on 2019-07-02 10:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rubric',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=20, unique=True, verbose_name='Name')),
                ('order', models.SmallIntegerField(db_index=True, default=0, verbose_name='Order')),
            ],
        ),
        migrations.CreateModel(
            name='SubRubric',
            fields=[
            ],
            options={
                'verbose_name': 'SubRubric',
                'verbose_name_plural': 'SubRubrics',
                'ordering': ('super_rubric__order', 'super_rubric__name', 'order', 'name'),
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('main.rubric',),
        ),
        migrations.CreateModel(
            name='SuperRubric',
            fields=[
            ],
            options={
                'verbose_name': 'SuperRubric',
                'verbose_name_plural': 'SuperRubrics',
                'ordering': ('order', 'name'),
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('main.rubric',),
        ),
        migrations.AddField(
            model_name='rubric',
            name='super_rubric',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='main.SuperRubric', verbose_name='SuperRubric'),
        ),
    ]