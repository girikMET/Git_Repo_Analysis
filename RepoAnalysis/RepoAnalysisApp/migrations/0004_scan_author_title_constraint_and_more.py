# Generated by Django 4.2.3 on 2023-07-20 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RepoAnalysisApp', '0003_scan_scan_created_at_scan_scan_updated_at_and_more'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='scan',
            constraint=models.UniqueConstraint(fields=('author', 'title'), name='author title constraint'),
        ),
        migrations.AddConstraint(
            model_name='user_scans',
            constraint=models.UniqueConstraint(fields=('scan_id', 'name', 'url_name'), name='scan session repo constraint'),
        ),
    ]
