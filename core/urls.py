
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('user_app.urls')),
    # path('api/', include('customer_care_app.urls')),
    path('api/', include('transaction_app.urls')),
    path('api/', include('payment_app.urls'))


]
