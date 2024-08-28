from django.shortcuts import render,redirect
from . models import *
# Create your views here.
def index(request):
    return render(request,"index.html")

def market(request):
    return render(request,"market.html")

def designer(request):
    return render(request,"design.html")


def logo(request):
    return render(request,"logo.html")

def marketing(request):
    return render(request,"marketing.html")

def logomaking(request):
    return render(request,"logomaking.html")

def worker(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        works=request.POST['works']
        perhour=request.POST['perhour']
        experience=request.POST['experience']
        usersave=Worker(name=name,email=email,phonenumber=phone,works=works,perhour=perhour,experience=experience)
        usersave.save()
        if works=='logo':
            return redirect('logo')
        elif works=='App':
            return redirect('designer')
        else:
            return redirect('marketing')
    return render(request,"worker.html")


def designer(request):
    if request.method=="POST":
        if 'file' in request.FILES:
            file = request.FILES['file']
            description = request.POST.get('description', '')
            designer = Designer(file=file, description=description)
            designer.save()
            return redirect("design")
        else:
            return render(request, "designer.html", {'error_message': "File is missing in the request."})
    return render(request, "designer.html")
        

def userlogin(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        Register.objects.get(email=email,password=password)
        return redirect("service")
    return render(request,"userlogin.html")

def designerlogin(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        Register.objects.get(email=email,password=password)
        return redirect("worker")    
    return render(request,"designerlogin.html")

def adminlogin(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        Register.objects.get(email=email,password=password)
        return redirect("adminview")    
    return render(request,"adminlogin.html")


def reg(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        role=request.POST.get("role")
        user=Register(name=name,email=email,password=password,role=role)
        user.save()
        if role=="user":
            return redirect('userlogin')
        elif role=="designer":
            return redirect('designerlogin')
        else :
            return redirect("adminlogin")

    return render(request,"registration.html")

def service(request):
    return render(request,"service2.html")

def design(request):
    return render(request,"design.html")

def adminview(request):
    reg=Register.objects.all()
    worker=Worker.objects.all()
    market=Marketing.objects.all()
    app=Logo.objects.all()
    logo=Logo.objects.all()

    return render(request,"adminview.html",{'reg':reg,'worker':worker,'market':market,'app':app,'logo':logo})