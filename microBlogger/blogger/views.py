from django.shortcuts import render
from blogger.forms import UserForm
from django.contrib.auth.models import User

from django.contrib.auth import authenticate , login, logout
from django.http import HttpResponseRedirect, HttpResponse,JsonResponse
from django.urls import reverse,reverse_lazy

from django.contrib.auth.decorators import login_required
from blogger.models import Blog,Comment

# Create your views here.
def index(request):
    return render(request, 'blogger/index.html', {})

@login_required
def logout_user(request):
    logout(request)

def validate_username(request):
    print ("this is validate user!!!!!!")
    username = request.GET.get('username', None)
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    return JsonResponse(data)

def comment(request):
    if request.user.is_authenticated :
        username = request.user.username
        user = User.objects.get(username=username)
        if request.method == 'GET':
            blog_id = request.GET['blog_id']
            comment_text = request.GET['comment_text']
            commentJson = {
                'comment_txt' : comment_text,
                'user' : username,
            }
            blog_obj = Blog.objects.get(pk=blog_id)
            
            if comment_text != '':
                print("DATA SUBMITTED!!")
                comment = Comment(username = user , blogtext = blog_obj , content = comment_text )
                comment.save()

    return JsonResponse(commentJson)

def registeration(request):
    user_form = UserForm()
    registered = False

    if request.method == "POST":
        print('checking for user validity????')
        user_form = UserForm(data=request.POST)
        # profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid():
            print(user_form)
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
            return HttpResponseRedirect(reverse_lazy('blogger:login'))
            
    return render( request, 'blogger/registeration.html', {
                                            'user_form' : user_form,
                                            'registered'    : registered,
                                            } )

def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse_lazy('blogger:display'))
            else:
                return HttpResponse('acount not active')
        else:
            print('some one tries to login in and failed !')
            print('USername: {} password{}'.format(username,password))
            return HttpResponse('Invalid Login Details!!')
    else:
        return render(request, 'blogger/login.html' , {})

def display_posts(request):
    blog_list = Blog.objects.order_by('-date_time')
    comment_list = Comment.objects.order_by('date_time')
    all_dict = { 'blogs' : blog_list, 'comments' : comment_list }
    return render(request,'blogger/display.html',context = all_dict)

def create_post(request):
    request.user
    
    if request.user.is_authenticated:
        username = request.user.username
        user = User.objects.get(username=username)
        first_name = user.first_name
        if request.method == 'POST' :
            content = request.POST.get('content')
            b = Blog.objects.create(username=user,content=content)
            b.save()
            return display_posts(request)
    else:
        print("ERROR USER IS NOT AUTHENTICATED!!")
    return render(request,'blogger/create.html',{'first_name' : first_name})
