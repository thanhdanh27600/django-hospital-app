from django.db import models
from django.utils import timezone
from .common import PERSONNEL_TYPE_CHOICES, PHONE_REGEX, GENDER_CHOICES, ROOM_TYPE_CHOICES, TEST_TYPE_CHOICES

# Create your models here.


class Personnel(models.Model):
    id = models.AutoField(primary_key=True, default=None)
    address = models.TextField(default=None)
    phone = models.CharField(
        validators=[PHONE_REGEX], max_length=12, default=None)
    gender = models.CharField(choices=GENDER_CHOICES,
                              max_length=12, default='NOT PROVIDED')
    first_name = models.CharField(max_length=25, default=None)
    last_name = models.CharField(max_length=25, default=None)
    date_of_birth = models.DateField(
        default=timezone.datetime(2000, 1, 1).date())
    type = models.CharField(
        choices=PERSONNEL_TYPE_CHOICES, default="STAFF",
        max_length=50, editable=False)
    personnel_id = models.CharField(
        max_length=50, editable=False, default=None, null=True)

    class Meta:
        abstract = True

    def __str__(self) -> str:
        return f'{self.personnel_id} - {self.first_name} {self.last_name}'


class Nurse(Personnel, models.Model):
    pass


class Staff(Personnel, models.Model):
    pass


class Doctor(Personnel, models.Model):
    pass


class HeadOfCamp(Personnel, models.Model):
    pass


class Volunteer(Personnel, models.Model):
    pass


class Patient(models.Model):
    number = models.AutoField(primary_key=True, default=None)
    patient_id = models.CharField(
        max_length=50, editable=False, default=None, null=True)
    full_name = models.CharField(max_length=50)
    phone = models.CharField(
        validators=[PHONE_REGEX], max_length=12)
    gender = models.CharField(choices=GENDER_CHOICES,
                              max_length=12, default='NOT PROVIDED')
    address = models.TextField()
    identify_number = models.IntegerField()
    nurse_id = models.ForeignKey(
        Nurse, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return f'{self.number} - {self.full_name}'


class PatientComobidity(models.Model):
    id = models.AutoField(primary_key=True, default=None)
    patient_number = models.ForeignKey(
        Patient, on_delete=models.CASCADE)
    comorbidity_name = models.CharField(max_length=50)


class Building(models.Model):
    id = models.AutoField(primary_key=True, default=None)
    building_name = models.CharField(max_length=50)
    number_of_floors = models.IntegerField(null=True, blank=True)

    def __str__(self) -> str:
        return self.building_name


class Room(models.Model):
    id = models.AutoField(primary_key=True, default=None)
    room_id = models.CharField(
        max_length=50, editable=False, default=None, null=True)
    floor = models.IntegerField(null=True, blank=True, default=0)
    maximum_capacity = models.IntegerField(null=True, blank=True, default=20)
    room_type = models.CharField(choices=ROOM_TYPE_CHOICES, max_length=50)
    building_name = models.ForeignKey(
        Building, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return self.room_id


class TestInfomation(models.Model):
    id = models.AutoField(primary_key=True, default=None)
    test_id = models.CharField(
        max_length=50, editable=False, default=None, null=True)
    value = models.CharField(max_length=10, null=True, blank=True)
    test_date = models.DateField(default=timezone.datetime(2000, 1, 1).date())
    positivity = models.BooleanField(null=True, blank=True)
    type = models.CharField(choices=TEST_TYPE_CHOICES, max_length=50)
    condition = models.TextField(null=True, blank=True)
    patient_number = models.ForeignKey(Patient, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.test_id}'


class Medication(models.Model):
    # code = models.CharField(primary_key=True, max_length=10) -> id
    name = models.TextField(default=None)
    price = models.FloatField(default=0.0)
    expiration_date = models.DateField(
        default=timezone.datetime(2000, 1, 1).date())

    def __str__(self) -> str:
        return f'{self.id} - {self.name}'


class MedicationEffect(models.Model):
    code = models.ForeignKey(
        Medication, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True, default=None)
    effect_name = models.CharField(max_length=50)


class ReceiveTreatment(models.Model):
    medication_code = models.ForeignKey(
        Medication, on_delete=models.CASCADE)
    patient_number = models.ForeignKey(
        Patient, on_delete=models.CASCADE)
    doctor_id = models.ForeignKey(
        Doctor, on_delete=models.CASCADE)
    start_date = models.DateField(default=timezone.datetime(2000, 1, 1).date())
    end_date = models.DateField(default=timezone.datetime(2000, 1, 1).date())
    result = models.TextField(default="Cured")
    treatment_period = models.IntegerField(
        editable=False, default=None, null=True)


class Symptom(models.Model):
    id = models.AutoField(primary_key=True, default=None)
    symptom_id = models.CharField(
        max_length=50, editable=False, default=None, null=True)
    start_date = models.DateField(default=timezone.datetime(2000, 1, 1).date())
    end_date = models.DateField(default=timezone.datetime(2000, 1, 1).date())
    symptom_name = models.CharField(max_length=50)
    patient_number = models.ForeignKey(
        Patient, on_delete=models.CASCADE, default=None)

    duration = models.IntegerField(editable=False, default=None, null=True)


class Admitted(models.Model):
    patient_number = models.ForeignKey(
        Patient, on_delete=models.CASCADE)
    test_id = models.ForeignKey(
        TestInfomation, on_delete=models.CASCADE)
    staff_id = models.ForeignKey(
        Staff, on_delete=models.CASCADE)
    admission_date = models.DateField(
        default=timezone.datetime(2000, 1, 1).date())
    location = models.TextField(null=True, blank=True)
    discharge_date = models.DateField(
        default=None, null=True, blank=True)


class History(models.Model):
    id = models.AutoField(primary_key=True, default=None)
    patient_number = models.ForeignKey(
        Patient, on_delete=models.CASCADE)
    room_id = models.ForeignKey(
        Room, on_delete=models.CASCADE)
    transfer_date = models.DateField(
        default=timezone.datetime(2000, 1, 1).date())
    destination_room = models.CharField(max_length=50, null=True, blank=True)
