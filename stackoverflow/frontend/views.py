from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from backend.models import *
from backend.manager import RegisteredMember
from backend.ood import Question
from backend.utility import Tag
from django.contrib.auth.decorators import login_required

tag1 = Tag("python")
tag2 = Tag('bash')
taglist = [tag1, tag1, tag1, tag1, tag2, tag2, tag2, tag2, tag2]

member1 = RegisteredMember(1, "rahul", "rahul", "rahul@mail.com")
question1 = Question(1, member1, "why showing int not callable",
    "When i tried to call {{ ques.getVotesCount }} showing this error.", None,
    taglist)

member2 = RegisteredMember(2, "gurdayal", "gurdayal", "gurdayal@mail.com")
question2 = Question(2, member2, "Who is Frontend expert with django\
    and also have an industry experience of 30 years ??",
"Who is Frontend expert with django\
    and also have an industry experience of 30 years?\n\
    I just wanted to know if anyone knows this please let me know.\n\
        Thanks in advance.", None, taglist)

def error_404(request, exception):
    return render(request, 'errors/404.html')

def error_500(request):
    return render(request, 'errors/500.html')


def home(request):
    global question1, question2
    context = {
        "questions": [question1, question2]
    }
    return render(request, 'home.html', context)

@login_required(login_url='login')
def ask(request):
    if request.method == "POST":
        title = request.POST.get('title')
        question = request.POST.get("question")
        tags = request.POST.get('tags').split(',')

        user = request.user
        entity = TextPhotoBasedEntityModel.objects.create(
            text=question, creator=user,
            )
        entity.save()

        tags_list = []
        for tag in tags:
            tags_list.append(Tags.objects.get_or_create(tag=tag))
        
        ques = QuestionModel.objects.create(
            title=title,
            entity=entity
        )
        ques.tags.set = tags_list
        ques.save()

        return redirect(f'question/{ques.id}')
    return render(request, 'ask_question.html')

def question(request, question_id:int):
    try:
        question = QuestionModel.objects.get(id=question_id)
        context = {
            'question': question
        }
        return render(request, 'question.html', context)
    except Exception as e:
        print(e)
        return render(request, 'errors/404.html')

def user_profile(request, user_id: int):
    if not request.user.is_authenticated:
        return redirect('login')

    global member1, member2

    context = {
        'user': member1 if user_id == 1 else member2
    }
    return render(request, 'profile.html', context)

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
    return render(request, 'login.html')

def signup(request):
    if request.method == "POST":
        username = request.POST.get('user_name')
        f_name = request.POST.get('full_name').split(' ')
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.create_user(username=username, password=password, email=email, first_name=f_name[0], last_name=f_name[1])
            user.save()
            user = authenticate(username=username, password=password)
            if user is not None:
                login(user)
                return render(request, 'home.html')
        except Exception as e:
            messages.error(request, "Invalid credentials")
            return render(request, 'signup.html')

    return render(request, 'signup.html')

def logoutView(request):
    logout(request)

    return redirect('home')



