from django import forms

class LoanForm(forms.Form):

    applicant_income=forms.IntegerField()

    coapplicant_income=forms.IntegerField()

    loan_amount=forms.IntegerField()

    loan_term=forms.IntegerField()

    credit_history=forms.IntegerField()
