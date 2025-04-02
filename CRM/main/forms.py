from django import forms
from .models import CRM_model

class CreateTaskForm(forms.ModelForm):
    class Meta:
        model = CRM_model
        fields = '__all__'
        exclude = ['date', 'checkbox', 'complete_date']
        widgets = {
            'customer_name': forms.TextInput(
                attrs={
                    'type': 'text',
                    'class': 'form-control',
                    'aria-describedby': 'basic-addon1',
                    'id': 'customer_name'
                }
            ),
            'expiry_date': forms.DateInput(
                attrs={
                    'id': 'expiry_date'
                }
            ),
            'product_description': forms.Textarea(
                attrs={
                    'type': 'text',
                    'class': 'form-control',
                    'aria-describedby': 'basic-addon1',
                    'id': 'product_description'
            }),
            'price': forms.NumberInput(
                attrs={
                    'type': 'text',
                    'class': 'form-control',
                    'aria-label': 'Dollar amount (with dot and two decimal places)',
                    'id': 'price'
                }
            ),
            'contacts': forms.TextInput(
                attrs={
                    'type': 'text',
                    'class': 'form-control',
                    'aria-describedby': 'basic-addon1',
                    'id': 'contacts'
                }
            ),
            'quality': forms.Select(
                attrs={
                    'class': 'form-select',
                    'aria-label': 'Default select example'
                }
            ),
            'type': forms.TextInput(
                attrs={
                    'type': 'text',
                    'class': 'form-control',
                    'aria-describedby': 'basic-addon1',
                    'id': 'type'
                }
            )
        }

class EditTaskForm(forms.Form):
    QUALITY_CHOICES = [
        ('C', 'Normal'),
        ('B', 'Good'),
        ('A', 'Medium'),
        ('S', 'Premium'),
        ('SS', 'Elite'),
    ]

    customer_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'type': 'text',
                                                                                 'class': 'form-control',
                                                                                 'aria-describedby': 'basic-addon1',
                                                                                 'id': 'customer_name'}))
    expiry_date = forms.DateField(widget=forms.DateInput(attrs={
                    'id': 'expiry_date'
                }))
    product_description = forms.CharField(max_length= 250, widget=forms.Textarea(attrs={
                    'type': 'text',
                    'class': 'form-control',
                    'aria-describedby': 'basic-addon1',
                    'id': 'product_description'
            }))
    price = forms.DecimalField(decimal_places=2, max_digits=7, widget=forms.NumberInput(attrs={
                    'type': 'text',
                    'class': 'form-control',
                    'aria-label': 'Dollar amount (with dot and two decimal places)',
                    'id': 'price'
                }))
    contacts = forms.CharField(max_length=60, widget=forms.TextInput(attrs={
                    'type': 'text',
                    'class': 'form-control',
                    'aria-describedby': 'basic-addon1',
                    'id': 'contacts'
                }))
    quality = forms.ChoiceField(choices=QUALITY_CHOICES, widget=forms.Select(attrs={
                    'class': 'form-select',
                    'aria-label': 'Default select example'
                }))
    type = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'type': 'text',
                    'class': 'form-control',
                    'aria-describedby': 'basic-addon1',
                    'id': 'type'}))
