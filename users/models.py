from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class User(AbstractUser):
    GENDERS = (
        ('m', 'Man'),
        ('w', 'Woman'),
        ('unknow', "I don't know")
    )
    gender = models.CharField('Sex', max_length=41,  choices=GENDERS, default='')
    image = models.ImageField(upload_to='users_images', null=True, blank=True)
    height = models.FloatField('height', default=0)
    weight = models.FloatField('weight', default=0)
    bmi = models.FloatField(null=True, blank=True)
    bmi_status = models.CharField(max_length=20, null=True, blank=True)
    bmi_history = models.JSONField(null=True, blank=True)
    weight_difference = models.CharField(max_length=100, null=True, blank=True)
    height_difference = models.CharField(max_length=100, null=True, blank=True)


    def calculate_bmi(self):
        if self.height and self.weight:

            # Формула для вычисления BMI: вес / (рост в метрах * рост в метрах)
            bmi_value = round(self.weight / ((self.height / 100)** 2),2)
            self.bmi = bmi_value
            # Определение статуса BMI
            if bmi_value < 18.5:
                self.bmi_status = 'Underweight'
            elif 18.5 <= bmi_value < 24.9:
                self.bmi_status = 'Normal'
            elif 25 <= bmi_value < 29.9:
                self.bmi_status = 'Overweight'
            else:
                self.bmi_status = 'Obese'

            if not self.bmi_history:
                self.bmi_history = [{'weight': self.weight,'height': self.height, 'bmi': self.bmi, 'date': timezone.now().strftime('%Y-%m-%d %H:%M:%S')}]
            else:
                last_entry_weight = self.bmi_history[-1]['weight']
                difference_weight = (f"compared to the previous result: " + f"you have gained weight by {(self.bmi_history[-1]['weight'] - self.weight) * -1}kg" if self.weight > float(last_entry_weight) else f"compared to the previous result: " + f"you've lost weight by {self.bmi_history[-1]['weight'] - self.weight}kg" if self.weight < last_entry_weight else f"same weight")
                self.weight_difference = difference_weight
                last_entry_height = self.bmi_history[-1]['height']
                difference_height = (f"compared to the previous result: " + f"you have grown up by {(self.bmi_history[-1]['height'] - self.height) * -1}cm" if self.height > float(last_entry_height) else f"compared to the previous result: " + f"you have become shorter by {self.bmi_history[-1]['height'] - self.height}cm" if self.height < last_entry_height else f"")
                self.height_difference = difference_height

                self.bmi_history.append({'height_difference': self.height_difference,'weight_difference': self.weight_difference, 'weight': self.weight, 'height': self.height,  'bmi': self.bmi, 'date': timezone.now().strftime('%Y-%m-%d %H:%M:%S')})
            return bmi_value
        return None

    def save(self, *args, **kwargs):
        self.bmi = self.calculate_bmi()
        super().save(*args, **kwargs)









