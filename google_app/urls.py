
from django.conf.urls import url
from django.contrib import admin
from lawyers import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
url(r'^$', views.home, name='home'),
url(r'^like_post/$', views.like_post, name="like_post"),
url(r'^rental_data/$', views.rental_data),
url(r'^validate_username/$', views.validate_username),
url(r'^data/$', views.data),
url(r'^admin/', admin.site.urls),     
]
