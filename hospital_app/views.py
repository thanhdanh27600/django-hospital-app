from random import randint
from django.http.response import JsonResponse
from rest_framework import generics, views, viewsets, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from hospital_app.models import *
from hospital_app.serializers import *

from django_filters.rest_framework import DjangoFilterBackend


class PatientSetView(generics.ListAPIView):

    def get(self, request, *arg, **kwarg):
        patient_id = kwarg.get("id", None)
        patient = Patient.objects.filter(number=patient_id)

        comors = PatientComobidity.objects.filter(
            patient_number=patient.get().number)
        symtomps = Symptom.objects.filter(
            patient_number=patient.get().number)
        tests = TestInfomation.objects.filter(
            patient_number=patient.get().number)
        treatments = ReceiveTreatment.objects.filter(
            patient_number=patient.get().number)
        
        result_patient = list(patient.values())[0]
        result_comors = list(comors.values())
        result_symtomps = list(symtomps.values())
        result_tests = list(tests.values())
        result_treatments = list(treatments.values())


        return JsonResponse({"data":
                             {
                                 "patient": result_patient,
                                 "comorbidities": result_comors,
                                 "symptoms": result_symtomps,
                                 "tests": result_tests,
                                 "treatments": result_treatments
                             }
                             }, safe=False, json_dumps_params={'ensure_ascii': False})


class PersonnelView(viewsets.ModelViewSet):
    serializer_class = PersonnelSerializer

    def get_queryset(self):
        nurse = Nurse.objects.all()
        doctor = Doctor.objects.all()
        staff = Staff.objects.all()
        head = HeadOfCamp.objects.all()
        return nurse.union(doctor, staff, head)


class PatientView(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['nurse_id', ]
    search_fields = ['identify_number', 'phone']
    ordering_fields = ['patient_id']


class NurseView(viewsets.ModelViewSet):
    queryset = Nurse.objects.all()
    serializer_class = NurseSerializer
    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter]
    filterset_fields = ['type', ]
    search_fields = ['personnel_id', 'phone']
    
class VolunteerView(viewsets.ModelViewSet):
    queryset = Volunteer.objects.all()
    serializer_class = VolunteerSerializer
    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter]
    filterset_fields = ['type', ]
    search_fields = ['personnel_id', 'phone']


class DoctorView(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter]
    filterset_fields = ['type', ]
    search_fields = ['personnel_id', 'phone']


class StaffView(viewsets.ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter]
    filterset_fields = ['type', ]
    search_fields = ['personnel_id', 'phone']


class HeadOfCampView(viewsets.ModelViewSet):
    queryset = HeadOfCamp.objects.all()
    serializer_class = HeadOfCampSerializer
    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter]
    filterset_fields = ['type', ]
    search_fields = ['personnel_id', 'phone']


class PatientComobidityView(viewsets.ModelViewSet):
    queryset = PatientComobidity.objects.all()
    serializer_class = PatientComobiditySerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['patient_number', ]
    search_fields = ['comorbidity_name', ]


class MedicationView(viewsets.ModelViewSet):
    queryset = Medication.objects.all()
    serializer_class = MedicationSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', ]
    ordering_fields = ['id', 'price']


class MedicationEffectView(viewsets.ModelViewSet):
    queryset = MedicationEffect.objects.all()
    serializer_class = MedicationEffectSerializer
    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['code', ]
    search_fields = ['effect_name', ]
    ordering_fields = ['id']


class ReceiveTreatmentView(viewsets.ModelViewSet):
    queryset = ReceiveTreatment.objects.all()
    serializer_class = ReceiveTreatmentSerializer
    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['patient_number', 'doctor_id', 'medication_code']
    search_fields = ['result', ]
    ordering_fields = ['start_date', 'end_date']


class AdmittedView(viewsets.ModelViewSet):
    queryset = Admitted.objects.all()
    serializer_class = AdmittedSerialzer
    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['patient_number', 'staff_id', 'test_id']
    search_fields = ['location', ]
    ordering_fields = ['admidssion_date']


class TestInfomationView(viewsets.ModelViewSet):
    serializer_class = TestInfomationSerializer
    queryset = TestInfomation.objects.all()
    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['patient_number', 'type']
    search_fields = ['value', 'condition', ]
    ordering_fields = ['test_date']


class SymptomView(viewsets.ModelViewSet):
    serializer_class = SymptomSerializer
    queryset = Symptom.objects.all()
    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['patient_number', ]
    search_fields = ['symptom_name', ]
    ordering_fields = ['start_date', 'end_date']


class BuildingView(viewsets.ModelViewSet):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['building_name']


class RoomView(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['building_name', 'room_type']
    ordering_fields = ['maximum_capacity', 'room_id']
