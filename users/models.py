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
    height = models.FloatField('Height', default='0')
    weight = models.FloatField('Weight', default='0')
    bmi = models.FloatField(null=True, blank=True)
    bmi_status = models.CharField(max_length=20, null=True, blank=True)
    bmi_history = models.JSONField(null=True, blank=True)
    bmi_trend = models.CharField(max_length=50, null=True, blank=True)



    def calculate_bmi(self):
        if self.height and self.weight:

            # Формула для вычисления BMI: вес / (рост в метрах * рост в метрах)
            bmi_value = self.weight / ((self.height / 100)** 2)
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
                self.bmi_history = [{'bmi': bmi_value}]
            else:
                last_entry = self.bmi_history[-1]['bmi']
                trend = "your bmi has become closer to normal"\
                    if bmi_value > last_entry \
                    else "your bmi has become further from the norm"\
                    if bmi_value < last_entry \
                    else "your bmi hasn't changed"
                self.bmi_trend = trend
                self.bmi_history.append({'bmi': bmi_value, 'date': timezone.now().strftime('%Y-%m-%d %H:%M:%S')})

            return bmi_value
        return None

    def save(self, *args, **kwargs):
        self.bmi = self.calculate_bmi()
        super().save(*args, **kwargs)

