from django.conf.urls import url
from django.conf.urls import (
    handler400, handler403, handler404, handler500
)
from bookform import views
from . import views
urlpatterns = [
    url(r'^ram/', views.index, name='index'),

]

