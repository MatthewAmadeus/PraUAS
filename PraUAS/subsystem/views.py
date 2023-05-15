from django.shortcuts import render
from django.views.generic import View
from django.conf import settings

from rest_framework.views import APIView
from rest_framework.response import Response

from machinelearning import mlmodel

from .models import Sensor, SensorLog, Actuator, ActuatorLog

class SensorTemplateView(APIView):
    sensor_name = ""
    graph_name = ""
    def get(self, request, format=None):
        sensor = Sensor.objects.get(name=self.sensor_name)
        raw_data = reversed(SensorLog.objects.filter(name__name__exact=self.sensor_name).order_by('-id')[:10])
        time_data = []
        log_data = []
        chart_label = self.graph_name
        for log in raw_data:
            time_data.append(log.time.strftime("%x %X"))
            log_data.append(log.value)
        data = {
            "value": sensor.value,
            "time_data": time_data,
            "chart_data": log_data,
            "chart_label": chart_label
        }
        return Response(data)

class ActuatorTemplateView(APIView):
    actuator_name = ""
    sensor1_name = ""
    sensor2_name = ""
    sensor3_name = ""
    model = ""
    graph_name = ""
    def get(self, request, format=None):
        actuator = Actuator.objects.get(name=self.actuator_name)
        sensor1 = Sensor.objects.get(name=self.sensor1_name)
        sensor2 = Sensor.objects.get(name=self.sensor2_name)
        sensor3 = Sensor.objects.get(name=self.sensor3_name)
        prediction = self.model.predict([float(sensor1.value), float(sensor2.value), float(sensor3.value)])
        actuator.state = int(prediction)
        actuator.save()
        actuator_log = ActuatorLog(name=actuator, state=actuator.state)
        actuator_log.save()
        
        raw_data = reversed(ActuatorLog.objects.filter(name__name__exact=self.actuator_name).order_by('-id')[:10])
        time_data = []
        log_data = []
        chart_label = self.graph_name
        for log in raw_data:
            time_data.append(log.time.strftime("%x %X"))
            log_data.append(log.state)
        data = {
            "state": actuator.state,
            "time_data": time_data,
            "chart_data": log_data,
            "chart_label": chart_label
        }
        return Response(data)

class ActuatorFromActuatorTemplateView(APIView):
    actuator_name = ""
    actuator1_name = ""
    actuator2_name = ""
    actuator3_name = ""
    model = ""
    graph_name = ""
    def get(self, request, format=None):
        actuator = Actuator.objects.get(name=self.actuator_name)
        actuator1 = Actuator.objects.get(name=self.actuator1_name)
        actuator2 = Actuator.objects.get(name=self.actuator2_name)
        actuator3 = Actuator.objects.get(name=self.actuator3_name)
        prediction = self.model.predict([float(actuator1.state), float(actuator2.state), float(actuator3.state)])
        actuator.state = int(prediction)
        actuator.save()
        actuator_log = ActuatorLog(name=actuator, state=actuator.state)
        actuator_log.save()
        
        raw_data = reversed(ActuatorLog.objects.filter(name__name__exact=self.actuator_name).order_by('-id')[:10])
        time_data = []
        log_data = []
        chart_label = self.graph_name
        for log in raw_data:
            time_data.append(log.time.strftime("%x %X"))
            log_data.append(log.state)
        data = {
            "state": actuator.state,
            "time_data": time_data,
            "chart_data": log_data,
            "chart_label": chart_label
        }
        return Response(data)

class DashboardView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'main.html')


# Susu Hewani dan Telur
class Sensor111(SensorTemplateView):
    sensor_name = "sensor111"
    
class Sensor112(SensorTemplateView):
    sensor_name = "sensor112"

class Sensor113(SensorTemplateView):
    sensor_name = "sensor113"
    
class Actuator11(ActuatorTemplateView):
    actuator_name = "actuator11"
    sensor1_name = "sensor111"
    sensor2_name = "sensor112"
    sensor3_name = "sensor113"
    model = mlmodel.actuator11_model

# Daging Merah
class Sensor121(SensorTemplateView):
    sensor_name = "sensor121"
    
class Sensor122(SensorTemplateView):
    sensor_name = "sensor122"

class Sensor123(SensorTemplateView):
    sensor_name = "sensor123w"

class Actuator12(ActuatorTemplateView):
    actuator_name = "actuator12"
    sensor1_name = "sensor121"
    sensor2_name = "sensor122"
    sensor3_name = "sensor123"
    model = mlmodel.actuator12_model
    
    
# Daging Putih
class Sensor131(SensorTemplateView):
    sensor_name = "sensor131"
    
