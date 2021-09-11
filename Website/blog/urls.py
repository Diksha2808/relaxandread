# from django.urls import path
# from django.conf import settings

# from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('',views.home,name='home'),
    path('',views.index,name='index'),
    path('shop/',views.shop,name='shop'),
    # path('admin/', admin.site.urls),
    # path('',include('blog.urls')),
]
