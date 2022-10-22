from django.shortcuts import HttpResponseRedirect, render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from backend.models import *
from django.contrib.auth.decorators import login_required
from backend.most_viewed import MostViewed

most_viewed = MostViewed()


def error_404(request, exception):
    return render(request, 'errors/404.html')


def error_500(request):
    return render(request, 'errors/500.html')


def home(request):
    global most_viewed
    for ques in QuestionModel.objects.all():
        most_viewed.add(ques)
    context = {
        "questions": most_viewed.get_list
    }
    return render(request, 'home.html', context)


@login_required(login_url='login')
def ask(request):
    if request.method == "POST":
        title = request.POST.get('title')
        question = request.POST.get("question")
        tags_list = [t.strip().lower() for t in request.POST.get('tags').split(',')]

        user = request.user
        entity = TextPhotoBasedEntityModel.objects.create(
            text=question, creator=user,
        )
        entity.save()

        Tags.objects.get_or_create(tag=tags_list)
        ques = QuestionModel.objects.create(
            title=title,
            entity=entity
        )
        ques.save()

        for tag in tags_list:
            ques.tags.add(Tags.objects.get(tag=tag).id)

        return redirect(f'question/{ques.id}')
    return render(request, 'ask_question.html')


@login_required
def add_comment(request, question_id: int):
    try:
        if request.method == "POST":
            question = QuestionModel.objects.get(id=question_id)

            comment_text = request.POST.get("comment")
            entity = TextPhotoBasedEntityModel.objects.create(
                text=comment_text, creator=User.objects.get(
                    username=request.user),
            )
            entity.save()
            comment = CommentModel.objects.create(
                entity=entity
            )
            comment.save()
            question.comments.add(comment)
            question.save()
    except Exception as e:
        messages.error(request, "Invalid credentials")
    finally:
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


@login_required
def add_answer(request, question_id: int):
    try:
        if request.method == "POST":
            question = QuestionModel.objects.get(id=question_id)

            answer_text = request.POST.get("answer")
            if str(request.user) == question.entity.creator.username:
                messages.error(request, "You can'nt anwer on your question")
            else:
                entity = TextPhotoBasedEntityModel.objects.create(
                    text=answer_text, creator=User.objects.get(
                        username=request.user),
                )
                entity.save()
                answer = AnswerModel.objects.create(
                    entity=entity
                )
                answer.save()
                question.answer.add(answer)
                question.save()
    except Exception as e:
        messages.error(request, f"{e}")
    finally:
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


def question(request, question_id: int):
    global most_viewed
    try:
        question = QuestionModel.objects.get(id=question_id)
        question.views += 1
        question.save()

        most_viewed.add(question)
        context = {
            'question': question
        }
        return render(request, 'question.html', context)
    except Exception as e:
        messages.error(request, f"{e}")
        return render(request, 'errors/404.html')


@login_required
def user_profile(request, user_id: int):
    try:
        user = RegisteredMemberModel.objects.get(id=user_id)
        context = {
            'user': user
        }
        return render(request, 'profile.html', context)
    except Exception as e:
        messages.error(request, f"{e}")
        return render(request, 'errors/404.html')


def loginView(request):
    if request.method == "POST" and not request.user.is_authenticated:
        username = request.POST.get('user_name')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    if request.user.is_authenticated:
        return redirect('home')

    messages.error(request, "User doesnot exists")
    return render(request, 'login.html')


def signup(request):
    if request.method == "POST" and not request.user.is_authenticated:
        username = request.POST.get('user_name')
        f_name = request.POST.get('full_name').split(' ')
        if len(f_name) < 2: f_name.append(' ')
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = User.objects.create_user(
                username=username, password=password, email=email, first_name=f_name[0], last_name=f_name[1])
            user.save()
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user=user)
                return render(request, 'home.html')
        except Exception as e:
            messages.error(request, f"Invalid credentials, {e}")
            return render(request, 'signup.html')
    if request.user.is_authenticated:
        return render(request, 'home.html')
    return render(request, 'signup.html')


def logoutView(request):
    logout(request)

    return redirect('home')
