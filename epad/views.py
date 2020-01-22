from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
@login_required(login_url = '/accounts/login/')
def home(request):
    '''
    View function to render thr home page
    '''
   
    user=request.User()
    return render(request,'home.html',)

@login_required(login_url = '/accounts/login/')
@permission_required("True","home")
def registered_users(request):
    users=User.objects.all()
    context={
        'users':users,
    }
    return render(request,'admin_site/users.html',context)


@login_required(login_url = '/accounts/login/')
@permission_required("True","home")
def user_deactivate(request,user_id):
    user=User.objects.get(id=user_id)
    user.is_active = False
    user.save()
    messages.success(request,f"{user.firstname}'s account has been deactivated'")
    return redirect('system_users')

@login_required(login_url = '/accounts/login/')
@permission_required("True","home")
def user_activate(request,user_id):
    user=User.objects.get(id=user_id):
    user.is_active=True
    user.save()
    messages.success(request,f"{user.firstname}'s account is now activated'")
    return redirect('system_users')


