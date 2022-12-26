from django.contrib import admin
from home import views
from django.urls import path

admin.site.site_header = 'Tazer Admin'
admin.site.index_title = 'Tazed Molestation'
admin.site.site_title = 'Bwahahaha Psyco'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name='home'),
    path('about',views.about, name='about'),
    path('tool',views.tool, name='weapons lmao'),
    path('gallery',views.gallery, name='14mar'),
    path('login',views.loginuser, name='login'),
    path('logout',views.logoutuser,name='Logout')
]
