from django.http import JsonResponse
import razorpay
from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, redirect
from empapp.models import productdb, salesdb, customerdb
from adminapp.models import employeedb,registerdb, imagedb, cartdb, orderdb, messagedb
# Create your views here.
def homepage(request):
    data = productdb.objects.all()
    emp = employeedb.objects.all()
    gal = imagedb.objects.all()
    pro = productdb.objects.all()

    # if request.session['Username'].exists():

    #     cart = cartdb.objects.filter(Username=request.session['Username'])
    #     rows = cart.count()
    #     totalprice = 0
    #     for i in cart:
    #         totalprice = totalprice + i.Totalprice
    # else:
    #     messages.warning(request, "Log In First....!")
    return render(request, "index.html", {'data':data, 'pro' :pro, 'emp':emp, 'gal':gal})

def userlogin(request):
    if request.method == "POST":
        uname = request.POST.get('username')
        pwd = request.POST.get('password')
        if registerdb.objects.filter(Username=uname, Password=pwd).exists():
            messages.success(request, "Log In Successfully....!")
            request.session['Username']=uname
            request.session['Password']=pwd
            return redirect(homepage)
        else:
            return redirect(registerlogin)
    return redirect(registerlogin)
def userlogout(request):
    del request.session['Username']
    del request.session['Password']
    return redirect(registerlogin)

def registerlogin(request):
    return render(request, "userlogin.html")
def registerpage(req):
    return render(req, "registration.html")
def saveregistration(req):
    if req.method == "POST":
        na = req.POST.get('username')
        em = req.POST.get('email')
        mob = req.POST.get('mobile')
        pas = req.POST.get('password')

        obj = registerdb(Username=na, email=em, mobile=mob, Password=pas)
        obj.save()
        messages.success(req, "Registered Successfully....!")
        return redirect(registerlogin)
def viewgal(req):
    gal = imagedb.objects.all()
    return render(req, "viewgallery.html", {'gal':gal})
def singleprod(req, pid):
    gal = imagedb.objects.all()

    products = productdb.objects.get(id=pid)
    return render(req, "singleproduct.html", {'products': products, 'gal':gal})

def addtocart(request):
    if request.method == "POST":
        na = request.POST.get('username')
        pr = request.POST.get('product')
        price = request.POST.get('price')
        ds = request.POST.get('desc')
        qty = request.POST.get('quantity')
        tp = request.POST.get('total')
        obj = cartdb(Username=na, Productname=pr, Price=price, Description=ds, Quantity=qty, Totalprice=tp)
        obj.save()
        messages.success(request, "Added To Cart Successfully....!")
        return redirect(homepage)
    else:
        messages.error(request, "Invalid request method.")
        return redirect('homepage')
def allproducts(req):
    pro = productdb.objects.all()
    return render(req, "products.html", {'pro': pro})
def viewcart(request):

    cart = cartdb.objects.filter(Username=request.session['Username'])
    totalprice = 0
    for i in cart:
        totalprice = totalprice+i.Totalprice

    client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
    payment = client.order.create({
        "amount": totalprice * 100,
        "currency": "INR",
        'payment_capture': 1,
    })
    print(payment)


    return render(request, "cart.html", {'cart':cart, 'totalprice':totalprice, 'payment':payment})



# Handle the callback or webhook request
def razorpay_callback(request):
    if request.method == "POST":
        # Parse the JSON response from Razorpay
        response_data = request.POST  # This may vary based on your integration method

        # Check the payment status
        payment_status = response_data.get("status")

        if payment_status == "captured":
            # Payment is successful
            # You can save order details to your database
            return JsonResponse({"status": "success"})
        else:
            # Payment has failed or is pending
            # Handle the failure and return an appropriate response
            return JsonResponse({"status": "failure"})
    else:
        # Handle invalid HTTP methods
        return JsonResponse({"status": "invalid method"})

def checkoutpage(request):

    cart = cartdb.objects.filter(Username=request.session['Username'])
    data = registerdb.objects.filter(Username=request.session['Username'])
    totalprice = 0
    for i in cart:
        totalprice = totalprice+i.Totalprice



    return render(request, "checkout.html", {'cart':cart, 'totalprice':totalprice, 'data':data})



def deletecart(request, dataid):
    data = cartdb.objects.filter(id=dataid)
    data.delete()
    return redirect(viewcart)
def success(request):
    cart = cartdb.objects.filter(Username=request.session['Username'])
    data = registerdb.objects.filter(Username=request.session['Username'])
    for j in data:
        em = j.email
        ph = j.mobile
    totalprice = 0
    for i in cart:
        totalprice = totalprice + i.Totalprice

    return render(request, "checkout.html", {'cart': cart, 'totalprice': totalprice, 'ph' : ph, 'em': em})


def placeorder(request):
    cart = cartdb.objects.filter(Username=request.session['Username'])
    if request.method == "POST":
        na = request.POST.get('name')
        adrs = request.POST.get('address')
        pin = request.POST.get('pin')
        mob = request.POST.get('phone')
        em = request.POST.get('email')
        for i in cart:
            obj1 = salesdb(Product=i.Productname, Price=i.Price, Quantity=i.Quantity, Total=i.Totalprice, Customer=i.Username)
            obj1.save()
        totalprice = 0
        for i in cart:
            totalprice = totalprice + i.Totalprice
        obj = orderdb(Name=na, Address=adrs, Pin=pin, Mobile=mob, Email=em, Product=obj1.Product, Quantity=obj1.Quantity, Totalprice=obj1.Price, Subtotal=totalprice)
        obj.save()
        if customerdb.objects.filter(Customer=na).exists():
            print()
        else:
            obj2 = customerdb(Customer=na, Place=adrs, Mobile=mob)
            obj2.save()
        messages.success(request, "Order Placed Successfully....!")
        cart.delete()

        return redirect(checkoutpage)
def aboutpage(req):
    gal = imagedb.objects.all()   
    return render(req, "aboutus.html", {'gal':gal})
def contactpage(request):
    gal = imagedb.objects.all()   
   
    return render(request, "contactus.html", {'gal':gal})
def sendmsg(request):
    if request.method == "POST":
        na = request.POST.get('name')
        sub = request.POST.get('subject')
        em = request.POST.get('email')
        mob = request.POST.get('mobile')
        msg = request.POST.get('message')
        obj = messagedb(Name=na, Subject=sub, Email=em, Mobile=mob, Message=msg)
        messages.success(request, "Message Send Successfully....!")
        obj.save()
        return redirect(contactpage)
def myorders(req):
    cs = req.session['Username']
    data = salesdb.objects.filter(Customer=cs)
    return render(req, "viewmyorder.html", {'cs':cs, 'data':data})


def product_list(request):
    query = request.GET.get('qq')
    if query:
        pro = productdb.objects.filter(Product__icontains=query)  # Adjust the field name accordingly
    else:
        pro = productdb.objects.all()
    
    
    return render(request, 'products.html', {'pro':pro})  # Replace 'your_template.html' with your actual template name



