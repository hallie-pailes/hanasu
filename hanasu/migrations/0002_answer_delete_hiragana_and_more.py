# Generated by Django 4.2.15 on 2024-12-28 04:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hanasu', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_text', models.CharField(max_length=255)),
                ('is_correct', models.BooleanField(default=False)),
            ],
        ),
        migrations.DeleteModel(
            name='Hiragana',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='answer_1',
            new_name='question_text',
        ),
        migrations.RemoveField(
            model_name='question',
            name='answer_2',
        ),
        migrations.RemoveField(
            model_name='question',
            name='answer_3',
        ),
        migrations.RemoveField(
            model_name='question',
            name='answer_4',
        ),
        migrations.RemoveField(
            model_name='question',
            name='text',
        ),
        migrations.DeleteModel(
            name='Lesson',
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hanasu.question'),
        ),
    ]