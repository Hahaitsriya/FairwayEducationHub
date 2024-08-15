# Generated by Django 4.2.14 on 2024-08-14 08:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0003_folder_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='folder',
            name='pictures',
            field=models.ManyToManyField(blank=True, related_name='folders', to='quickstart.picture'),
        ),
        migrations.AlterField(
            model_name='picture',
            name='folder',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='picture_set', to='quickstart.folder'),
        ),
    ]
