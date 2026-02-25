from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
def loginView(request):
    form = AuthenticationForm(request)
    if request.method == "POST":
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            newUser = form.get_user()
            login(request,newUser)
            return redirect('/')
    return render(request,"accounts/login.html",{"form":form})
def logoutView(request):
    logout(request)
    return render(request,"accounts/logout.html",{})
def registerView(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        user_obj = form.save()
        return redirect("/login")
    context = {"form":form}
    return render(request,"accounts/register.html",context=context)
# Create your views here.
