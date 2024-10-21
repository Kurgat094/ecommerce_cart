from django.shortcuts import render,get_object_or_404,redirect
from .models import Product,CartItem
from .forms import CartAddProductForm
# Create your views here.


def product_list(request):
    products=Product.objects.all()
    return render(request,'product_list.html', {'products':products})

def product_detail(request,product_id):
    product = get_object_or_404(Product,id=product_id)
    form = CartAddProductForm()
    return render(request, 'product_details.html', {'product':product})


def add_to_cart(request,product_id):
    product=get_object_or_404(Product,id=product_id)
    form=CartAddProductForm(request.POST)
    if form.is_valid():
        cart_item=form.save(commit=False)
        cart_item.product=product
        cart_item.save()
        return redirect("cart_details")
        
def cart_detail(request):
    cart_items=CartItem.objects.all()
    total_price=sum (item.get_total_price() for item in cart_items)
    return render(request,"cart_details.html",{'cart_items':cart_items},{'total_price':total_price})