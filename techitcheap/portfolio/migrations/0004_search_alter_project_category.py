# Generated by Django 5.1.1 on 2024-10-02 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_alter_project_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('your_field', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='project',
            name='category',
            field=models.CharField(blank=True, choices=[('Website Design', 'Website Design'), ('Product Development', 'Product Development'), ('Mobile App Development', 'Mobile App Development'), ('Mobile App and Web Maintenance', 'Mobile App and Web Maintenance')], max_length=255, null=True),
        ),
    ]
