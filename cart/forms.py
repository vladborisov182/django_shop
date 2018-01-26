from django import forms


class CartAddProductForm(forms.Form):
    PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]
    quantity = forms.TypedChoiceField(label='Количество', choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
