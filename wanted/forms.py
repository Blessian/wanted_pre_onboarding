from django import forms
from wanted.models import Recruit


class RecruitForm(forms.ModelForm):
    class Meta:
        model = Recruit
        fields = ['company', 'recruit_position', 'reward', 'content', 'skills']
