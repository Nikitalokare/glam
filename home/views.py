from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from AdminApp.models import Category,Product_Category,products,Brand,payment
from home.models import UserInfo,Mycart,OrderMaster,fileupload
from .forms import MyFileForm
import os

# Create your views here.
def home(request):
    cat = Product_Category.objects.all()
    product = products.objects.all()
    brand = Brand.objects.all()
    return render(request,'home.html',{"brand":brand,"cats":cat,"product":product})

def showproduct(request,id):
    brand =  Brand.objects.all()
    cat = Product_Category.objects.all()
    product = products.objects.filter(category = id)
    return render(request,"showproduct.html",{"brand":brand,"cats":cat,"product":product})

def showbrandproduct(request,id):
    cat = Product_Category.objects.all()
    brand = Brand.objects.all()
    product = products.objects.filter(product_brand= id)
    return render(request,"showbrandproduct.html",{"brand":brand,"cats":cat,"product":product})

def viewproduct(request,id):
    brand =  Brand.objects.all()
    cat = Product_Category.objects.all()
    product = products.objects.get(id = id)
    return render(request,"viewproduct.html",{"brand":brand,"cats":cat,"product":product})

def viewbrandproduct(request,id):
    cat = Product_Category.objects.all()
    brand =  Brand.objects.all()
    product = products.objects.get(id = id)
    return render(request,"viewbrandproduct.html",{"brand":brand,"cats":cat,"product":product})

def SignUp(request):
    if(request.method == "GET"):
        return render(request,"SignUp.html",{})
    else:
        uname = request.POST["uname"]
        pwd = request.POST["pwd"]
        try:
            #Is user already present
            user = UserInfo.objects.get(username=uname)            
        except:
            #We can create user, as user is not present
            user = UserInfo(uname,pwd)
            user.save()
            return redirect(home)
        else:
            message = "This user already exist"
            return render(request,"SignUp.html",{"message":message})
        
def login(request):
    if(request.method == "GET"):
        return render(request,"login.html",{})
    else:
        uname = request.POST["username"]
        pwd = request.POST["password"]
        try:
            user = UserInfo.objects.get(username=uname,password = pwd) 
        except:
            message = "Please Enter correct username or password"
            return render(request,"login.html",{"message":message})
            
        else:
            request.session["username"] = uname
            return redirect(home)
        
def SignOut(request):
    request.session.clear()
    return redirect(home)

def addToCart(request):
    if("username" in request.session):
        user = UserInfo.objects.get(username = request.session["username"])
        prod_id = request.POST["pid"]
        product = products.objects.get(id=prod_id)
        qty = request.POST["qty"]
        shade = request.POST["test"]
        
        try:
            item = Mycart.objects.get(user=user,product=product)
        except:
            cart = Mycart()
            cart.user = user
            cart.product = product
            cart.qunt = qty
            cart.shade = shade
            request.session["shade"] = cart.shade
            cart.save()
            messages.info(request, 'Item added successfully')       
        else:
            messages.info(request, 'Item already in cart')
        return redirect(viewCart)
    else:
        return redirect(login)

def viewCart(request):
    if(request.method == "GET"):
        items = Mycart.objects.filter(user = request.session["username"])
        total = 0
        for t in items:
            total += t.product.product_price * t.qunt
        request.session["total"] = total
        return render(request,"viewCart.html",{"items":items})
    else:
        cart_id = request.POST["cart_id"]
        item = Mycart.objects.get(id=cart_id)
        action = request.POST["action"]
        if(action == "remove"):
            item.delete()
        else:
            qty = request.POST["qunt"]
            item.qunt = qty
            item.save()
        return redirect(viewCart)

def Aboutus(request):
    return render(request,"Aboutus.html",{})

def career(request):
    '''if(request.method == "GET"):
        return render(request,"career.html",{})
    else:
        file = request.POST["file"]
        file_upload = fileupload()
        file_upload.file = file
        file_upload.save()
    return redirect(home)'''
    if(request.method == "GET"):
        mydata=fileupload.objects.all()    
        myform=MyFileForm()
        if mydata!='':
            context={'form':myform,'mydata':mydata}
            return render(request,"career.html",context)
        else:
            context={'form':myform}
            return render(request,"career.html",context)
            
    else:
        myform=MyFileForm(request.POST,request.FILES)        
        if myform.is_valid():
            MyFile = request.FILES.get('file_name')

            exists=fileupload.objects.filter(file=MyFile).exists()

            if exists:
                messages.error(request,'The file %s is already exists...!!!'% MyFile)
            else:
                fileupload.objects.create(file=MyFile).save()
                messages.info(request,"File uploaded successfully.")
                return redirect(career)
def mamearth(request):
    brand = Brand.objects.all()
    product = products.objects.all()
    return render(request,"mamearth.html",{"brand":brand,"product":product})

def swissbeauty(request):
    brand = Brand.objects.all()
    product = products.objects.all()
    return render(request,"swissbeauty.html",{"brand":brand,"product":product})

def sugarcosmetics(request):
    brand = Brand.objects.all()
    product = products.objects.all()
    return render(request,"sugarcosmetics.html",{"brand":brand,"product":product})

def makepayment(request):
    if(request.method == "GET"):
        return render(request,"makepayment.html",{})
    else:
        card_no = request.POST["card_no"]
        cvv = request.POST["cvv"]
        expiry = request.POST["expiry"]
        try:
            buyer = payment.objects.get(card_no=card_no,cvv=cvv,expiry=expiry)
        except:
            messages.info(request,'Enter a Valid details')  
            return redirect(makepayment)
        else:
            owner = payment.objects.get(card_no='222',cvv='222',expiry='12/2026')
            buyer.balance -= float(request.session["total"])
            owner.balance += float(request.session["total"])
            buyer.save()
            owner.save()
            myorder = OrderMaster()
            user = UserInfo.objects.get(username=request.session["username"])
            myorder.user  = user
            myorder.amount = request.session["total"]
            myorder.shades = request.session["shade"]
            items = Mycart.objects.filter(user=user)
            details = ","
            for item in items:
                details+= item.product.product_name+" "
                item.delete()

            myorder.details= details
            myorder.save()  
            messages.info(request,'Payment Done Successfully')  
            return redirect(makepayment)
        
def search(request):
    search1 = request.POST["Search"]
    #print(search1)
    search_product = products.objects.filter(product_name__icontains = search1)
    #item = products.objects.all()
    '''for prods in product:
        if(prods.product_name == search1):
            search_product = search1'''
            
    cat = Product_Category.objects.all()
    product = products.objects.all()
    return render(request,'search.html', { "cats":cat,"product":product,'search_product' : search_product })
    
def myorder(request):
    if(request.method == "GET"):
        items = Mycart.objects.filter(user = request.session["username"])
        myorder = OrderMaster.objects.filter(user = request.session["username"])
    return render(request,'myorder.html', { "myorder":myorder,"items":items})

def ShippingAddress(request):
    if(request.method == "GET"):
        return render(request,"ShippingAddress.html",{})
    else:
        pass