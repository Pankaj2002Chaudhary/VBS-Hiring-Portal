# Generated by Django 5.1.1 on 2024-09-26 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recruitment_portal', '0005_alter_candidate_age_alter_candidate_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='resume',
            field=models.FileField(default='none', upload_to='resumes/'),
        ),
    ]
