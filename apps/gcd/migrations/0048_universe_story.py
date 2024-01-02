# Generated by Django 3.2.19 on 2023-09-30 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gcd', '0047_feature_disambiguation'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='universe',
            field=models.ManyToManyField(to='gcd.Universe'),
        ),
        migrations.AddField(
            model_name='storycharacter',
            name='universe',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gcd.universe'),
        ),
    ]
