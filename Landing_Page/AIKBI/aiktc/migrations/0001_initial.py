# Generated by Django 4.0.4 on 2022-11-02 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=50)),
                ('startup_name', models.CharField(max_length=50)),
                ('website_url', models.CharField(default=None, max_length=100, null=True)),
                ('startup_email', models.EmailField(max_length=254)),
                ('mobile', models.IntegerField()),
                ('founder_name', models.CharField(max_length=20)),
                ('details', models.CharField(max_length=400)),
                ('company_type', models.CharField(max_length=20)),
                ('industry', models.CharField(max_length=20)),
                ('title_startup', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('funding_type', models.CharField(max_length=20)),
                ('more_info', models.CharField(max_length=300)),
                ('current_status', models.CharField(max_length=30)),
                ('pitch_deck', models.CharField(default=None, max_length=50)),
            ],
        ),
    ]
