# Generated by Django 3.2.6 on 2022-01-13 14:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('topic', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=50)),
                ('content', models.CharField(max_length=100)),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='topic.topic')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]