from django.shortcuts import render
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Machine,ProductionLog,Calculations
from datetime import datetime



# this api calculates the OEE of all machines and returns a dictionary
class OEECalculationView(APIView):

    def get(self,request):

        oee_data = {}

        machines = Machine.objects.all()

        for machine in machines:

            calculation                    = Calculations.objects.get(machine=machine)
            
            available_time                 = calculation.available_time*60

            unplanned_downtime             = calculation.unplanned_downtime*60

            available_operating_time       = available_time - unplanned_downtime

            total_products                 = calculation.good_product + calculation.bad_product

            ideal_cycle_time               = calculation.ideal_cycle_time

            actual_output                  = calculation.good_product + calculation.bad_product



            availability                  = (available_time-unplanned_downtime)/available_time * 100

            perfomance                    = ideal_cycle_time*actual_output/available_operating_time

            quality                       = calculation.good_product/total_products * 100

            oee                            = (availability * perfomance * quality)//100

            oee_data[machine.machine_name] = f"{oee}%"
        
        return Response(oee_data, status=status.HTTP_200_OK)




# this view calculates the OEE of a single machine with the given id
class OEECalculationForSingleMachineView(APIView):

    def get(self,request,machine_id):

        machine = Machine.objects.get(id=machine_id)

        calculation                    = Calculations.objects.get(machine=machine)
            
        available_time                 = calculation.available_time*60

        unplanned_downtime             = calculation.unplanned_downtime*60

        available_operating_time       = available_time - unplanned_downtime

        total_products                 = calculation.good_product + calculation.bad_product

        ideal_cycle_time               = calculation.ideal_cycle_time

        actual_output                  = calculation.good_product + calculation.bad_product



        availability                   = (available_time-unplanned_downtime)/available_time * 100

        perfomance                     = ideal_cycle_time*actual_output/available_operating_time

        quality                        = calculation.good_product/total_products * 100

        oee                            = (availability * perfomance * quality)//100

        
        return Response({'OEE':f"{oee}%"}, status=status.HTTP_200_OK)




# this view calculates the OEE of a given machine in a provided date range
class OEEWithDateRangeView(APIView):

    def get(self,request,machine_id):

        # here we are finding the difference between the number of days, since the OOE of a machine in a date-
        # range can be calculated by multiplying the difference in number of days with OEE of machine in 1 single day-
        # this is possible becaues, we have created 3 cycles of 8 hrs each covered by 3 different machines,
        # so 3 machines have one cycle each for one day

        start_date_str          = request.GET.get('start_date')
        end_date_str            = request.GET.get('end_date')

        # Parse the date strings into datetime objects
        start_date              = datetime.strptime(start_date_str, '%Y-%m-%d')
        end_date                = datetime.strptime(end_date_str, '%Y-%m-%d')

        # Calculate the time difference in seconds
        time_difference_seconds = (end_date - start_date).total_seconds()

        # Convert the time difference to days
        difference_in_days      = time_difference_seconds / 86400


        machine = Machine.objects.get(id = machine_id)

        calculation                    = Calculations.objects.get(machine=machine)
            
        available_time                 = calculation.available_time*60

        unplanned_downtime             = calculation.unplanned_downtime*60

        available_operating_time       = available_time - unplanned_downtime

        total_products                 = calculation.good_product + calculation.bad_product

        ideal_cycle_time               = calculation.ideal_cycle_time

        actual_output                  = calculation.good_product + calculation.bad_product



        availability                   = (available_time-unplanned_downtime)/available_time * 100

        perfomance                     = ideal_cycle_time*actual_output/available_operating_time

        quality                        = calculation.good_product/total_products * 100

        oee                            = (availability * perfomance * quality)//100

        oee_for_given_date_range       = difference_in_days*oee / difference_in_days

        return Response({'OEE':f"{oee_for_given_date_range}%"}, status=status.HTTP_200_OK)

