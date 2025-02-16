# Generated by Django 4.2.16 on 2025-02-16 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_school_registration', '0006_alter_student_days'),
    ]

    operations = [
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_name', models.CharField(max_length=10, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='student',
            name='days',
            field=models.JSONField(choices=[('MON', 'Monday'), ('TUE', 'Tuesday'), ('WED', 'Wednesday'), ('THU', 'Thursday'), ('FRI', 'Friday'), ('SAT', 'Saturday'), ('SUN', 'Sunday')]),
        ),
    ]
