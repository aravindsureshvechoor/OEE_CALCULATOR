from django.urls import path
from .views import OEECalculationView,OEECalculationForSingleMachineView,OEEWithDateRangeView

urlpatterns = [
    path('oeecalculation/',OEECalculationView.as_view(),name='oee_calculation'),
    path('oeeforamachine/<int:machine_id>/',OEECalculationForSingleMachineView.as_view(),name='oee_for_a_machine'),
    path('oeewithdaterange/<int:machine_id>/',OEEWithDateRangeView.as_view(),name='oee_with_date_range')
]