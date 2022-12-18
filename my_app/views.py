# import imp
# from django.shortcuts import render
# from django.http import HttpResponse
# def first_view(req):
#     return render(req,'firsthtml.html')
from django.shortcuts import render
from django.http import HttpResponse
from . forms import sample

# Create your views here.
def first_view(req):
    return HttpResponse("Hii Iam Shoeb")


def second_view(req):
    return render(req, "temp.html")


def index(request):
    student = sample()
    return render(request, "firsthtml.html", {"form": student})


forms.py
from django import forms


class sample(forms.Form):
    g = (("1", "cse"), ("2", "csm"), ("3", "ece"))
    h = (("1", "male"), ("2", "female"))
    c = (("1", "JAVA"), ("2", "C++"))
    n1 = forms.CharField(label="Name")
    e1 = forms.EmailField(label="Email")
    g1 = forms.ChoiceField(label="course", choices=g)
    a1 = forms.IntegerField(label="age")
    h1 = forms.ChoiceField(label="Gender", choices=h, widget=forms.RadioSelect)
    c1 = forms.ChoiceField(
        label="courses", choices=c, widget=forms.CheckboxSelectMultiple
    )
    d1 = forms.DateInput(label="DOB")


# Create your views here.
