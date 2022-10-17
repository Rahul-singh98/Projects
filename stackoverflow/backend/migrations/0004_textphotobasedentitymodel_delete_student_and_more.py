# Generated by Django 4.1.2 on 2022-10-17 07:10

import backend.constants
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('backend', '0003_student_teacher'),
    ]

    operations = [
        migrations.CreateModel(
            name='TextPhotoBasedEntityModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=300)),
                ('numberOfUsersReported', models.IntegerField(default=0)),
                ('status', models.IntegerField(choices=[(0, 'OPEN'), (1, 'CLOSED'), (2, 'DELETED'), (3, 'DEFAULT')], default=backend.constants.Status['DEFAULT'])),
                ('creationDateTime', models.DateTimeField(auto_now=True)),
                ('lastUpdated', models.DateTimeField(auto_now=True)),
                ('creator', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Creator')),
                ('membersWhoUpvoted', models.ManyToManyField(to='backend.registeredmembermodel', verbose_name='Upvoting members')),
                ('photos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.photos', verbose_name='List of photos')),
            ],
        ),
        migrations.DeleteModel(
            name='Student',
        ),
        migrations.DeleteModel(
            name='Teacher',
        ),
    ]
