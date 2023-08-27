from microapp import views
from . import views
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name = 'Home'),
    path('aboutus/',views.aboutus,name = 'Aboutus'),
    path('contact/',views.contact,name = 'Contact'),
    path('services/',views.services,name = 'Services'),
    path('team/',views.team,name = 'Team'),
    path('login/',views.login_user,name = 'Login_user'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('contact-info/', views.contact_info, name='contact_info'),
    path('upload/', views.upload_file, name='upload_file'),
    path('delete/<int:file_id>/', views.delete_file, name='delete_file'),
    path('download/<int:file_id>/', views.download_file, name='download'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
