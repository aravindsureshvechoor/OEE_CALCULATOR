from django.test import TestCase,Client
from django.urls import reverse
from OEEapp.models import Machine,Calculations,ProductionLog
from rest_framework.test import APIClient
from django.utils import timezone


class TestOEEViews(TestCase):

    def setUp(self):
        self.client    = Client()
        self.apiclient = APIClient()

        self.machine = Machine.objects.create(
            machine_name      = 'Test Machine',
            machine_serial_no = '001',
        )

        self.production_log   = ProductionLog.objects.create(
            cycle_number      = "CN001",
            unique_id         = "ABC123",
            material_name     = "Product A",
            machine           = self.machine,
            start_time        = timezone.now(),
            end_time          = timezone.now(),
            duration          = 8  
        )

        self.calculation = Calculations.objects.create(
            machine           = self.machine,
            production_log    = self.production_log,
            available_time    = 8,  
            unplanned_downtime= 0,  
            ideal_cycle_time  = 5, 
            good_product      = 96, 
            bad_product       = 0,  
        )


    # this test case checks if the OEECalculationView works as expected
    def test_oee_calculation_view(self):

        url         = reverse('oee_calculation')

        response    = self.client.get(url)

        self.assertEqual(response.status_code,200)



    # this test case checks if the OEECalculationView works as expected
    def test_oee_for_a_machine_view(self):

        machine_id = self.machine.id

        url        = reverse('oee_for_a_machine', kwargs={'machine_id':machine_id})

        response   = self.apiclient.get(url)

        self.assertEquals(response.status_code,200)

        oee_value = response.data.get('OEE')

        expected_oee = "100.0%"  

        self.assertEqual(oee_value, expected_oee)

    

    # this test case checks if the OEEWithDateRangeView works as expected
    def test_oee_with_date_range_view(self):

        start_date = '2022-01-01'

        end_date   = '2022-01-31'

        machine_id = self.machine.id

        url  = reverse('oee_with_date_range', kwargs={'machine_id': machine_id})
        url += f'?start_date={start_date}&end_date={end_date}'

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)





    

    

    
