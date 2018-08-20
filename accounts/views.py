from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.

def signup_view(request):
	#Request the post form
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		#Validate the Form and save
		if form.is_valid():
			form.save()
			# Login User and Redirect
			return redirect('create_products')
	else:		
		form = UserCreationForm()
	return render(request, 'accounts/signup.html', {'form': form})

def login_view(request):
	if request.method =='POST':
		#Authenticate the user input
		form = AuthenticationForm(data=request.POST)
		#Validate the form and Redirect
		if form.is_valid():

			return redirect('create_products')

	else:
		form = AuthenticationForm()
	return render(request, 'accounts/login.html', {'form': form })	
