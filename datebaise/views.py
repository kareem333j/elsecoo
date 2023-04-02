from django.shortcuts import render
from .models import PostsAdd,Admin, Zapayn, ShopActivate,Product,Checkin,Offer
from datetime import datetime
from .forms import ProductForm
import os
import time
# from django.db.models import Q
# Create your views here.


# home page
def index(request):
    check_exsit = 0
    if len(Checkin.objects.all()) > 0:
        check_exsit = 1
    x = {
        'post':PostsAdd.objects.all(),
        'admin':Admin.objects.all(),
        'zapayn':Zapayn.objects.filter(name = "zapayn-now"),
        'active': ShopActivate.objects.filter(name = "activetion"),
        'product':Product.objects.all(),
        'checks':Checkin.objects.all(),
        'countchecks':Checkin.objects.all().count(),
        'exsit':check_exsit
    }
    return render(request, 'index.html', x)



# user pages
def posts(request):
    x = {
        'admin':Admin.objects.all(),
        'posts':PostsAdd.objects.all()
    }
    return render(request, 'pages/posts.html',x)

from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
# store
def store(request):
    search = str(request.POST.get('search'))
    productt = Product.objects.all()
    category = request.POST.get('category-search')

    # search proccess
    if Product.objects.filter(category = category):
        productt = Product.objects.filter(category = category)
    elif category == "الجميع":
        productt = Product.objects.all()
    else:
        if request.method == "POST":
            if len(search) > 0:
                if Product.objects.filter(name__contains = search):
                    productt = Product.objects.filter(name__contains = search)
                else:
                    productt = Product.objects.all()
        else:
            productt = Product.objects.all()

    c = {
        'product':productt,
        'cate':category,
        'search':search,
        'errorpro':Product.objects.all()
    }
    return render(request, 'pages/store.html',c)

@csrf_exempt
def addpro(request):
    saving_story = 'none'
    name = request.POST.get('name')
    price = request.POST.get('price')
    pieces = request.POST.get('pieces')
    category = request.POST.get('category')
    image = request.FILES.get('image')
    if request.method == "POST":
        s_pro = Product(name = name, price = price, pieces = pieces, category = category, image = image)
        if Product.objects.filter(name = name, price = price,category = category):
            print("product rebeated")
        else:
            if len(price) <= 4:
                s_pro.save()
                saving_story = 'yes'
            else:
                saving_story = 'no'
    return render(request, 'admin/addproduct.html',{'pro':ProductForm, 'savingstory':saving_story})

@csrf_exempt
def editstore(request):
    search = str(request.POST.get('search'))
    productt = Product.objects.all()
    category = request.POST.get('category-search')
    # search proccess
    if Product.objects.filter(category = category):
        productt = Product.objects.filter(category = category)
    elif category == "الجميع":
        productt = Product.objects.all()
    else:
        if request.method == "POST":
            if len(search) > 0:
                if Product.objects.filter(name__contains = search):
                    productt = Product.objects.filter(name__contains = search)
                else:
                    productt = Product.objects.all()
        
        else:
            productt = Product.objects.all()


    c = {
        'product':productt,
        'cate':category,
        'search':search,
        'errorpro':Product.objects.all()
    }
    return render(request, 'admin/editstore.html',c)

@csrf_exempt
def editpro(request, pk):
    prod = Product.objects.get(id = pk)
    if request.method == "POST":
        if len(request.FILES) != 0:
            if len(prod.image) > 0:
                os.remove(prod.image.path)
            prod.image = request.FILES.get('img')
            
        prod.name = request.POST.get('editname')
        if request.POST.get('editprice'):
            prod.price = request.POST.get('editprice')
        else:
            prod.price = 0
        prod.pieces = request.POST.get('editpieces')
        prod.category = request.POST.get('category')
        prod.save()
    return render(request, 'admin/goid/editproduct.html',{'date':ProductForm, 'pro':Product.objects.filter(id = pk)})

def deletepro(request, pk):
    prod = Product.objects.filter(id = pk)
    delete = request.GET.get('delete')
    if Product.objects.filter(id = delete):
        if request.method == "GET":
            prod.delete()
    b = {
        'pro':Product.objects.filter(id = pk)
    }
    return render(request, 'admin/goid/delete-product.html',b)

def morepro(request, pk):
    prod = Product.objects.filter(id = pk)
    x= {
        'prod':prod
    }
    return render(request, 'pages/more-product.html',x)





