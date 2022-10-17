from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .constants import Status, AccountStatus


class RegisteredMemberModel(models.Model): 
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    account_state = models.IntegerField(choices=AccountStatus.choices(), default=AccountStatus.ACTIVE.value)
    reputation = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} {self.user.email}"

@receiver(post_save, sender=User)
def create_user_registeredmembermodel(sender, instance, created, **kwargs):
    if created:
        RegisteredMemberModel.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_registeredmembermodel(sender, instance, **kwargs):
    instance.registeredmembermodel.save()


class Photos(models.Model):
    photo = models.ImageField()


class Tags(models.Model):
    tag = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.tag}"


class TextPhotoBasedEntityModel(models.Model):
    text = models.TextField(max_length=300)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Creator')
    photos = models.ForeignKey(Photos, verbose_name="List of photos", on_delete=models.CASCADE, null=True)
    membersWhoDownvoted = models.ManyToManyField("RegisteredMemberModel", verbose_name='Downvoting members', related_name='upvote')
    membersWhoUpvoted = models.ManyToManyField("RegisteredMemberModel", verbose_name="Upvoting members", related_name='Downvote') 
    numberOfUsersReported = models.IntegerField(default=0)
    status = models.IntegerField(choices=Status.choices(), default=Status.DEFAULT.value)

    creationDateTime = models.DateTimeField(auto_now=True)
    lastUpdated = models.DateTimeField(auto_now=True)


class QuestionModel(models.Model):
    title = models.CharField(max_length=200)
    tags = models.ManyToManyField("Tags", verbose_name="tags list", related_name="tags")
    comments = models.ForeignKey("CommentModel", verbose_name="comments list", on_delete=models.CASCADE, null=True)
    answer = models.ForeignKey("AnswerModel", verbose_name="answers list", on_delete=models.CASCADE, null=True)
    entity = models.OneToOneField("TextPhotoBasedEntityModel", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}"


class AnswerModel(models.Model):
    solved_problem = models.BooleanField(default=False)
    comments = models.ForeignKey("CommentModel", verbose_name="comments list", on_delete=models.CASCADE)
    entity = models.OneToOneField("TextPhotoBasedEntityModel", on_delete=models.CASCADE)


class CommentModel(models.Model):
    entity = models.OneToOneField("TextPhotoBasedEntityModel", on_delete=models.CASCADE)
