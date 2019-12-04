from django.conf.urls import url
from . import views
from django.contrib import admin

app_name = "allposts"

urlpatterns = [
    # /allposts/
    url(r'^$',views.index,name="index"),
    
    # /allposts/{listing_id}/
    url(r'^(?P<listing_id>[0-9]+)/$',views.detail,name='detail'),

    #/allposts/post/add/
    url(r'post/add/$',views.PostCreate.as_view(),name='listing-add'),
    
    #/allposts/searchcar/
    url(r'^searchcar/$',views.CarListView.as_view(),name='searchcar'),
    
    #allposts/searchcar/search/
    url(r'^searchcar/search/$',views.search,name="search"),

    #allposts/filter/
    url(r'^filter/$',views.filter,name="filter")
]
