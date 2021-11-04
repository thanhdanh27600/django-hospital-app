from django.core.validators import RegexValidator

PHONE_REGEX = RegexValidator(
    regex=r'^(0?)(3[2-9]|5[6|8|9]|7[0|6-9]|8[0-6|8|9]|9[0-4|6-9])[0-9]{7}$', message="Invalid phone number (Vietnamese only)")

GENDER_CHOICES = [('MALE', 'Male'), ('FEMALE', 'Female'),
                  ('NOT PROVIDED', 'Not Provided')]

ROOM_TYPE_CHOICES = [('NORMAL', 'Normal room'),
                     ('EMERGENCY', 'Emergency room'),
                     ('RECUP.', 'Recuperation room')]

TEST_TYPE_CHOICES = [('PCR', 'PCR test'),
                     ('QUICK', 'Quick test'),
                     ('SPO2', 'SPO2 test'),
                     ('RESP.', 'Respiratory rate')]

PERSONNEL_TYPE_CHOICES = [('NURSE', 'Nurse'),
                          ('STAFF', 'Staff'),
                          ('DOCTOR', 'Doctor'),
                          ('HEAD', 'Head of camp')]
                          
PERSONNEL_GET_TYPE = {"NURSE": "NURSE",
                          "STAFF": "STAFF",
                          "DOCTOR": "DOCTOR",
                          "HEAD": "HEAD"}
