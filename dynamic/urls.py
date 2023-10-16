from django.urls import path
from . import views as v



urlpatterns = [
    path('home',v.home,name='home'), # weird stuff happening because of chrome ( remember !!!)
    path('product/<id>',v.productpage,name='productpage'),
    path('delete/<id>',v.delete,name='dproduct'),
    path('contactus',v.contact,name='contact'),
    path('aboutus',v.aboutus,name='about'),
    path('search',v.search,name='search'),
    path('create',v.create,name='create'),
    path('edit/<id>',v.edit,name='edit'),
    path('category/<cat_name>',v.category,name='category'),
    
]






