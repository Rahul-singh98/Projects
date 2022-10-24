from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(RegisteredMemberModel)
admin.site.register(Tags)
admin.site.register(QuestionModel)
admin.site.register(AnswerModel)
admin.site.register(CommentModel)
admin.site.register(Photos)
admin.site.register(TextPhotoBasedEntityModel)
