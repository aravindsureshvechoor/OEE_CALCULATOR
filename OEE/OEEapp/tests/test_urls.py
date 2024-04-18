from django.test import SimpleTestCase
from django.urls import reverse,resolve
from OEEapp.views import OEECalculationView,OEECalculationForSingleMachineView,OEEWithDateRangeView

class TestUrls(SimpleTestCase):

    # this functions tests if the URL's are correctly mapping to the recommended views

    def test_oee_calculation(self):
        url = reverse('oee_calculation')
        self.assertEquals(resolve(url).func.view_class, OEECalculationView)

    def test_oee_for_a_machine(self):
        url = reverse('oee_for_a_machine',kwargs={'machine_id':1})
        self.assertEquals(resolve(url).func.view_class, OEECalculationForSingleMachineView)

    def test_oee_with_date_range(self):
        url = reverse('oee_with_date_range',kwargs={'machine_id':1})
        self.assertEquals(resolve(url).func.view_class, OEEWithDateRangeView)