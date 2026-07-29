from django.db import models

class Prediction(models.Model):

    applicant_income=models.IntegerField()

    coapplicant_income=models.IntegerField()

    loan_amount=models.IntegerField()

    prediction=models.CharField(max_length=20)

    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return self.prediction
