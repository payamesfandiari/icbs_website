
from django import forms

class SearchForm(forms.Form):
    query_n_id = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),label='شماره ملی',required=True,
                                 max_length=10,min_length=10,error_messages={'query_n_id':'کد ملی یک عدد ده رقمی است.'})

    def clean_query_n_id(self):
        query_n_id = self.cleaned_data['query_n_id']
        if not query_n_id.isdigit():
            raise forms.ValidationError('Mix of Numbers and digits is not allowed')
        return query_n_id
