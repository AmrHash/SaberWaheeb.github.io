from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.core.mail import send_mail
from django.views.generic import ListView, DetailView
from .models import Post

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



    

#Views of the Scientific Research

def Science(request):
    return render(request, 'science.html')




#Views of the Operation

def Operation(request):
    
    return render(request, 'operation_list.html')


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'

