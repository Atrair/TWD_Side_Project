from django.urls import path
from mammoth import views
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from .views import (search)

app_name = 'mammoth'

urlpatterns = [


    path('', views.index, name='index'),

    url(r'^$', search, name='searchposts'),

    path('gallery/pattern/<slug:pattern_title_slug>/', views.pattern, name='pattern'),

    # Registration
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('restricted/', views.restricted, name='restricted'),
    path('logout/', views.user_logout, name='logout'),
  
    #for comment url
    path('comment/',views.submit_comment,name='comment'),
    
    # Header
    path('forum/', views.forum, name='forum'),
    path('gallery/', views.gallery, name='gallery'),
    path('share_your_pattern/', views.share_your_pattern, name='share_your_pattern'),
    path('knit_kit/', views.knit_kit, name='knit_kit'),
    path('shop/', views.shop, name='shop'),
    path('search/', views.search, name='search'),
    
    # Footer
    path('terms_and_conditions/', views.terms_and_conditions, name='terms_and_conditions'),
    path('site_map/', views.site_map, name='site_map'),
    path('about_us/', views.about_us, name='about_us'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('faq/', views.faq, name='faq'),
    
]

if settings.DEBUG:
    urlpatterns= urlpatterns + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
    urlpatterns= urlpatterns + static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)
