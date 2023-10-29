from django import forms

from .models import Buy,new_user,Buy2


class BookingForm(forms.ModelForm):
    class Meta:
        model = Buy
        fields ='__all__'


        values={
            'name':'rice',
            'price':10,
            
                
        }

class new_use(forms.ModelForm):
    class Meta:
        model = new_user
        fields ='__all__'



class buyname(forms.ModelForm):
    class Meta:
        model = Buy2
        fields ='__all__'













