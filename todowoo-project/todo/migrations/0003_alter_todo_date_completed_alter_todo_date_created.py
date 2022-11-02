# Generated by Django 4.1.3 on 2022-11-02 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("todo", "0002_alter_todo_date_completed"),
    ]

    operations = [
        migrations.AlterField(
            model_name="todo",
            name="date_completed",
            field=models.DateTimeField(
                blank=True, null=True, verbose_name="Дата выполнения"
            ),
        ),
        migrations.AlterField(
            model_name="todo",
            name="date_created",
            field=models.DateTimeField(auto_now_add=True, verbose_name="Дата создания"),
        ),
    ]