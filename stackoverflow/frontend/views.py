from django.shortcuts import render
from backend.manager import RegisteredMember
from backend.ood import Question
from backend.utility import Tag

def home(request):
    member1 = RegisteredMember(1, "rahul", "rahul", "rahul@mail.com")
    question1 = Question(1, member1, "why showing int not callable",
        "When i tried to call {{ ques.getVotesCount }} showing this error.")

    member2 = RegisteredMember(2, "gurdayal", "gurdayal", "gurdayal@mail.com")
    question2 = Question(2, member2, "Who is Frontend expert with django\
        and also have an industry experience of 30 years ??",
    "Who is Frontend expert with django\
        and also have an industry experience of 30 years?\n\
        I just wanted to know if anyone knows this please let me know.\n\
            Thanks in advance.")
    context = {
        "questions": [question1, question2]
    }
    return render(request, 'home.html', context)
