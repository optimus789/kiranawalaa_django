from django import forms

TAX= [
    ('0.0', 'No tax'),
    ('8.0', "7 % gst"),
    ('12.0', '12 % gst'),
    ('18.0', '18 % gst'),
    ]

CAT = [
    ('fruit', 'Fruit'),
    ('beverage', "Beverage"),
    ('biscuit', 'Biscuits'),
    ('grains', 'Grains'),
    ('vegetables', 'Vegetables'),
]

UNITS = [
    ('kg', 'KiloGram(KG)'),
    ('lt', "Litre(LT)"),
    ('gm', 'Gram(gm)'),
    ('ml', 'MiliLitre(ml)'),
    ('Nos', 'Number of pieces')
]


class CreateItemForm(forms.Form):
    title = forms.CharField(max_length=100, required=True)
    desc = forms.CharField(max_length=2000)
    category = forms.CharField(
        label='Select type: ',
        widget=forms.RadioSelect(choices=CAT),
        required=True)
    cprice = forms.FloatField(label="Cost Price", required=True)
    sprice = forms.FloatField(label="Selling Price", required=True)
    mrp = forms.FloatField(label="Maximum Retail Price(MRP): ", required=True)
    tax = forms.FloatField(label='Tax', widget=forms.RadioSelect(choices=TAX), required=False)
    stock = forms.IntegerField(label="Stock", required=True)
    units = forms.ChoiceField(label="Unit", required=True ,choices=UNITS)