from django.contrib import admin
from django.urls import path
from . import views, ajax_views


app_name = 'estudios'
urlpatterns = [

#  Home
      path('', views.Home.as_view(), name='home'),
            path('dashboard/', views.Dashboard.as_view(), name='dashboard'),
                  path('pos/', views.Pos.as_view(), name='pos'),

# Estudios
      path('estudios/<int:pk>', views.Estudios.as_view(), name='estudios'),
     
# Servcios
      path('service/', views.Service.as_view(), name='service'),
            path('service-create/', views.ServiceCreate.as_view(), name='service-create'),
                  path('service-detail/<int:pk>/', views.ServiceDetail.as_view(), name='service-detail'),
                        path('service-update/<int:pk>/', views.ServiceUpdate.as_view(), name='service-update'),
                  path('service-delete/<int:pk>/', views.ServiceDelete.as_view(), name='service-delete'),
            path('service-client-service/<int:pk>', views.ServiceClientSelect.as_view(), name='service-client-service'),

# Planes
      path('plan/', views.Plan.as_view(), name='plan'),
            path('plan-create/', views.PlanCreate.as_view(), name='plan-create'),
                  path('plan-detail/<int:pk>/', views.PlanDetail.as_view(), name='plan-detail'),
                        path('plan-update/<int:pk>/', views.PlanUpdate.as_view(), name='plan-update'),
                  path('plan-delete/<int:pk>/', views.PlanDelete.as_view(), name='plan-delete'),

# Ventas
      path('sale/', views.Sale.as_view(), name='sale'),
            path('sale-create/<int:pk>', views.SaleCreate.as_view(), name='sale-create'),
                  path('sale-reserver/<int:pk>', views.SaleReserver.as_view(), name='sale-reserver'),
                        path('sale-update/<int:pk>/', views.SaleUpdate.as_view(), name='sale-update'),
                  path('sale-create-date-choice/<int:pk>/', views.SaleCreateDateChoice.as_view(), name='sale-create-date-choice'),
            path('sale-client-date-choice/<int:pk>/', views.SaleClientDateChoice.as_view(), name='sale-client-date-choice'),
      path('fast-sale', views.FastSale.as_view(), name='fast-sale'),

# Gatos
      path('gastos-create', views.GastosCreate.as_view(), name='gastos-create'),

# Factura 
      path('factura/<int:pk>', views.Factura.as_view(), name='factura'),

# Galeria
      path('gallery/', views.Gallery.as_view(), name='gallery'),
            path('moment-create/', views.MomentCreate.as_view(), name='moment-create'),
                  path('moment-update/<int:pk>/', views.MomentUpdate.as_view(), name='moment-update'),

#  Caja 
      path('box/', views.Box.as_view(), name='box'),
            path('box-create/', views.BoxCreate.as_view(), name='box-create'),

# Aministracion
      path('admin', views.Admin.as_view(), name='admin'),
            path('empleados/', views.Empleados.as_view(), name='empleados'),
                  path('empleados-create/', views.EmpleadoCreate.as_view(), name='empleados-create'),
                        path('empleados-update/<int:pk>/', views.EmpleadoUpdate.as_view(), name='empleados-update'),
                  path('empleados-delete/<int:pk>/', views.EmpleadoDelete.as_view(), name='empleados-delete'),

# Perfil de usuario
      path('profile-client/<int:pk>/', views.ProfileClient.as_view(), name='profile-client'),

# Yes
      path('yes/', views.Yes.as_view(), name='yes'),

# Login
      path('login/', views.Login.as_view(), name='login'),
            path('logout/', views.Logout.as_view(), name='logout'),

#  Ajax
      path('ajax/verify-date-choice/', ajax_views.VerifyDateChoice, name='verify-date-choice'),
            path('ajax/search/', ajax_views.Search, name='search'),
                  path('ajax/get-estudios/', ajax_views.GetEstudios, name='get-estudios'),


#  Mhia
      path('mhia/', views.Mhia.as_view(), name='mhia'),

]


