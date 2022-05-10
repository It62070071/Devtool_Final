from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.models import User
# Create your views here.
def hello(request):
    #Query Data From Model
    data = Post.objects.all()
    return render(request,'index.html',{'Posts': data})

# def page1(request):
#     return render(request, 'page1.html')

def createform(request):
    return render(request, 'Form.html')

def registerform(request):
    return render(request, 'registerForm.html')

# def addBlogs(request):
#     Title = request.POST['Title']
#     Description = request.POST['Description']
#     return render(request, 'addForm.html',{'Title': Title, 'Description': Description})

def registerBlogs(request):
    username = request.POST['username']
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    email = request.POST['email']
    password = request.POST['password']
    repassword = request.POST['repassword']

    user = User.objects.create_user(
        username = username,
        password = password,
        email = email,
        first_name = firstname,
        last_name = lastname
    )
    user.save()
    return render(request, 'registercomplete.html', {'complete': "REGISTER COMPLETE"})

# def createpost(request):
#     title = request.POST['Title']
#     desc = request.POST['Description']

#     post = Post.objects.all(
#         Title = title,
#         Desc = desc
#     )

#     post.save()
#     return render(request,'index.html',{'Posts': post})