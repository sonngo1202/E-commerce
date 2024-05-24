"""shipment URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from shipment_service.views import CarriersView, ShipmentInfoView, ShipmentView, TransactionView, ShipmentInfoEditView, CarriersEditView, TransactionEditView, ShipmentInfoOfUserView, UpdateShipmentView, ShipmentOfOrderView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/ecomSys/shipment/shipment-info', ShipmentInfoView.as_view()),
    path('api/ecomSys/shipment/shipment-info/<int:id>', ShipmentInfoEditView.as_view()),
    path('api/ecomSys/shipment/shipment-info/<str:user_id>', ShipmentInfoOfUserView.as_view()),
    path('api/ecomSys/shipment/transaction', TransactionView.as_view()),
    path('api/ecomSys/shipment/transaction/<int:id>', TransactionEditView.as_view()),
    path('api/ecomSys/shipment/carrier', CarriersView.as_view()),
    path('api/ecomSys/shipment/carrier/<int:id>', CarriersEditView.as_view()),
    path('api/ecomSys/shipment/', ShipmentView.as_view()),
    path('api/ecomSys/shipment/<int:id>', UpdateShipmentView.as_view()),
    path('api/ecomSys/shipment/<int:order_id>', ShipmentOfOrderView.as_view()),
]