class Sensor132(SensorTemplateView):
    sensor_name = "sensor132"

class Sensor133(SensorTemplateView):
    sensor_name = "sensor133"
    
class Actuator13(ActuatorTemplateView):
    actuator_name = "actuator13"
    sensor1_name = "sensor131"
    sensor2_name = "sensor132"
    sensor3_name = "sensor133"
    model = mlmodel.actuator13_model
 
    
# Beras, Gandum, Jagung
class Sensor211(SensorTemplateView):
    sensor_name = "sensor211"
    
class Sensor212(SensorTemplateView):
    sensor_name = "sensor212"

class Sensor213(SensorTemplateView):
    sensor_name = "sensor213"

class Actuator21(ActuatorTemplateView):
    actuator_name = "actuator21"
    sensor1_name = "sensor211"
    sensor2_name = "sensor212"
    sensor3_name = "sensor213"
    model = mlmodel.actuator21_model
    
 
# Sayuran
class Sensor221(SensorTemplateView):
    sensor_name = "sensor221"
    
class Sensor222(SensorTemplateView):
    sensor_name = "sensor222"

class Sensor223(SensorTemplateView):
    sensor_name = "sensor223"

class Actuator22(ActuatorTemplateView):
    actuator_name = "actuator22"
    sensor1_name = "sensor221"
    sensor2_name = "sensor222"
    sensor3_name = "sensor223"
    model = mlmodel.actuator22_model


# Buah-buahan
class Sensor231(SensorTemplateView):
    sensor_name = "sensor231"
    
class Sensor232(SensorTemplateView):
    sensor_name = "sensor232"

class Sensor233(SensorTemplateView):
    sensor_name = "sensor233"
    
class Actuator23(ActuatorTemplateView):
    actuator_name = "actuator23"
    sensor1_name = "sensor231"
    sensor2_name = "sensor232"
    sensor3_name = "sensor233"
    model = mlmodel.actuator23_model
    
    
# Deteksi Musim
class Sensor311(SensorTemplateView):
    sensor_name = "sensor311"
    
class Sensor312(SensorTemplateView):
    sensor_name = "sensor312"

class Sensor313(SensorTemplateView):
    sensor_name = "sensor313"

class Actuator31(ActuatorTemplateView):
    actuator_name = "actuator31"
    sensor1_name = "sensor311"
    sensor2_name = "sensor312"
    sensor3_name = "sensor313"
    model = mlmodel.actuator31_model
    
    
# Deteksi Hasil Penjualan Berfluktuasi
class Sensor321(SensorTemplateView):
    sensor_name = "sensor321"
    
class Sensor322(SensorTemplateView):
    sensor_name = "sensor322"

class Sensor323(SensorTemplateView):
    sensor_name = "sensor323"

class Actuator32(ActuatorTemplateView):
    actuator_name = "actuator32"
    sensor1_name = "sensor321"
    sensor2_name = "sensor322"
    sensor3_name = "sensor323"
    model = mlmodel.actuator32_model

    
# Deteksi Jumlah Pengunjung Restoran
class Sensor331(SensorTemplateView):
    sensor_name = "sensor331"
    
class Sensor332(SensorTemplateView):
    sensor_name = "sensor332"

class Sensor333(SensorTemplateView):
    sensor_name = "sensor333"
    
class Actuator33(ActuatorTemplateView):
    actuator_name = "actuator33"
    sensor1_name = "sensor331"
    sensor2_name = "sensor332"
    sensor3_name = "sensor333"
    model = mlmodel.actuator33_model
    
    
class Actuator1(ActuatorFromActuatorTemplateView):
    actuator_name = "actuator1"
    actuator1_name = "actuator11"
    actuator2_name = "actuator12"
    actuator3_name = "actuator13"
    model = mlmodel.actuator1_model
    
class Actuator2(ActuatorFromActuatorTemplateView):
    actuator_name = "actuator2"
    actuator1_name = "actuator21"
    actuator2_name = "actuator22"
    actuator3_name = "actuator23"
    model = mlmodel.actuator2_model
    
class Actuator3(ActuatorFromActuatorTemplateView):
    actuator_name = "actuator3"
    actuator1_name = "actuator31"
    actuator2_name = "actuator32"
    actuator3_name = "actuator33"
    model = mlmodel.actuator3_model
    
class PerformanceView(ActuatorFromActuatorTemplateView):
    actuator_name = "performance"
    actuator1_name = "actuator1"
    actuator2_name = "actuator2"
    actuator3_name = "actuator3"
    model = mlmodel.performance_model