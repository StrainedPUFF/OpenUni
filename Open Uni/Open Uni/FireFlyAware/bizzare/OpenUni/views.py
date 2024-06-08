from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
# Create your views here.
# from django.http import HttpResponse
from django.template import loader

from .models import Category


# def index(request):
#     latest_category_list = Category.objects.order_by("-pub_date")[:5]
#     template = loader.get_template("OpenUni/index.html")
#     context = {
#         "latest_category_list": latest_category_list,
#     }
#     return HttpResponse(template.render(context, request))

def index(request):
    latest_category_list = Category.objects.order_by("-pub_date")[:5]
    context = {"latest_category_list": latest_category_list}
    return render(request, "OpenUni/index.html", context)
# def detail(request, category_id):
#     return HttpResponse("These are the categories available%s." % category_id)

def detail(request, question_id):
    category = get_object_or_404(Category, pk=question_id)
    return render(request, "OpenUni/detail.html", {"category": category})



def homepage(request, category_id):
    response = "You're at our homepage %s."
    return HttpResponse(response % category_id)


def menu(request, category_id):
    return HttpResponse("You're at our menu window%s." % category_id)