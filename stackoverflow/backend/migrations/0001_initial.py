# Generated by Django 4.1.1 on 2022-10-22 09:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AnswerModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('solved_problem', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='CommentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Photos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='RegisteredMemberModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_state', models.IntegerField(choices=[(0, 'ACTIVE'), (1, 'CLOSED'), (2, 'CANCELED'), (3, 'BLACKLISTED'), (4, 'BLOCKED')], default=0)),
                ('reputation', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='TextPhotoBasedEntityModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('numberOfUsersReported', models.IntegerField(default=0)),
                ('status', models.IntegerField(choices=[(0, 'OPEN'), (1, 'CLOSED'), (2, 'DELETED'), (3, 'DEFAULT')], default=3)),
                ('creationDateTime', models.DateTimeField(auto_now=True)),
                ('lastUpdated', models.DateTimeField(auto_now=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Creator')),
                ('membersWhoDownvoted', models.ManyToManyField(related_name='upvote', to='backend.registeredmembermodel', verbose_name='Downvoting members')),
                ('membersWhoUpvoted', models.ManyToManyField(related_name='Downvote', to='backend.registeredmembermodel', verbose_name='Upvoting members')),
                ('photos', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.photos', verbose_name='List of photos')),
            ],
        ),
        migrations.CreateModel(
            name='QuestionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('views', models.IntegerField(default=0)),
                ('answer', models.ManyToManyField(to='backend.answermodel', verbose_name='answers list')),
                ('comments', models.ManyToManyField(to='backend.commentmodel', verbose_name='comments list')),
                ('entity', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='backend.textphotobasedentitymodel')),
                ('tags', models.ManyToManyField(related_name='tags', to='backend.tags', verbose_name='tags list')),
            ],
        ),
        migrations.AddField(
            model_name='commentmodel',
            name='entity',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='backend.textphotobasedentitymodel'),
        ),
        migrations.AddField(
            model_name='answermodel',
            name='comments',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.commentmodel', verbose_name='comments list'),
        ),
        migrations.AddField(
            model_name='answermodel',
            name='entity',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='backend.textphotobasedentitymodel'),
        ),
    ]
