# Generated by Django 3.2.16 on 2022-12-14 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('dob', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=50)),
                ('cpassword', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]