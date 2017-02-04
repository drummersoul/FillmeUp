from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.views.generic import View
from django.contrib import messages
from django.db.models import Q

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

#from user.models import UserProfile
from .models import Volunteer, Review, Report
from .forms import VolunteerForm, ReviewForm, ReportForm

# Create your views here.


class CreateView(View):

    def get(self, request):
        form = VolunteerForm(request.POST or None, request.FILES or None)

        context = {
            "form": form,
            "title": "Create Volunteer"
        }

        return render(request, "volunteer/create.html", context)

    def post(self, request):
        form = VolunteerForm(request.POST or None, request.FILES or None)

        if form.is_valid():
            volunteer = form.save(commit=False)

            if request.user.is_superuser or request.user.is_staff:
                volunteer.verification_status = 1
            else:
                volunteer.verification_status = 0

            volunteer.save()

            return HttpResponseRedirect(volunteer.get_absolute_url())
        else:
            print (form.errors)

        context = {
            "form": form,
            "title": "Create Volunteer"
        }

        return render(request, "volunteer/create.html", context)


class UpdateView(View):

    def get(self, request, slug=None):
        instance = get_object_or_404(Volunteer, slug=slug)
        form = VolunteerForm(request.POST or None,
                            request.FILES or None, instance=instance)

        context = {
            "form": form,
            "title": "Update Volunteer Details"
        }

        return render(request, "volunteer/update.html", context)

    def post(self, request, slug=None):
        instance = get_object_or_404(Volunteer, slug=slug)
        form = VolunteerForm(request.POST or None,
                            request.FILES or None, instance=instance)

        if form.is_valid():
            volunteer = form.save(commit=False)
            if request.user.is_superuser or request.user.is_staff:
                volunteer.verification_status = 1
            else:
                volunteer.verification_status = 0

            volunteer.save()

            return HttpResponseRedirect(volunteer.get_absolute_url())

        context = {
            "form": form,
            "title": "Update Volunteer Details"
        }

        return render(request, "volunteer/update.html", context)


class DetailView(View):

    def get(self, request, slug):
        volunteer = get_object_or_404(Volunteer, slug=slug)
        form = ReviewForm(request.POST or None)

        reviews = Review.objects.filter(volunteer=volunteer)

        context = {
            "volunteer": volunteer,
            "reviews": reviews,
            "form": form,
            "title": "Volunteer Details"
        }

        return render(request, "volunteer/detail.html", context)

    def post(self, request, slug):
        volunteer = get_object_or_404(Volunteer, slug=slug)
        user = get_object_or_404(UserProfile, user=request.user)
        print(user)
        form = ReviewForm(request.POST or None)

        if form.is_valid():
            review = form.save(commit=False)
            review.user = user
            review.volunteer = volunteer
            review.save()
            return HttpResponseRedirect(volunteer.get_absolute_url())

        context = {
            "volunteer": volunteer,
            "form": form,
            "title": "volunteer Details"
        }

        return render(request, "volunteer/detail.html", context)


class ListView(View):

    def get(self, request):
        object_list = Volunteer.objects.all().order_by("name")
        query = request.GET.get("query")
        if query:
            object_list = object_list.filter(
                Q(name__icontains=query) |
                Q(address__icontains=query) |
                Q(website__icontains=query) |
                Q(registration_no__icontains=query) |
                Q(email__icontains=query)
            ).distinct()

        paginator = Paginator(object_list, 2)  # Show 25 contacts per page
        page_request_var = "page"
        page = request.GET.get(page_request_var)
        try:
            object = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            object = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of
            # results.
            object = paginator.page(paginator.num_pages)

        context = {
            "object_list": object,
            "page_request_var": page_request_var,
            "title": "List of Volunteers"
        }

        return render(request, "volunteer/list.html", context)


class DeleteView(View):

    def get(self, request, slug):
        instance = get_object_or_404(Volunteer, slug=slug)
        instance.delete()

        return redirect('home')


class BlockView(View):

    def get(self, request, slug):
        instance = get_object_or_404(Volunteer, slug=slug)
        instance.blocked = True
        instance.save()

        return redirect('home')


class ReportView(View):
    def get(self, request, slug):
        volunteer = get_object_or_404(Volunteer, slug=slug)
        user = get_object_or_404(UserProfile, user=request.user)
        form = ReportForm(request.POST or None)

        context = {
            "volunteer": volunteer,
            "user": user,
            "form": form,
            "title": "Report a Volunteer"
        }

        return render(request, "volunteer/report.html", context)

    def post(self, request, slug):
        volunteer = get_object_or_404(Volunteer, slug=slug)
        user = get_object_or_404(UserProfile, user=request.user)
        form = ReportForm(request.POST or None)

        if form.is_valid():
            report = form.save(commit=False)
            report.user = user
            report.volunteer = volunteer
            report.save()
            return HttpResponseRedirect(volunteer.get_absolute_url())

        context = {
            "volunteer": volunteer,
            "user": user,
            "form": form,
            "title": "Report a Volunteer"
        }

        return render(request, "volunteer/report.html", context)


class ReportDetailView(View):
    def get(self, request, id=None):
        report = get_object_or_404(Report, id=id)

        context = {
            "report": report,
            "title": "Report Detail"
        }

        return render(request, "volunteer/report_detail.html", context)


class ReportListView(View):
    def get(self, request):
        object_list = Report.objects.all()  # .order_by("-timestamp")

        paginator = Paginator(object_list, 1)  # Show 25 contacts per page
        page_request_var = "page"
        page = request.GET.get(page_request_var)
        try:
            object = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            object = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of
            # results.
            object = paginator.page(paginator.num_pages)

        context = {
            "object_list": object,
            "page_request_var": page_request_var,
            "title": "List of Reports"
        }

        return render(request, "volunteer/report_list.html", context)


class ReportDeleteView(View):

    def get(self, request, id):
        instance = get_object_or_404(Report, id=id)
        instance.delete()
        return redirect('home')


class ReportVerifyView(View):

    def get(self, request, id):
        instance = get_object_or_404(Report, id=id)
        instance.verification_status = 1
        instance.save()
        return redirect('home')
