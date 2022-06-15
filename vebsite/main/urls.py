from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path ('',views.index, name='home' ),
    path ('about', views.about, name='about'),
    path ('create', views.create, name='create'),
    path ('feedback', views.feedback, name='feedback'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
