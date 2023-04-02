from django.urls import path
from . import views
urlpatterns = [
    # home
    path('', views.index, name='index'),
    path('editadmin/', views.editadmin, name='editadmin'),
    
    # pages
    path('posts/', views.posts, name='posts'),
    path('store/', views.store, name='store'),
    path('about/', views.about, name='about'),
    
    # admin
    path('edithome/', views.edithome, name='edithome'),
    
    # store
    path('editstore/', views.editstore, name='editstore'),
    path('add-product/', views.addpro, name='addproduct'),
    path('editpro/<str:pk>/', views.editpro, name='editpro'),
    path('moreproduct/<str:pk>/', views.morepro, name='morepro'),
    path('delete-product/<str:pk>/', views.deletepro, name='deleteproduct'),
    
    # zapayn
    path('editzapayn/', views.zapayn, name='zapayn'),
    path('active/', views.active, name='active'),
    path('zapayn/', views.zapayn_main, name='zapayn-main'),
    
    # post
    path('addpostpage/', views.addpostpage, name='addpostpage'),
    path('deletepage/<str:pk>/', views.deletepage, name='deletepage'),
    path('editposts/', views.editposts, name='editposts'),
    path('posteditpage/<str:pk>/', views.posteditpage, name='posteditpage'),
    path('post/<str:pk>/', views.post, name='post'),
    
    # checkin
    path('checkin/', views.checkin, name='checkin'),
    path('checks/', views.checks, name='checks'),
    path('more-check/<str:pk>/', views.more_checks, name='more-checks'),
    path('delete-check/<str:pk>/', views.deletecheck, name='delete-check'),
    
    # edit checks
    path('editchecks/', views.editchecks, name='editchecks'),
    path('editcheck/<str:pk>/', views.editcheck, name='editcheck'),
    
    # offers
    path('offers/', views.offers, name='offers'),
    path('more-offer/<str:pk>/', views.more_offers, name='more-offer'),
    path('addoffer/', views.addoffer, name='addoffer'),
    path('delete-offer/<str:pk>/', views.delete_offer, name='delete-offer'),
    # edit offer
    path('editoffers/', views.editoffers, name='editoffers'),
    
    # karem only
    path('s-admin/', views.s_admin, name='s-admin'),
    path('s-zapayn/', views.s_zapayn, name='s-zapayn'),
]