from django import forms

class CreateForm (forms.Form):
    Product_id = forms.IntegerField(
        label="Enter Product ID",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Product ID'
            }
        )
    )
    Product_name = forms.CharField(
        label="Enter Product Name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Product Name'
            }
        )
    )
    Price = forms.IntegerField(
        label="Enter Product Price",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Price'

            }
        )
    )
    Cname = forms.CharField(
        label="Enter Customer Name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Customer Name'
            }
        )
    )
    Mobile = forms.IntegerField(
        label="Enter Mobile Number",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Mobile Number'
            }
        )
    )


class UpdateForm (forms.Form):
    Product_id = forms.IntegerField(
        label="Enter Product ID",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Product Id'
            }
        )
    )
    Price= forms.IntegerField(
        label="Enter a new price",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'New Price'
            }
        )
    )


class DeleteForm (forms.Form):
    Product_id = forms.IntegerField(
        label="Enter Product ID",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Product Id'
            }
        )
    )
