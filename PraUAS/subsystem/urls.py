from django.urls import path

from . import views

urlpatterns = [
    path('', views.DashboardView.as_view()),
    
    # Susu Hewani dan Telur
    path('sensor/sensor111', views.Sensor111.as_view()),
    path('sensor/sensor112', views.Sensor112.as_view()),
    path('sensor/sensor113', views.Sensor113.as_view()),
    path('actuator/actuator11', views.Actuator11.as_view()),
    
    # Daging Merah
    path('sensor/sensor121', views.Sensor121.as_view()),
    path('sensor/sensor122', views.Sensor122.as_view()),
    path('sensor/sensor123', views.Sensor123.as_view()),
    path('actuator/actuator12', views.Actuator12.as_view()),
    
    # Daging Putih
    path('sensor/sensor131', views.Sensor131.as_view()),
    path('sensor/sensor132', views.Sensor132.as_view()),
    path('sensor/sensor133', views.Sensor133.as_view()),
    path('actuator/actuator13', views.Actuator13.as_view()),
    
    # Beras, Gandum, Jagung
    path('sensor/sensor211', views.Sensor211.as_view()),
    path('sensor/sensor212', views.Sensor212.as_view()),
    path('sensor/sensor213', views.Sensor213.as_view()),
    path('actuator/actuator21', views.Actuator21.as_view()),
    
    # Sayuran
    path('sensor/sensor221', views.Sensor221.as_view()),
    path('sensor/sensor222', views.Sensor222.as_view()),
    path('sensor/sensor223', views.Sensor223.as_view()),
    path('actuator/actuator22', views.Actuator22.as_view()),
    
    # Buah-buahan
    path('sensor/sensor231', views.Sensor231.as_view()),
    path('sensor/sensor232', views.Sensor232.as_view()),
    path('sensor/sensor233', views.Sensor233.as_view()),
    path('actuator/actuator23', views.Actuator23.as_view()),
    
    # Deteksi Musim
    path('sensor/sensor311', views.Sensor311.as_view()),
    path('sensor/sensor312', views.Sensor312.as_view()),
    path('sensor/sensor313', views.Sensor313.as_view()),
    path('actuator/actuator31', views.Actuator31.as_view()),
    
    # Deteksi Hasil Penjualan Berfluktuasi
    path('sensor/sensor321', views.Sensor321.as_view()),
    path('sensor/sensor322', views.Sensor322.as_view()),
    path('sensor/sensor323', views.Sensor323.as_view()),
    path('actuator/actuator32', views.Actuator32.as_view()),
    
    # Deteksi Jumlah Pengunjung Restoran
    path('sensor/sensor331', views.Sensor331.as_view()),
    path('sensor/sensor332', views.Sensor332.as_view()),
    path('sensor/sensor333', views.Sensor333.as_view()),
    path('actuator/actuator33', views.Actuator33.as_view()),
    
    path('actuator/actuator1', views.Actuator1.as_view()),
    path('actuator/actuator2', views.Actuator2.as_view()),
    path('actuator/actuator3', views.Actuator3.as_view()),
    path('actuator/performance', views.PerformanceView.as_view()),
]