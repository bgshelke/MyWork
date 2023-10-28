from django import forms
from .models import Enquiry

clg = [('d.y. patil','d.y. patil'),('P.C.C.O.E','P.C.C.O.E'),('J.S.P.M','J.S.P.M'),('R.M.C','R.M.C'),('sinhgad','sinhgad'),('other','other')]

gen = [('M','Male'),('F','Female'),('O','Others')]
courses = [('Python','Python'),('Java','Java'),('C','C'),('C++','C++')]
batch = [('regular','regular'),('full-day','full-day')]
edu = [('B.E','B.E'),('Btech','Btech'),('B.com','B.com'),('Bsc','Bsc'),('Other','Other')]
branch = [('Electrical','Electrical'),('Mechanical','Mechanical'),('Electronics','Electronics'),('Civil','Civil'),('CS','CS'),('Other','Other')]
class EnquiryForm(forms.ModelForm):
    
    class Meta:
        model = Enquiry
        exclude = ['sno']

        labels = {
        'name' : 'Enter Name:',
        'mobile' : 'Enter Contact:',
        'education':'Select Education:',
        'stream' : 'Select Stream:',
        'college' : 'Select College:',
        'gender' : 'Select Gender',
        'pass_year' : 'Enter Passout Year',
        'course' : 'Select Course:',
        'b_type' : 'Select Batch Type:',
        'reff' : 'Enter Refference:',
        'remark' : 'Enter Remark if any:'
        }
        widgets={
                'mobile':forms.NumberInput(attrs={
                    'placeholder':'e.g.123456789'
                }),
                'college':forms.Select(choices=clg,attrs={
                    'class':'form-control'
                }),
                'gender' : forms.RadioSelect(choices=gen,attrs={
                    'class':'form-control'}),
                'pass_year' : forms.NumberInput(attrs={
                    'type':'year','placeholder':'YYYY'
                }),
                'b_type':forms.Select(choices=batch,attrs={
                    'class':'form-control'}),
                'course' : forms.Select(choices=courses,attrs={
                    'class':'form-control'}),
                'education' : forms.Select(choices=edu,attrs={
                    'class':'form-control'}),
                'stream':forms.Select(choices=branch,attrs={
                    'class':'form-control'})

        }

