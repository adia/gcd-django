# Generated by Django 3.2.11 on 2022-02-13 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indexer', '0005_indexer_cover_letterer_creator_only'),
    ]

    operations = [
        migrations.AddField(
            model_name='indexer',
            name='use_tabs',
            field=models.BooleanField(db_index=True, default=True),
        ),
    ]
