from django import forms
from django.utils.translation import ugettext_lazy

# import models
from apps.core.models.tag import Tag


class TagForm(forms.ModelForm):

    class Meta:
        model = Tag
        labels = {
            'name': ugettext_lazy("tbl_title_name")
        }
        fields = ('name',)
