# Generated by Django 4.0.5 on 2023-03-11 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0004_article_unique_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='visuals',
            field=models.FileField(null=True, upload_to='uploads/'),
        ),
    ]