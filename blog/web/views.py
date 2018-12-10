from django.shortcuts import render
from backweb.models import Article1,Type

def index(request):
    if request.method == 'GET':
        types = Type.objects.all()
        article = Article1.objects.all()
        article1 = article.first()
        return render(request, 'web/index.html',{'types':types,'article':article,'article1':article1})


def share(request):
    if request.method == 'GET':
        types = Type.objects.all()
        article = Article1.objects.all()
        article1 = article.first()
        return render(request, 'web/share.html',{'types':types,'article':article,'article1':article1})


def about(request):
    if request.method == 'GET':
        types = Type.objects.all()
        article = Article1.objects.all()
        article1 = article.first()
        return render(request, 'web/about.html',{'types':types,'article':article,'article1':article1})


def info(request,id):
    if request.method == 'GET':
        types = Type.objects.all()
        article = Article1.objects.all()
        article1 = article.first()
        return render(request, 'web/info1.html',{'types':types,'article':article,'article1':article1})




def gbook(request):
    if request.method == 'GET':

        return render(request, 'web/gbook.html')




def infopic(request):
    if request.method == 'GET':

        return render(request, 'web/infopic.html')




