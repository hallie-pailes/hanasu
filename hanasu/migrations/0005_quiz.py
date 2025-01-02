# Generated by Django 4.2.15 on 2024-12-31 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hanasu', '0004_answer_delete_choice'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('total_questions', models.IntegerField()),
                ('total_correct', models.IntegerField()),
            ],
        ),
    ]