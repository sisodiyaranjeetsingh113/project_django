from django.urls import path
from . import views
urlpatterns =   [
    path('',views.homeview,name='homeview'),
    path('add/',views.createview,name='createview'),
    path('<int:id>/',views.updateview,name='updateview'),
    path('delete/<int:id>/',views.deleteview,name='deleteview'),
    path('add1/',views.createviewfortask,name='add')

]

from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)