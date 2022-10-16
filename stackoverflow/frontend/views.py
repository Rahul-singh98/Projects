from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password, check_password
from backend.models import RegisteredMemberModel
from backend.manager import RegisteredMember
from backend.ood import Question
from backend.utility import Tag

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

def home(request):
    global question1, question2
    # if request.GET.get('search'):
    #     context = {
    #     "questions": [question1]
    #     }
    # else:
    context = {
        "questions": [question1, question2]
    }
    return render(request, 'home.html', context)

def ask(request):

    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'ask_question.html')

def question(request, question_id:int):
    global question1 , question2
    
    context = {
        'question': question1 if question_id == 1 else question2
    }
    return render(request, 'question.html', context)

def user_profile(request, user_id: int):
    if not request.user.is_authenticated:
        return redirect('login')

    global member1, member2

    context = {
        'user': member1 if user_id == 1 else member2
    }
    return render(request, 'profile.html', context)

def login(request):
    if request.method == "POST":
        username = request.POST.get('user_name')
        password = request.POST.get('password')
        print(username, password)
        user = authenticate(request, username=username, password=password)

        print("User => ", user)
        if user is None:
            return redirect('login')
        return render(request, 'home.html', {'user':user})
    return render(request, 'login.html')

def signup(request):
    if request.method == "POST":
        user_name = request.POST.get('user_name')
        f_name = request.POST.get('full_name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        cipher = make_password(password)

        user = RegisteredMemberModel(
            user_name = user_name,
            name = f_name,
            email = email,
            password = cipher
        )

        try:
            user.save()
            authenticate(request, username=user_name, password=cipher)
            return render(request, 'home.html')
        except Exception as e:
            print(e)


    return render(request, 'signup.html')