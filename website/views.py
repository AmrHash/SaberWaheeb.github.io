from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.core.mail import send_mail
from django.views.generic import ListView, DetailView, CreateView
from .models import Post, ScientificResearch

def home(request):
    return render(request, 'index.html')

class HomeView(ListView):
    model = Post
    template_name = 'index.html'

def bio(request):
    return render(request, 'bio.html')

def contact(request):
    if request.method == "POST":
        message_name = request.POST ["name"]
        message_phone = request.POST ["phone"]
        message = request.POST ["message"]


        # Send An Email
        send_mail( 
            message_name,
            message,
            message_phone,
            ['saberwaheeb@gmail.com'],
        )


        return render(request, 'contact.html', {})

    else:
        return render(request, 'contact.html', {})


class ArticleDetailView(DetailView):
    model = Post
    template_name= 'article_details.html'
    

#Views of the Scientific Research

def Science(request):
    return render(request, 'science.html')

class ScienceView(ListView):
    model = ScientificResearch
    template_name = 'Science.html'

class ScienceDetailView(DetailView):
    model = ScientificResearch
    template_name= 'Science_details.html'
    object_context_name = 'Science_article'


#Views of the Operation

def Operation(request):
    
    return render(request, 'operation_list.html')

class OperationView(ListView):
    object_context_name = 'operation'
    model = Operation
    template_name = 'operation_list.html'

class OperationDetailView(DetailView):
    model = Operation
    template_name= 'operation_details.html'
    object_context_name = 'operation'