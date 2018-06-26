from django.shortcuts import render
from django.core.serializers import serialize
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.http import JsonResponse
from django.contrib.auth.models import User

from .forms import RentalForm,LeafForm
from .models import Area,Rental,Post,Like,Leaf
from django.core.serializers import serialize
from django.http.response import JsonResponse


def home(request):

    if request.method== 'POST':
        leaf_form = LeafForm(request.POST)
        name = request.POST.get('name')
        c = request.POST.get('geom')
        coords = c.split(',',1)[1].split(":")[1][1:-2]
        event = Leaf(name=name,geom=coords)
        event.save()
        form = UserCreationForm(request.POST)
        # form.save()
    else:
        form = UserCreationForm()
        leaf_form = LeafForm()
    posts = Post.objects.all()
    leaf_form = LeafForm()

    return render(request, 'home.html', {'posts': posts, 'form':form,'leaf_form':leaf_form})

def validate_username(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken' : User.objects.filter(username__iexact=username).exists()
    }
    return JsonResponse(data)


def like_post(request):
    if request.method == 'GET':
        post_id = request.GET['post_id']
        likedpost = Post.objects.get(pk=post_id)
        m = Like(post=likedpost)
        m.save()
        return HttpResponse("Success!")
    else:
        return HttpResponse("Request method is not GET")



def rental_data(request):
    data = serialize('geojson', Rental.objects.all())
    return HttpResponse(data, content_type='json')

def data(request):
    events = Leaf.objects.all()
    d = []
    for event in events:
        
        y,x = event.geom.split(",")
        d.append(
        {
        "type": "FeatureCollection",
        "features": [{
        "type": "Feature",
        "properties": {'name': event.name},
        "geometry": {
        "type": "Point",
        "coordinates": [float(y),float(x)]
        }}]
        }
        )
    return JsonResponse(d,safe=False)
        
    