# admin pages
def edithome(request):
    return render(request, 'admin/edithome.html')

# about
def about(request):
    x = {
        'admin':Admin.objects.all()
    }
    return render(request, 'pages/about.html',x)

# edit admin page
@csrf_exempt
def editadmin(request):
    admin_info = Admin.objects.get(id=1)
    
    if request.method == "POST":
        if len(request.FILES) != 0:
            if len(admin_info.image) > 0 :
                os.remove(admin_info.image.path)
            admin_info.image = request.FILES.get('admin-photo')
        admin_info.name = request.POST.get('admin-name')
        admin_info.admin_bio = request.POST.get('admin-bio')
        admin_info.face_url = request.POST.get('facebook')
        admin_info.insta_url = request.POST.get('instagram')
        admin_info.tiktok_url = request.POST.get('tiktok')
        admin_info.phone_num = request.POST.get('phone')
        admin_info.save()
    x = {
        'admin':Admin.objects.filter(id =1),
    }
    return render(request, 'admin/editadmin.html',x)


# post
@csrf_exempt
def editposts(request):
    postdelete = request.POST.get('postdelete')
    search = request.POST.get('search-post')
    
    if request.method == "POST":
        if PostsAdd.objects.filter(post__contains = search):
            post = PostsAdd.objects.filter(post__contains = search)
        else:
            post = PostsAdd.objects.all()
    else:
            post = PostsAdd.objects.all()
    x = {
        'post':post,
        'admin':Admin.objects.all(),
        'search':search,
    }
    return render(request, 'admin/editposts.html',x)

@csrf_exempt
def posteditpage(request, pk):
    post = PostsAdd.objects.filter(id = pk)
    postcontent = request.POST.get('postcontent')
    # time = request.POST.get('time')
    if request.method == "POST":
        PostsAdd.objects.filter(id = pk).update(post = postcontent)
    else:
        print("Error -_-")
    x = {
        'post':post,
        'timenow':datetime.now,
    }
    return render(request, 'admin/goid/posteditpage.html',x)

@csrf_exempt
def addpostpage(request):
    saving_story = 'none'
    new_post = request.POST.get('newpost')
    img = request.FILES.get('img')
    if request.method == "POST":
        if PostsAdd.objects.filter(post = new_post):
            print("Error Post -_-")
        else:
            s_post = PostsAdd(post = new_post, image = img)
            s_post.save()
            saving_story = 'yes'
    else:
        print('Error -_-')
    return render(request, 'admin/addpostpage.html',{'savingstory':saving_story})

def deletepage(request ,pk):
    post = PostsAdd.objects.filter(id = pk)
    delete = request.GET.get('delete')
    if PostsAdd.objects.filter(id = delete):
        if request.method == "GET":
            post.delete()
    x = {
        'post':post,
    }
    return render(request, 'admin/goid/delete.html',x)

@csrf_exempt
def post(request, pk):
    post = PostsAdd.objects.filter(id = pk)
    post_v = PostsAdd.objects.get(id = pk)
    
    
    # functions visetors
    def get_ip(request):
        adress = request.META.get('HTTP_X_FORWARDED_FOR')
        if adress:
            ip = adress.split(',')[-1].strip()
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
    # ip = get_ip(request)
    
    
    post_v.post_views = post_v.post_views +1
    post_v.save()
    o = {
        'post':post,
        'admin':Admin.objects.all(),
    }
    return render(request, 'pages/post_id.html',o)




# zapayn
def zapayn_main(request):
    zapayn = request.POST.get('zapayn')
    
    if request.method == "POST":
        Zapayn.objects.filter(name = "zapayn-now").update(members = zapayn)
        
    x = {
        'zapayn':Zapayn.objects.filter(name = "zapayn-now"),
        'active': ShopActivate.objects.filter(name = "activetion"),
    }
    return render(request, 'pages/zapayn-main.html',x)

@csrf_exempt
def zapayn(request):
    zapayn = request.POST.get('zapayn')
    
    if request.method == "POST":
        Zapayn.objects.filter(name = "zapayn-now").update(members = zapayn)
        
    x = {
        'zapayn':Zapayn.objects.filter(name = "zapayn-now"),
    }
    return render(request, 'admin/zapayn.html',x)

