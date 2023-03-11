from django import forms


class Product2CartForm(forms.Form):
    count = forms.IntegerField(min_value=1)
    #product_id = forms.IntegerField(min_value=1, show_hidden_initial=True)