from .import views
from django.urls import path

urlpatterns=[
    path('',views.home,name='home'),
    path('login',views.login,name='login'),
    path('signup',views.signup,name='signup'),
    #admin page
    path('adminhome',views.adminhome,name='adminhome'),
    path('usercreate',views.usercreate,name='usercreate'),
    path('login_user',views.login_user,name='login_user'),
    path('addproduct',views.addproduct,name='addproduct'),
    path('products_add',views.products_add,name='products_add'),
    path('viewproduct',views.viewproduct,name='viewproduct'),
    path('cate',views.cate,name='cate'),
    path('addcate',views.addcate,name='addcate'),
    path('viewusers',views.viewusers,name='viewusers'),
    path('delete/<int:pk>',views.delete,name='delete'),
    path('deleteuser/<int:pk>',views.deleteuser,name='deleteuser'),
    path('userhome',views.userhome,name='userhome'),
    path('cart/<int:pk>/<int:k>/',views.cartitem,name='cartitem'),
    path('details/<int:pk>/<int:k>/',views.details,name='details'),
    path('viewcart/<int:pk>',views.viewcart,name='viewcart'),
    path('deletecart/<int:pk>',views.deletecart,name='deletecart'),
    path('profile/<int:pk>',views.myprofile,name='myprofile'),
    path('items',views.listcart,name='listcart'),
    path('deleteitem/<int:pk>',views.deleteitem,name='deleteitem'),
    path('editproduct/<int:pk>',views.editproduct,name='editproduct')
    
]