
from django.http import HttpResponse
from .models import Listing,Rim,Manufacturer,Car
from django.http import Http404
from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView


def index(request):
    all_listings = Listing.objects.all()
    all_rim = Rim.objects.all()
    all_manufacturer = Manufacturer.objects.all()
    context = {
        'all_listings': all_listings,
        'all_rim':all_rim,
        'all_manufacturer':all_manufacturer
    }

    return render(request,'allposts/index.html',context)

def detail(request,listing_id):
    try: 
        listing = Listing.objects.get(pk=listing_id)
        rim = Rim.objects.get(pk=listing.get_rim_key())
        manufacturer = Manufacturer.objects.get(pk=rim.get_manufacturer_key())


    except Listing.DoesNotExist:
        raise Http404("Listing does not exist")
    return render(request,'allposts/detail.html',{'listing':listing, 'rim':rim,'manufacturer':manufacturer})

class PostCreate(CreateView):
    model = Listing
    fields = [
        'listing_id',
        'rim_model',
        'quantity',
        'price',
        'seller_name',
        'seller_phone',
        'image',
        'location',
        'condition'
        ]


class CarListView(ListView):
    template_name = 'allposts/searchcar.html'
    queryset = Car.objects.all()

def search(request):
    try:
        template_name = 'allposts/search.html'
        carmake = request.POST['carmake']
        caryear = request.POST['caryear']
        carmodel = request.POST['carmodel']
        selected_car = Car.objects.get(year=caryear,make=carmake,model=carmodel)

        matched_rim = Rim.objects.filter(bolt_pattern=selected_car.bolt_pattern)

        matchedListing = []

        for rim in matched_rim:
            rim_match_listing = Listing.objects.filter(rim_model=rim.rim_model)
            for matched_post in rim_match_listing:
                matchedListing.append(matched_post)
        context = {
            'selected_car': selected_car,
            'matchedListing': matchedListing
            }
    except Car.DoesNotExist:
        raise Http404("Car specified does not exist in database")

    return render(request,'allposts/search.html',context)


def filter(request):
    template_name = "allposts/filter_search.html"
    context = {}
    
    queryhit = Listing.objects.all()
    # rim = Rim.objects.filter(pk=listing.get_rim_key())
    try:
        rimmodel = request.POST['rim_model']
        queryhit = queryhit.filter(rim_model=rimmodel)
    except:
        print("rim model: None selected")

    try:
        bolt_pattern = request.POST['bolt_pattern']
        matched_rim = Rim.objects.filter(bolt_pattern=bolt_pattern)
        queryhit = queryhit.filter(rim_model__in=matched_rim)
    except:
        print("bolt pattern: None selected")

    

    try: 
        manufacturer = request.POST['manufacturer']
        matched_manufacturer = Manufacturer.objects.get(name=manufacturer)
        matched_rims_manufacturer = Rim.objects.filter(manufacturer=matched_manufacturer.name)
        queryhit = queryhit.filter(rim_model__in=matched_rims_manufacturer)
    except:
        print("manufacturer: none selected")
    
    
    seller_name = request.POST['Sellername'].strip()
    if seller_name == '':
        print("seller name left blank")
    else:
        queryhit = queryhit.filter(seller_name=seller_name)
    
    
    return render(request,'allposts/filter_search.html', {'queryhit' : queryhit})