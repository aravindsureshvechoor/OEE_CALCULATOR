from django.db import models

# Create your models here.
class Machine(models.Model):
    machine_name      = models.CharField(max_length=100)
    machine_serial_no = models.CharField(max_length=50)
    time              = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.machine_name

class ProductionLog(models.Model):
    cycle_number   = models.CharField(max_length=10)
    unique_id      = models.CharField(max_length=50)
    material_name  = models.CharField(max_length=100)
    machine        = models.ForeignKey(Machine, on_delete=models.CASCADE)
    start_time     = models.DateTimeField()
    end_time       = models.DateTimeField()
    duration       = models.FloatField() 

    def __str__(self):
        return f"Production Log: {self.cycle_number} (Duration: {self.duration} hours)"

class Calculations(models.Model):
    
    machine            = models.ForeignKey(Machine, on_delete=models.CASCADE)
    production_log     = models.ForeignKey(ProductionLog, on_delete=models.CASCADE)
    available_time     = models.FloatField()
    unplanned_downtime = models.FloatField()
    ideal_cycle_time   = models.IntegerField()
    good_product       = models.IntegerField()
    bad_product        = models.IntegerField()

    def __str__(self):
        return f"{self.machine.machine_name}+{self.production_log.cycle_number}"

    



