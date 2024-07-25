from django.shortcuts import render

#Dummy Database
posts = [
    {
        'author':'Bruno',
        'title':'Post 101',
        'content':'This is my head speaking',
        'date':'July, 25 2024'
    },
    {
        'author':'Manoti',
        'title':'Post 102',
        'content':'I present to you my soul',
        'date':'july, 13 2024'
    }
]
# Create your views here.
def blog_home(request):
    b_context = {
        'posts':posts
    }
    return render(request, 'blog_home.html', b_context)
