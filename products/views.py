from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm


# Create your CRUD views here.
def list_products(request):
	products = Product.objects.all()
	return render(request, 'products.html', {'products': products})

#Request Form 
def create_product(request):
	form = ProductForm(request.POST or None)
	#Validate, save, Redicrect the Request form
	if form.is_valid():
		form.save()
		return redirect('list_products')

	return render(request, 'products-form.html', {'form': form})		
#Request Form
def update_product(request, id):
	product = Product.objects.get(id=id)
	form = ProductForm(request.POST or None, instance=product)
	#Validate,save,Redirect the Request Form
	if form.is_valid():
		form.save()
		return redirect('list_products')
	return render(request, 'products-form.html', {'form':form, 'product':product})
#Request Form
def delete_product(request, id):
	product = Product.objects.get(id=id)
	#Delete and Redirect the Request Form
	if request.method == 'POST':
		product.delete()
		return redirect('list_products')

	return render(request, 'prod-delete-confirm.html', {'product':product})			