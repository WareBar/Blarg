from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout

# Create your views here.


def user_register(request):
	if request.method == "POST":
		form = UserCreationForm(request.POST)
		if form.is_valid():
			# form.save()
			login(request, form.save())
			return redirect("POST:list")
	else:
		form = UserCreationForm()



	return render(request, "USERS/user_register.html",{
		"form": form
		})



def user_login(request):


	if request.method == "POST":
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			login(request, form.get_user())
			return redirect('home')
	else:
		form = AuthenticationForm()

	return render(request, "USERS/user_login.html",{
		"form":form
		})

def user_logout(request):
	if request.method == "POST":
		logout(request)
		return redirect('home')


