from django.db import models
from .constants import Status, AccountStatus


class RegisteredMemberModel(models.Model):    
    user_name = models.CharField(max_length=25, unique=True)
    name = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=100)

    account_state = models.IntegerField(choices=AccountStatus.choices(), default=AccountStatus.ACTIVE.value)
    reputation = models.IntegerField(default=0)

    # class Meta:
    #     excludes = ['password']


class Photos(models.Model):
    photo = models.ImageField()
    creator = models.ForeignKey(RegisteredMemberModel, on_delete=models.CASCADE)


class Tags(models.Model):
    tag = models.CharField(max_length=20, unique=True)


class TextPhotoBasedEntityModel(models.Model):
    text = models.TextField(max_length=300)
    creator = models.OneToOneField(RegisteredMemberModel, on_delete=models.CASCADE, verbose_name='Creator')
    photos = models.ManyToManyField(Photos, verbose_name="List of photos")
    membersWhoDownvoted = models.ManyToManyField(RegisteredMemberModel, verbose_name='Downvoting members')
    membersWhoUpvoted = models.ManyToManyField(RegisteredMemberModel)
    numberOfUsersReported = models.IntegerField(default=0)
    status = models.IntegerField(choices=Status.choices(), default=Status.DEFAULT)

    creationDateTime = models.DateTimeField(auto_now=True)
    lastUpdated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


# class QuestionModel(TextPhotoBasedEntityModel):
#     pass