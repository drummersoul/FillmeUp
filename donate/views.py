from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse, HttpResponseRedirect,Http404
from .models import Donate
from .forms import DonateForm
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from urllib import quote_plus
from django.utils import timezone
from django.db.models import Q
from users.models import UserProfile
from users.forms import UserForm, UserProfileForm



def donate_create(request):
    if not request.user.is_active:
        if not request.user.is_staff or not request.user.is_superuser:
            raise Http404
    else:
        form = DonateForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            instance= form.save(commit = False)
            instance.user = request.user
            print form
            instance.save()
            messages.success(request, "Succesfully Created")
            return HttpResponseRedirect(instance.get_absoulute_url())
        else:
            print form.errors
        context = {
            "form" : form,

        }
        return render(request,"donate/donate_form.html",context)
#
def donate_list(request):
    if not request.user.is_active:
        if not request.user.is_staff or not request.user.is_superuser:
            raise Http404
    instance=Donate.objects.all()
    object_list = UserProfile.objects.all() #.order_by("-timestamp")
    paginator = Paginator(object_list, 5) # Show 25 contacts per page
    page_request_var = "page"
    page = request.GET.get(page_request_var)
    try:
        object = paginator.page(page)
    except PageNotAnInteger:
    # If page is not an integer, deliver first page.
        object = paginator.page(1)
    except EmptyPage:
    # If page is out of range (e.g. 9999), deliver last page of results.
        object = paginator.page(paginator.num_pages)
    context = {
    	"object_list": object,
    	"page_request_var": page_request_var,
    	"title":"UserList",
        "instance_list":instance
    	}
    return render(request, "donate/donate_list.html", context)

def donate_detail(request,slug):
    instance = get_object_or_404(Donate, slug=slug)
    if not request.user.is_active:
        if not request.user.is_staff or not request.user.is_superuser:
            raise Http404
    context = {

    }
    return render(request,"donate/donate_detail.html",{})
    return HttpResponse("<h1>detail</h1>")

def donate_update(request,slug=None):
    if not request.user.is_staff or not request.user.is_superuser:
        return Http404
    instance = get_object_or_404(Donate, slug=slug)
    form = DonateForm(request.Donate or None,request.FILES or None, instance=instance)
    if form.is_valid():
        instance= form.save(commit = False)
        instance.save()
        messages.success(request, "<a href='#'> Item </a>Saved",extra_tags='html_safe')
        return HttpResponseRedirect(instance.get_absoulute_url())

    context = {
        "title": instance.title,
        "instance" : instance,
        "form" : form,
    }
    return render(request,"donate_form.html",context)



def donate_delete(request,slug=None):
    if request.user.is_staff or not request.user.is_superuser:
        return Http404
    instance = get_object_or_404(Donate, slug=slug)
    instance.delete()
    messages.success(request, "Succesfully Deleted")
    return redirect("donate:list")
def home(request,slug=None):

    return render(request,"home.html")
def about_us(request,slug=None):
    return render(request,"about_us.html",{})
# Create your views here.
