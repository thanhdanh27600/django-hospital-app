from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls.conf import re_path

from .views import *
# import routers
from rest_framework import routers


router = routers.DefaultRouter()

router.register(r'personnel', PersonnelView, basename='PersonnelView')
router.register(r'nurse', NurseView)
router.register(r'patient', PatientView)
router.register(r'doctor', DoctorView)
router.register(r'staff', StaffView)
router.register(r'head', HeadOfCampView)
router.register(r'volunteer', VolunteerView)
router.register(r'building', BuildingView)
router.register(r'room', RoomView)
router.register(r'patientcomo', PatientComobidityView)
router.register(r'medication', MedicationView)
router.register(r'symptom', SymptomView)
router.register(r'medication-effect', MedicationEffectView)
router.register(r'receive-treatment', ReceiveTreatmentView)
router.register(r'test-information', TestInfomationView)
router.register(r'admitted', AdmittedView)

urlpatterns = [
    path('', include(router.urls)),
    path('patient-set/<int:id>', PatientSetView.as_view(), name="Patient view set"),
]

urlpatterns += staticfiles_urlpatterns()
