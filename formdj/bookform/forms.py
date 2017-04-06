from django.forms import ModelForm
from bookform.models import Book
from django.core.exceptions import NON_FIELD_ERRORS

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'authors']
