from rest_framework import serializers
from hospital_app.common import PERSONNEL_GET_TYPE
from hospital_app.models import *


class PatientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

    def create(self, validated_data):
        patient = Patient.objects.create(**validated_data)
        patient.patient_id = 'PATIENT{:05d}'.format(patient.number)
        patient.save()
        return patient


class NurseSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Nurse
        fields = '__all__'

    def create(self, validated_data):
        nurse = Nurse.objects.create(**validated_data)
        nurse.type = PERSONNEL_GET_TYPE['NURSE']
        nurse.personnel_id = 'NURSE{:05d}'.format(nurse.id)
        nurse.save()
        return nurse


class HeadOfCampSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = HeadOfCamp
        fields = '__all__'

    def create(self, validated_data):
        head = HeadOfCamp.objects.create(**validated_data)
        head.type = PERSONNEL_GET_TYPE['HEAD']
        head.personnel_id = 'HEAD{:05d}'.format(head.id)
        head.save()
        return head


class VolunteerSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Volunteer
        fields = '__all__'

    def create(self, validated_data):
        vol = Volunteer.objects.create(**validated_data)
        vol.type = PERSONNEL_GET_TYPE['VOLUNTEER']
        vol.personnel_id = 'VOLUNTEER{:05d}'.format(vol.id)
        vol.save()
        return vol


class DoctorSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Doctor
        fields = '__all__'

    def create(self, validated_data):
        doctor = Doctor.objects.create(**validated_data)
        doctor.type = PERSONNEL_GET_TYPE['DOCTOR']
        doctor.personnel_id = 'DOCTOR{:05d}'.format(doctor.id)
        doctor.save()
        return doctor


class StaffSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Staff
        fields = '__all__'

    def create(self, validated_data):
        staff = Staff.objects.create(**validated_data)
        staff.type = PERSONNEL_GET_TYPE['STAFF']
        staff.personnel_id = 'STAFF{:05d}'.format(staff.id)
        staff.save()
        return staff


class PersonnelSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    personnel_id = serializers.CharField()
    type = serializers.CharField()
    url = serializers.CharField(default=None, read_only=True)


class PatientComobiditySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = PatientComobidity
        fields = '__all__'


class ReceiveTreatmentSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = ReceiveTreatment
        fields = '__all__'


class MedicationSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Medication
        fields = '__all__'


class MedicationEffectSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = MedicationEffect
        fields = '__all__'


class ReceiveTreatmentSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = ReceiveTreatment
        fields = '__all__'

    def create(self, validated_data):
        recv_treatment = ReceiveTreatment.objects.create(**validated_data)
        recv_treatment.treatment_period = (
            recv_treatment.end_date - recv_treatment.start_date).days
        recv_treatment.save()
        return recv_treatment


class TestInfomationSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = TestInfomation
        fields = '__all__'

    def create(self, validated_data):
        testInfo = TestInfomation.objects.create(**validated_data)
        testInfo.test_id = '{} - {}'.format(testInfo.type,
                                            str(testInfo.patient_number))
        testInfo.save()
        return testInfo


class SymptomSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Symptom
        fields = '__all__'

    def create(self, validated_data):
        symptom = Symptom.objects.create(**validated_data)
        symptom.symptom_id = 'SYMPTOM{:05d} - {}'.format(
            symptom.id, str(symptom.patient_number))
        symptom.duration = (symptom.end_date - symptom.start_date).days
        symptom.save()
        return symptom


class BuildingSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Building
        fields = '__all__'


class RoomSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Room
        fields = '__all__'

    def create(self, validated_data):
        room = Room.objects.create(**validated_data)
        room.room_id = '{}{:05d} - {}'.format(room.room_type,
                                              room.id, str(room.building_name))
        room.save()
        return room


class AdmittedSerialzer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Admitted
        fields = '__all__'
        
class HistorySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = History
        fields = '__all__'


class PatientRelatedSerializer(serializers.HyperlinkedModelSerializer):

    combor = PatientComobiditySerializer(many=True, read_only=True)

    class Meta:
        model = Patient
        fields = ['patient_id', 'full_name', 'phone',
                  'gender', 'address', 'identify_number', 'nurse_id', 'combor']
