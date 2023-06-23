from django.http import JsonResponse
from django.shortcuts import render,redirect
from .forms import CreateUserForm, LoginForm, CreateRecordForm, UpdateRecordForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .models import Person
from api.serializers import PersonSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .pagination import CustomPageNumberPagination
from django.contrib.auth.models import Group

from django.contrib import messages
from .filters import PersonFilter
from django.contrib.admin.views.decorators import user_passes_test
from .decorators import authenticated_user,allowed_users


# Home page
@authenticated_user
def home(request):
    return render(request, 'person_app/index.html')


# Dashboard
# @user_passes_test(lambda u: u.is_superuser, login_url='user-login')
@login_required(login_url='user-login')
@allowed_users(allowed_roles=['admin'])
def dashboard(request):
    person_records = Person.objects.all()
    myFilter = PersonFilter()
    # paginator = CustomPageNumberPagination
    # paginated_records = paginator.paginate_queryset(request, person_records)

    context = {'records': person_records,
               'filtersform': myFilter.form,}

    return render(request, 'person_app/dashboard.html', context=context)

@login_required(login_url='user-login')
# Filter Record
def filter_records(request):
    person_records = Person.objects.all()
    # print(*request.GET.values())
    myFilter = PersonFilter(request.GET, queryset=person_records)
    if any(myFilter.data.values()):
        filtered_qs = myFilter.qs
    else:
        filtered_qs = Person.objects.none()
    if len(filtered_qs)==0 and any(request.GET.values()):
        messages.error(request, "Please enter a vaild record to search")
    context = {
        'filtersform':myFilter.form,
        'querysets':filtered_qs,
    }

    return render(request, 'person_app/dashboard.html', context=context)


# User logout
def user_logout(request):
    
    auth.logout(request)
    messages.success(request, "Logout success!")
    
    return redirect("user-login")


# User login
@authenticated_user
def user_login(request):

    form = LoginForm()

    if request.method == "POST":

        form = LoginForm(request, data=request.POST)

        if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None :

                auth.login(request, user)
                messages.success(request,"User logged in successfully")
            
            if user.is_superuser:
                return redirect("dashboard")
            else:
                return redirect("filter-records")

    context = {'form':form}

    return render(request, 'person_app/user-login.html', context=context)

# Register user
@authenticated_user
def register(request):
    form = CreateUserForm(request.POST or None)

    if request.method == "POST":

        # form = CreateUserForm(request.POST)

        if form.is_valid():

            user = form.save()
            # By default all users are assigned with "guest" role, to change this
            # access admin panel
            group = Group.objects.get(name="guest")
            user.groups.add(group)
            messages.success(request, "Account created successfully!")

            return redirect("user-login")

    context = {'form':form}

    return render(request, 'person_app/register.html', context=context)

    
@login_required(login_url='user-login')
@allowed_users(allowed_roles=['admin'])
@api_view(['GET','POST'])
def create_record(request):
    form = CreateRecordForm()
    if request.method == 'POST':
        form = CreateRecordForm(request.POST)
        if form.is_valid():
            serializer = PersonSerializer(data=form.cleaned_data)
            if serializer.is_valid():
                serializer.save()
                serialized_data = serializer.data
                return render(request, 'person_app/create-record-details.html', {'serialized_data': serialized_data})

    context = {'form':form}
    return render(request, 'person_app/create-record.html',context=context)

# - Read / View a singular record

@login_required(login_url='my-login')
@allowed_users(allowed_roles=['admin'])
@api_view(['GET'])
def singular_record(request, pk):

    person_record = Person.objects.get(id=pk)

    context = {'record':person_record}

    return render(request, 'person_app/view-record.html', context=context)

@login_required(login_url='user-login')
@allowed_users(allowed_roles=['admin'])
@api_view(['GET','POST'])
def update_record(request, pk):
 
    try:
        person_obj = Person.objects.get(pk=pk)
    except Person.DoesNotExist:
        persons_list = Person.objects.all()
        return render(request, 'person_app/dashboard.html', {'records':persons_list,'status_code': status.HTTP_404_NOT_FOUND})
    
    form = UpdateRecordForm(instance=person_obj)
    print("method is ",request.method)
        
    if request.method == 'POST':
        serializer = PersonSerializer(person_obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            # serialized_data = serializer.data
            # return render(request, 'person_app/view-record.html')
            messages.success(request,"Your record was updated successfully")
            return redirect('dashboard')
        
    context = {'form':form}
    return render(request, 'person_app/update-record.html', context=context)
            

@login_required(login_url='user-login')
@allowed_users(allowed_roles=['admin'])
@api_view(['GET','DELETE'])
def delete_record(request, pk):
    print("method is ",request.method)
    try:
        person_obj = Person.objects.get(pk=pk)
    except Person.DoesNotExist:
        persons_list = Person.objects.all()
        return render(request, 'person_app/dashboard.html', {'records':persons_list,'status_code': status.HTTP_404_NOT_FOUND})
    
    person_obj.delete()
    messages.success(request,"Your record was deleted successfully")
    return redirect('dashboard')


        
        

