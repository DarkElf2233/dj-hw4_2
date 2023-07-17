# Generated by Django 4.2.3 on 2023-07-14 13:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='Название')),
            ],
        ),
        migrations.CreateModel(
            name='ArticleTagsPositions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_main', models.BooleanField()),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='positions', to='articles.article')),
                ('tags', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='positions', to='articles.tags')),
            ],
        ),
    ]
