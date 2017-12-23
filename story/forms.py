from django import forms
from .models import Story, Category

class StoryForm(forms.ModelForm):
    sb_thing = forms.CharField(widget=forms.TextInput(attrs={'class':'abc1 el-input__inner el-input__inner_m', 'placeholder': '字數上限30字'}))
    sb_story = forms.CharField(widget=forms.TextInput(attrs={'class':'abc2 el-input__inner el-input__inner_m', 'placeholder': '字數上限30字'}))
    sb_name = forms.CharField(widget=forms.TextInput(attrs={'class':'abc3 el-input__inner el-input__inner_s'}))

    #tags = forms.ModelMultipleChoiceField(
    #    to_field_name='slug',
    #    required=False,
    #    help_text=('Separate by comma to add more than once, or select from available tags'),
    #    queryset=Tag.objects.all(),
    #    widget=forms.SelectMultiple(attrs={
    #        'placeholder': ('Additional tags'),
    #        'class': 'el-select el-input__inner'
    #    })
    #)
    #tagsinput = forms.CharField(widget=forms.TextInput(attrs={'class':'el-dropdown-menu slot="dropdown"'}))
    #tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all())
    #tagsinput = forms.CharField(widget=forms.TextInput(attrs={'data-role':'tagsinput'}))

    def __init__(self, *args, **kwargs):
         super(StoryForm, self).__init__(*args, **kwargs)
         #self.fields['first_name'].widget.attrs.update({'autofocus': 'autofocus'})

         #remove labels for fields
         for field_name in self.fields:
            field = self.fields.get(field_name)
            #field.widget.attrs['placeholder'] = field.label
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
            'category',
            'adjective_t'
        )
    #def clean(self):
        # this condition only if the POST data is cleaned, right?
    #    cleaned_data = super(StoryForm, self).clean()
    #    print(cleaned_data.get('tags')) # return queryset of tags
