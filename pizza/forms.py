from django.forms import ModelForm, ModelMultipleChoiceField, Textarea

from pizza.models import Pizza, Skladnik

class PizzaForm(ModelForm):
    skladniki = ModelMultipleChoiceField(queryset=Skladnik.objects.all())
    class Meta:
        model = Pizza
        exclude = ('data',)
        widgets = {
            'opis': Textarea(attrs={'cols': 80, 'rows': 3}),
        }


class SkladnikForm(ModelForm):
    class Meta:
        model = Skladnik
        fields = ('nazwa', 'jarski')