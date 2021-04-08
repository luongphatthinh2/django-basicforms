from django.shortcuts import render
from basicapp import forms

# Create your views here.


def index(request):
    return render(request, 'basicapp/index.html')


def form_name_view(request):
    form = forms.FormName()  # make a instance of FormName class
    if request.method == 'POST':
        form = forms.FormName(request.POST)  # request.POST contains data input
        # from user

        # if form.is_valid():
        #     print("VALIDATION SUCCESS !!")
        #     print ("NAME : " + form.cleaned_data['name'])
        #     print ("EMAIL : " + form.cleaned_data['email_email'])
        #     print ("VALID_TEXT : " + form.cleaned_data['text'])

    return render(request, 'basicapp/form_page.html', {'form': form})
