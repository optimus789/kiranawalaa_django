from django import forms
from .models import Item

TAX = [
    ("0.0", "No tax"),
    ("8.0", "8 % gst"),
    ("12.0", "12 % gst"),
    ("18.0", "18 % gst"),
]

CAT = [
    ("fruit", "Fruit"),
    ("beverage", "Beverage"),
    ("biscuit", "Biscuits"),
    ("grains", "Grains"),
    ("vegetables", "Vegetables"),
]

UNITS = [
    ("kg", "KiloGram(KG)"),
    ("lt", "Litre(LT)"),
    ("gm", "Gram(gm)"),
    ("ml", "MiliLitre(ml)"),
    ("Nos", "Number of pieces"),
]


class ItemCreateForm(forms.ModelForm):
    desc = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 3, "cols": 20}),
        max_length=1000,
        required=True,
    )
    """descr = forms.CharField( widget=forms.Textarea )
    desc = forms.CharField(max_length=2000)"""
    category = forms.ChoiceField(label="Select type: ", choices=CAT, required=True)
    """cprice = forms.FloatField(label="Cost Price", required=True)
    sprice = forms.FloatField(label="Selling Price", required=True)
    mrp = forms.FloatField(label="Maximum Retail Price(MRP): ", required=True)"""
    tax = forms.ChoiceField(label="Tax", choices=TAX, required=False)
    """stock = forms.IntegerField(label="Stock", required=True)"""
    units = forms.ChoiceField(label="Unit", required=True, choices=UNITS)

    class Meta:
        model = Item
        fields = [
            "title",
            "desc",
            "category",
            "image",
            "cprice",
            "sprice",
            "mrp",
            "tax",
            "stock",
            "units",
        ]


class ItemUpdateForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ["image"]

