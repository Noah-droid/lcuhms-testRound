# Generated by Django 3.1 on 2022-08-05 02:21

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='blocks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Block_Name', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='floors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Floor_Number', models.IntegerField(null=True)),
                ('Number_of_Rooms', models.IntegerField(null=True)),
                ('Block_Name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hostelapp.blocks')),
            ],
        ),
        migrations.CreateModel(
            name='room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Room_No', models.IntegerField(null=True)),
                ('Capacity', models.IntegerField(default=4)),
                ('Number_already_occupied', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(4), django.core.validators.MinValueValidator(0)])),
                ('hide', models.BooleanField(default=False)),
                ('Block_Name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hostelapp.blocks')),
                ('Floor_Number', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hostelapp.floors')),
            ],
        ),
        migrations.CreateModel(
            name='warden',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Block_Name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hostelapp.blocks')),
                ('Floor_Number', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hostelapp.floors')),
                ('Warden_ID', models.ForeignKey(limit_choices_to={'groups__name': 'warden'}, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='student_room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(limit_choices_to={'groups__name': 'student'}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('user_room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hostelapp.room')),
            ],
        ),
        migrations.AddField(
            model_name='room',
            name='Warden_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hostelapp.warden'),
        ),
    ]
