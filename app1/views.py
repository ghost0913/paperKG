from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def v3baisort1(request, response=None):
    response = HttpResponse('[{"id":1,"content":"热卖爆款","url":"9.png"},{"id":2,"content":"坚果炒货","url":"2.png"},]')
    response["Access-Control-Allow-Origin"] = "*"
    return response
