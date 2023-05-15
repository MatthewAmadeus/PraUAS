from django.db import models

class Sensor111(models.Model):
    value = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)

class Sensor112(models.Model):
    value = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)

class Sensor113(models.Model):
    value = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)

class Sensor121(models.Model):
    value = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)

class Sensor122(models.Model):
    value = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)
    
class Sensor123(models.Model):
    value = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)

class Sensor131(models.Model):
    value = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)

class Sensor132(models.Model):
    value = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)

class Sensor133(models.Model):
    value = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)
