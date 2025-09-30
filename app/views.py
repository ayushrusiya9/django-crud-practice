from django.shortcuts import render,redirect
from django.urls import reverse
from urllib.parse import urlencode
# from app.models import UploadForm
from django.db.models import Q
from app.models import *
# Create your views here.
def landing(request):
    return render(request,'ragister.html')

def open_form(request):
    if request.method == "POST":
        n = request.POST.get('name')
        e = request.POST.get('email')
        c = request.POST.get('contact')
        i = request.FILES.get('image')
        d = request.FILES.get('document')
        v = request.FILES.get('video')
        p = request.POST.get('password')
        cp = request.POST.get('cpassword')

        data = UploadForm.objects.filter(Email=e)
        print(data)
        if data:
            msg = "Email already exist!!!"
            return render(request, 'ragister.html',{'msg':msg,'open_form':'open_form','image':i,'name':n,'email':e,'contact':c,'password':p,'cpassword':cp})
        else:
            if p == cp:
                UploadForm.objects.create(Name=n,Email=e,Contact=c,Image=i,Documents=d,Video=v,Password=p)
                # msg = "Registration Successfull!!"
                url = reverse("login")
                data = urlencode({'msg1':'Registration Successfull!!'})
                # return render(request,'login.html',{'msg1':msg})
                return redirect(f'{url}?{data}')
            else:
                msg = "Incorrect Confirm Password!!!"
                return render(request,'ragister.html',{'msg2':msg,'open_form':'open_form','name':n,'email':e,'contact':c,'image':i,'password':p})
    return render(request,'ragister.html',{'open_form':'open_form'})

def login(request):
    if request.method == 'POST':
        e = request.POST.get('email')
        p = request.POST.get('password')

        # print("helloooo.....")
        user = UploadForm.objects.filter(Email=e).first()
        print(user)
        
        if user is not None:
            user_pass = user.Password
            if user_pass == p:
                print("Image path:", user.Image)
                print("Image URL:", user.Image.url)

                url = reverse('dashboard')
                # data = urlencode({'id':user.id})
                request.session['id'] = user.id
                # return render(request, 'dashboard.html', {'data':data})
                return redirect(f'{url}')
            else:
                msg = "Invalid Password!!"
                return render(request,'login.html',{'loginmsg':msg,'email':user.Email})
        else:
            alert = "User Not Found!!! Please Ragister"
            return render(request,'ragister.html',{"alert":alert,'open_form':'open_form'} )
    else:
        msg = request.GET.get('msg1')
        return render(request, 'login.html',{'msg1':msg})

def dashboard(request):
    user_id = request.session['id']
    print(user_id)
    int(user_id)
    # user_id = request.GET.get('id')
    user = UploadForm.objects.get(id=user_id)
    # print(user_id)
    data = {'id':user.id,'name':user.Name,'email':user.Email,'password':user.Password,'document':user.Documents,'image':user.Image}
    request.session['id'] = user.id
    return render(request, 'dashboard.html',{'data':data})
    
def query(request):
    user_id = request.session['id']
    # print(user_id)
    # user = UploadForm.objects.get(id=pk)
    user = UploadForm.objects.get(id=user_id)
    data = {'id':user.id,'name':user.Name,'email':user.Email,'password':user.Password,'document':user.Documents,'image':user.Image}
    if request.method == 'POST':
        n = request.POST.get('name')
        e = request.POST.get('email')
        q = request.POST.get('query')
        UserQuery.objects.create(Name=n,Email=e,Query=q)
        return render(request, 'dashboard.html',{'data':data})
    return render(request, 'dashboard.html', {'data':data, 'query':'query'})

def show_query(request):
    user_id = request.session['id']
    user = UploadForm.objects.get(id=user_id)
    e = user.Email
    data = {'id':user.id,'name':user.Name,'email':user.Email,'password':user.Password,'document':user.Documents,'image':user.Image}
    show_query = UserQuery.objects.filter(Email=e)
    # print(show_query.id)
    if show_query:
        # request.session['showquery_id']=show_query.id
        return render(request, 'dashboard.html', { 'show_query': show_query, 'data': data})
    else:
        msg = "Queries not found!!!"
        return render(request, 'dashboard.html', {'show_query': show_query, 'data': data,'msg':msg})
    
def search(request):
    if request.method == 'POST':
        sv = request.POST.get('search')
        user_id = request.session['id']
        user = UploadForm.objects.get(id=user_id)
        data = {'id':user.id,'name':user.Name,'email':user.Email,'password':user.Password,'document':user.Documents,'image':user.Image}
        # show_query = UserQuery.objects.filter(Name__icontains=sv)
        show_query = UserQuery.objects.filter(Q(Name__icontains=sv) | Q(Email__icontains=sv) | Q(Query__icontains=sv))
        return render(request,'dashboard.html',{'data': data,'show_query':show_query})
 
def update_query(request):
    user_id = request.session['id']
    # user = UploadForm.objects.get(id=pk)
    user = UploadForm.objects.get(id=user_id)
    e = user.Email
    olddata = UserQuery.objects.filter(Email=e).first()
    data = {'id':user.id,'name':user.Name,'email':user.Email,'password':user.Password,'document':user.Documents,'image':user.Image}
    if request.method == 'POST':
        n = request.POST.get('name')
        e = request.POST.get('email')
        q = request.POST.get('query')
        olddata.Query = q
        olddata.save()
        return render(request,'dashboard.html',{'data':data})
    return render(request,'dashboard.html',{'data':data,'olddata':olddata})

def Delete_query(request,pke):
    user_id =  request.session['id']
    user = UploadForm.objects.get(id=user_id)
    data = {'id':user.id,'name':user.Name,'email':user.Email,'password':user.Password,'document':user.Documents,'image':user.Image}
    olddata = UserQuery.objects.filter(id=pke)
    e = user.Email
    show_query = UserQuery.objects.filter(Email=e)
    olddata.delete()
    if olddata:
        return render(request,'dashboard.html',{'data':data})
    else:
        return render(request,'dashboard.html',{'data':data,'show_query':show_query})

def log_out(request):
    request.session.flush()
    return redirect('landing')
        