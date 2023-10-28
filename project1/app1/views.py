from django.shortcuts import render
from .forms import EnquiryForm
from django.shortcuts import redirect
from .models import Enquiry


# Create your views here.

def enquiry_view(request):
    form = EnquiryForm()
    if request.method == 'POST':
        form = EnquiryForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('enquiry_url')
    template_name  = 'app1/enquiry.html'
    context = {'form':form}
    return render(request,template_name,context)

def display_view(request):
    data = Enquiry.objects.all()
    template_name = 'app1/show.html'
    context ={'data':data}
    return render(request,template_name,context)

def contact_view(request):
    template_name = 'app1/contact.html'
    context = {}
    return render(request,template_name,context)