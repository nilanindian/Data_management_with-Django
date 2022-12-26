from django.shortcuts import render,HttpResponse,redirect
from .models import myrecord
from .filters import myfilter
from django.core.paginator import Paginator, EmptyPage
from django.contrib.auth import authenticate, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm



def index(req):
    return render (req,"index.html")



def log(req):
    if req.method=='GET':
        form=AuthenticationForm()
        return render(req,"signin.html",{'form':form})
    elif req.method=='POST':
        form=AuthenticationForm(request=req,data=req.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            if user is not None:
                req.session['user']=username
                data=myrecord.objects.all()
                p=Paginator(data,10)
                p_no=req.GET.get('x',1)
                try :
                    page=p.page(p_no)
                except EmptyPage:
                    page=p.page(1)
                return render(req,"home.html",{"myrecord":page})
            elif user is None:
               # return HttpResponse("Invalid username")
                return render(req,"signin.html",{'form':form})
        else :
            return render(req,"index.html")

         

def reg(req):
    if req.method=="GET":
        uform=UserCreationForm()
        return render(req,"register.html",{'form':uform})
    elif req.method=='POST':
        uform=UserCreationForm(req.POST)
        if uform.is_valid():
            uform.save()
            return redirect("http://127.0.0.1:8000")
        else:
            return render(req,"register.html",{'form':uform})



def home(req):
    data=myrecord.objects.all()
    p=Paginator(data,6)
    p_no=req.GET.get('x',1)
    try :
        page=p.page(p_no)
    except EmptyPage:
        page=p.page(1)
    return render(req,"home.html",{"myrecord":page})



def insert(req):
    return render(req,"insert.html")



def update(req,ID):

    if req.method=="GET":
        data=myrecord.objects.get(id=ID)
        return render(req,"update.html",{"x":data})
    elif req.method=="POST":
        data=myrecord.objects.get(id=ID)
        data.name=req.POST['name']
        data.city=req.POST['city']
        data.email=req.POST['email']
        data.phone=req.POST['phone']
        data.save()
        #return redirect("home.html")
        return redirect("http://127.0.0.1:8000/home")

def save(req):
    data=myrecord()
    data.name=req.POST['name']
    data.city=req.POST['city']
    data.email=req.POST['email']
    data.phone=req.POST['phone']
    data.save()
    return redirect("http://127.0.0.1:8000/home")




def delete(req,ID):
    data=myrecord.objects.get(id=ID)
    data.delete()
    return redirect("http://127.0.0.1:8000/home")




def search(req):
    return render (req,"search.html")




def filter(req):
    orders = myrecord.objects.all()
    tablefilter = myfilter(req.GET, queryset=orders)
    orders = tablefilter.qs
    context = {'orders': orders, 'tablefilter': tablefilter}
    return render(req, 'search.html', context)




def logout(req):
      if req.session.get('user')!=None:
        try:
            del req.session['user'] 
            return render (req,"index.html")
        except:
            HttpResponse("you are already logged out")
      else:
          
            return render(req,"index.html")