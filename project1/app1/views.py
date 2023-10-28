from django.shortcuts import render
from .forms import EnquiryForm

# Create your views here.

def enquiry_view(request):
    form = EnquiryForm()
    template_name  = 'app1/enquiry.html'
    context = {'form':form}
    return render(request,template_name,context)