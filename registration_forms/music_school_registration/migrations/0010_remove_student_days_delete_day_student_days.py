# Generated by Django 4.2.16 on 2025-02-16 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_school_registration', '0009_populate_days'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='days',
        ),
        migrations.DeleteModel(
            name='Day',
        ),
        migrations.AddField(
            model_name='student',
            name='days',
            field=models.JSONField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')], default=''),
            preserve_default=False,
        ),
    ]
