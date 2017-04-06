from django.shortcuts import render,render_to_response
from django.shortcuts import HttpResponse
from django.forms import modelformset_factory
from forms import BookForm
from bookform.models import Book
from django.template import RequestContext

# Create your views here.


def index(request):

    BookFormSet=modelformset_factory(Book,fields=('name','authors'),extra=10,can_delete=True)
    formset=BookFormSet()
    return render(request,'bookform\index.html',{'formset':formset})

def handler404(request):
    response = render(request,'404.html', {'status':400},
                                )
    response.status_code = 404
    print('I am getting called 404')
    return response
def handler500(request):
    response = render(request,'500.html', {'status':400},
                                  )
    print('I am getting called 500')
    response.status_code = 500
    return response
