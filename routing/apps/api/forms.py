from django import forms
from django.core.validators import validate_email


class CSVImportForm(forms.Form):
    filename = forms.FileField(label='Select a CSV file to import:',)

    def clean(self):
        cleaned_data = super(CSVImportForm, self).clean()
    
        f = TextIOWrapper(request.FILES['filename'].file, encoding='ASCII')
        result_csvlist = csv.DictReader(f)
        # first line (only) contains additional information about the event
        # let's validate that against its form definition
        event_info = next(result_csvlist)
        f_eventinfo = ResultsForm(event_info)
        if not f_eventinfo.is_valid():
            raise forms.ValidationError("Error validating 1st line of data (after header) in CSV")
    
        return cleaned_data
