from django import forms
from .models import Story

class StoryForm(forms.ModelForm):
    story = forms.CharField(widget = forms.TextInput(
        attrs = {
        'class': 'form-control',
        }
    ))

    def __init__(self, *args, **kwargs):
         super(StoryForm, self).__init__(*args, **kwargs)
         #self.fields['first_name'].widget.attrs.update({'autofocus': 'autofocus'})

         #remove labels for fields
         for field_name in self.fields:
            field = self.fields.get(field_name)
            field.widget.attrs['placeholder'] = field.label
            field.label =''

    class Meta:
        model = Story
        fields = (
            'sb_gender',
            'sb_adv',
            'sb_adj',
            'sb_about',
            'sb_thing',
            'who',
            'sth_adj',
            'sb_story',
            'itjcts',
            'sb_name',
            'mark',
        )
