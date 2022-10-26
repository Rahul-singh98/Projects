from django.shortcuts import render
from django.http import HttpResponse
from .models import Code
from .forms import CodeForm


# Create your views here.
def add_code(request):
    if request.method == "POST":
        form = CodeForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Program added')
        else:
            return HttpResponse('not valid')
    else:
        form = CodeForm()
    return render(request, 'code_editor/add_code.html', {'code_form': form})
