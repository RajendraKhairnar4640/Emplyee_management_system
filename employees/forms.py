from django import forms
from .models import Employee, Attendance

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'required': True}),
            'mobile': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'department': forms.Select(attrs={'class': 'form-control', 'required': True}),
        }

class AttendanceForm(forms.ModelForm):

    class Meta:
        model = Attendance
        fields = '__all__'
        widgets = {
            'employee': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'date': forms.DateInput(attrs={'class': 'datepicker', 'id': 'date_input'}),
            
        }
        
    def __init__(self, *args, **kwargs):
        employees = kwargs.pop('employees', None)
        super(AttendanceForm, self).__init__(*args, **kwargs)
        if employees:
            self.fields['employee'].queryset = employees
        

