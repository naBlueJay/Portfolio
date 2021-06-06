from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path('', RedirectView.as_view(url='/condense/')),
    # Not sure why views is underlinded in code editer...
    path('condense/', views.get_form, name = 'urlform'),
    # This redirects to the original URL the URL ID is set to
    path('<short_url>/', views.redirect_short_url, name = 'redirect_function'),
]