@csrf_exempt
def active(request):
    active = request.POST.get('active')
    if request.method =='POST':
        ShopActivate.objects.filter(name = "activetion").update(active = active)
    else:
        print('Error -_-')
    return render(request, 'admin/active.html')

# check
@csrf_exempt
def checkin(request):
    checkphone = "non"
    name = request.POST.get('name')
    phone = request.POST.get('phone')
    if Checkin.objects.filter(name = name) and Checkin.objects.filter(phone_num = phone):
        print('repeated')
    else:
        s_date = Checkin(name = name, phone_num = phone)
        if request.method == "POST":
            if len(phone) == 11:
                checkphone = "yes"
                s_date.save()
                # return render(request, 'pages/checks-in.html')
            else:
                checkphone = "no"
    
    x={
        'checkphone':checkphone,
    }
    return render(request, 'pages/checkin.html',x)

def checks(request):
    checks = Checkin.objects.all()
    x = {
        'checkin':checks,
        'countchecks':Checkin.objects.all().count(),
    }
    return render(request, 'pages/checks-in.html',x)

@csrf_exempt
def more_checks(request,pk):
    check = Checkin.objects.get(id = pk)
    check.user_views = check.user_views + 1
    check.save()
    x = {
        'check':Checkin.objects.filter(id = pk)
    }
    
    return render(request, 'pages/more-checks.html',x)

# edit checks
@csrf_exempt
def editchecks(request):
    checks = Checkin.objects.all()
    search = request.POST.get('search-post')
    if request.method == "POST":
        if Checkin.objects.filter(name__contains = search):
            checks = Checkin.objects.filter(name__contains = search)
        elif Checkin.objects.filter(phone_num__contains = search):
            Checkin.objects.filter(phone_num__contains = search)
        else:
            Checkin.objects.all()
    x = {
        'checkin':checks
    }
    return render(request, 'admin/editchecks.html',x)


def editcheck(request,pk):
    checkedit = Checkin.objects.filter(id = pk)
    x = {
        'check':checkedit
    }
    return render(request, 'admin/editcheck.html',x)

def deletecheck(request,pk):
    check = Checkin.objects.filter(id = pk)
    delete = request.GET.get('delete')
    if Checkin.objects.filter(id = delete):
        if request.method == "GET":
            Checkin.objects.get(id = pk).delete()
    x={
        'check':check
    }
    return render(request, 'admin/goid/delete-check.html',x)

# offers
def offers(request):
    none = 'none'
    if len(Offer.objects.all()) == 0:
        none = 'yes'
    return render(request, 'pages/offers.html',{'offer':Offer.objects.all(),'nonee':none})

def more_offers(request,pk):
    offer = Offer.objects.filter(id = pk)
    x = {
        'admin':Admin.objects.all(),
        'offer':offer
    }
    return render(request, 'pages/more-offer.html',x)

def editoffers(request):
    return render(request, 'admin/editoffers.html',{'offer':Offer.objects.all()})

def delete_offer(request,pk):
    delete = request.GET.get('delete')
    if Offer.objects.filter(id = delete):
        if request.method == "GET":
            Offer.objects.get(id = pk).delete()
    x={
        'offer':Offer.objects.filter(id=pk)
    }
    return render(request, 'admin/goid/delete-offer.html',x)

@csrf_exempt
def addoffer(request):
    saving = 'none'
    title = request.POST.get('title')
    offer = request.POST.get('offer')
    range = request.POST.get('range')
    price = request.POST.get('price')
    if request.method == "POST":
        if Offer.objects.filter(title = title, offer = offer, price = price):
            saving = 'no'
        else:
            s_offer = Offer(title = title, price = price, range_continue = range,offer = offer)
            s_offer.save()
            saving = 'yes'
    x ={
        'save':saving
    }
    return render(request, 'admin/addoffer.html',x)

# karem only
@csrf_exempt
def s_admin(request):
    img_ad = request.FILES.get('image')
    if request.method == "POST":
        s_ad = Admin(image = img_ad)
        s_ad.save()
    return render(request, 'karem/start-admin.html',{'pro':ProductForm})

@csrf_exempt
def s_zapayn(request):
    activate = request.POST.get('activate')
    num_zapayn = request.POST.get('num-zapayn')
    
    if request.method == "POST":
        s_date = ShopActivate(active = activate)
        s_datee = Zapayn(members = num_zapayn)
        s_date.save()
        s_datee.save()
    return render(request, 'karem/start-zapayn.html')
