from django.shortcuts import render
from blogger.forms import UserForm
from django.contrib.auth.models import User 

from django.contrib.auth import authenticate , login, logout
from django.http import HttpResponseRedirect, HttpResponse,JsonResponse
from django.urls import reverse


from django.contrib.auth.decorators import login_required







# Create your views here.
def index(request):
    
    return render(request, 'blogger/index.html', {})






@login_required
def logout_user(request):
    logout(request)




def validate_username(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    return JsonResponse(data)



def registeration(request):
    user_form = UserForm()
    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        # profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
        else:
            print(user_form.error)
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
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('acount not active')
        else:
            print('some one tries to login in and failed !')
            print('USername: {} password{}'.format(username,password))
            return HttpResponse('Invalid Login Details!!')
    else:
        return render(request, 'blogger/login.html' , {})

