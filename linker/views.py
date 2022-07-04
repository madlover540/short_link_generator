from django.shortcuts import redirect, render
from linker.models import Genu
from linker.forms import My_Form
import uuid

# Create your views here.
def form_view (request):
    form = My_Form()
    update_form = Genu()
    code = str(uuid.uuid4())[:5]
    if request.method == 'POST':
        form = My_Form(request.POST)
        if form.is_valid():
            my_domain = 'http://127.0.0.1:8000'
            prefix = form.cleaned_data['link']
            updater = 'http://' + prefix
            context = my_domain+ '/' + code
            update_form = Genu(link = updater, uuid = code)
            update_form.save()
            return render (request,'linker/index.html', {'context': context , 'form':form } ) 


    return render (request, 'linker/index.html', {'form':form})


def go (request, pk):
    url_details = Genu.objects.get (uuid =pk)
    return redirect (url_details.link)