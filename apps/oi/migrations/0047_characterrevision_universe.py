# Generated by Django 3.2.19 on 2023-10-14 21:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gcd', '0049_character_universe'),
        ('oi', '0046_universe_story'),
    ]

    operations = [
        migrations.AddField(
            model_name='characterrevision',
            name='universe',
            field=models.ForeignKey(null=True, blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='character_revisions', to='gcd.universe'),
        ),
    ]
