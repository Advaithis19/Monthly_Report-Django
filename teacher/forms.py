from django import forms
from django.db.models import fields
from django.forms import widgets
from django.forms.widgets import PasswordInput, Select, SelectDateWidget, SelectMultiple, TextInput, NumberInput, Textarea
from django.core.exceptions import ValidationError
from django.http import request
from api.models import *

class GrantForm(forms.ModelForm):
    """def __init__(self, *args, **kwargs):
        user = kwargs.pop('user','')
        super(GrantForm, self).__init__(*args, **kwargs)
        self.fields['PI']=forms.ModelChoiceField(queryset=Profile.objects.all())
        self.fields['CO_PI']=forms.ModelChoiceField(queryset=Profile.objects.all())"""

    class Meta:
        model = Grants
        exclude = ['date_added']

        widgets = {
            'title': TextInput(attrs={
                'style': 'width: 100%;',
                'placeholder': 'Title'
                }),
            'agency' : TextInput(attrs={
                'style': 'width: 100%',
                'placeholder': 'Agency',
            }),
            'sanc_amt': NumberInput(attrs={
                'style': 'width: 100%;',
                'placeholder': 'Sanction Amount',
            }),
            'year': NumberInput(attrs={
                'style': 'width: 100%;',
                'placeholder': 'Year',
            }),
            'remarks': Textarea(attrs={
                'style': 'width: 100%;',
                'placeholder': 'Remarks',
                'rows' : 5
            }),
            'PI': Select(attrs={
                'style': 'width: 100%;',
                'placeholder': 'PI',
            }),
            'CO_PI': Select(attrs={
                'style': 'width: 100%;',
                'placeholder': 'Co PI',
            }),
        }


class EventForm(forms.ModelForm):
    """def __init__(self, *args, **kwargs):
        user = kwargs.pop('user','')
        super(GrantForm, self).__init__(*args, **kwargs)
        self.fields['PI']=forms.ModelChoiceField(queryset=Profile.objects.all())
        self.fields['CO_PI']=forms.ModelChoiceField(queryset=Profile.objects.all())"""

    class Meta:
        model = Event
        exclude = ['date_added']

        widgets = {
            'title': TextInput(attrs={
                'style': 'width: 100%;',
                'placeholder': 'Title'
                }),
            'venue' : TextInput(attrs={
                'style': 'width: 100%',
                'placeholder': 'Venue',
            }),
            'n_stud': NumberInput(attrs={
                'style': 'width: 100%;',
                'placeholder': 'No of students',
            }),
            'n_fac': NumberInput(attrs={
                'style': 'width: 100%;',
                'placeholder': 'No of faculty',
            }),
            'n_ind': NumberInput(attrs={
                'style': 'width: 100%;',
                'placeholder': 'No from industry',
            }),
            'date': SelectDateWidget(attrs={
                'style': 'width: 100%;',
                'placeholder': 'Date',
            }),
            'u_id': SelectMultiple(attrs={
                'style': 'width: 100%;',
                'placeholder': 'Faculty involved',
            }),
        }


class BookForm(forms.ModelForm):
    """def __init__(self, *args, **kwargs):
        user = kwargs.pop('user','')
        super(GrantForm, self).__init__(*args, **kwargs)
        self.fields['PI']=forms.ModelChoiceField(queryset=Profile.objects.all())
        self.fields['CO_PI']=forms.ModelChoiceField(queryset=Profile.objects.all())"""

    class Meta:
        model = Book
        exclude = ['date_added']

        widgets = {
            'n_isbn': NumberInput(attrs={
                'style': 'width: 100%;',
                'placeholder': 'ISBN #',
            }),
            'name': TextInput(attrs={
                'style': 'width: 100%;',
                'placeholder': 'Name of Book'
                }),
            'publisher' : TextInput(attrs={
                'style': 'width: 100%',
                'placeholder': 'Publisher',
            }),
            'u_id': SelectMultiple(attrs={
                'style': 'width: 100%;',
                'placeholder': 'Faculty involved',
            }),
        }


class WorkshopForm(forms.ModelForm):
    """def __init__(self, *args, **kwargs):
        user = kwargs.pop('user','')
        super(GrantForm, self).__init__(*args, **kwargs)
        self.fields['PI']=forms.ModelChoiceField(queryset=Profile.objects.all())
        self.fields['CO_PI']=forms.ModelChoiceField(queryset=Profile.objects.all())"""

    class Meta:
        model = Workshop
        exclude = ['date_added']

        widgets = {
            'event_name': TextInput(attrs={
                'style': 'width: 100%;',
                'placeholder': 'Name of the event'
                }),
            'venue' : TextInput(attrs={
                'style': 'width: 100%',
                'placeholder': 'Venue',
            }),
            'date': SelectDateWidget(attrs={
                'style': 'width: 100%;',
                'placeholder': 'Date of Event',
            }),
            
            'u_id': SelectMultiple(attrs={
                'style': 'width: 100%;',
                'placeholder': 'Faculty involved',
            }),
        }


class MouForm(forms.ModelForm):
    """def __init__(self, *args, **kwargs):
        user = kwargs.pop('user','')
        super(GrantForm, self).__init__(*args, **kwargs)
        self.fields['PI']=forms.ModelChoiceField(queryset=Profile.objects.all())
        self.fields['CO_PI']=forms.ModelChoiceField(queryset=Profile.objects.all())"""

    class Meta:
        model = MoU
        exclude = ['date_added']

        widgets = {
            'organisation': TextInput(attrs={
                'style': 'width: 100%;',
                'placeholder': 'Organisation'
                }),
            'mod_col' : TextInput(attrs={
                'style': 'width: 100%',
                'placeholder': 'Mode of Collaboration',
            }),
            'validity': NumberInput(attrs={
                'style': 'width: 100%;',
                'placeholder': 'Validity',
            }),
            'date': SelectDateWidget(attrs={
                'style': 'width: 100%;',
                'placeholder': 'Date',
            }),
            'u_id': SelectMultiple(attrs={
                'style': 'width: 100%;',
                'placeholder': 'Faculty involved',
            }),
        }
class ProposalForm(forms.ModelForm):
    """def __init__(self, *args, **kwargs):
        user = kwargs.pop('user','')
        super(GrantForm, self).__init__(*args, **kwargs)
        self.fields['PI']=forms.ModelChoiceField(queryset=Profile.objects.all())
        self.fields['CO_PI']=forms.ModelChoiceField(queryset=Profile.objects.all())"""

    class Meta:
        model = Proposal
        exclude = ['date_added']

        widgets = {
            'title': TextInput(attrs={
                'style': 'width: 100%;',
                'placeholder': 'Title'
                }),
            'submitted_to' : TextInput(attrs={
                'style': 'width: 100%',
                'placeholder': 'Submitted to',
            }),
            'budg_amt': NumberInput(attrs={
                'style': 'width: 100%;',
                'placeholder': 'Budgetted amount',
            }),
            'status': Select(attrs={
                'style': 'width: 100%;',
                'placeholder': 'Status',
            }),
            'PI': Select(attrs={
                'style': 'width: 100%;',
                'placeholder': 'PI',
            }),
            'CO_PI': Select(attrs={
                'style': 'width: 100%;',
                'placeholder': 'Co PI',
            }),
        }

class ConsultancyForm(forms.ModelForm):
    """def __init__(self, *args, **kwargs):
        user = kwargs.pop('user','')
        super(GrantForm, self).__init__(*args, **kwargs)
        self.fields['PI']=forms.ModelChoiceField(queryset=Profile.objects.all())
        self.fields['CO_PI']=forms.ModelChoiceField(queryset=Profile.objects.all())"""

    class Meta:
        model = Consultancy
        exclude = ['date_added']

        widgets = {
            'title': TextInput(attrs={
                'style': 'width: 100%;',
                'placeholder': 'Title'
                }),
            'fund_agency' : TextInput(attrs={
                'style': 'width: 100%',
                'placeholder': 'Funding Agency',
            }),
            'rec_amt': NumberInput(attrs={
                'style': 'width: 100%;',
                'placeholder': 'Validity',
            }),
            'f_id': Select(attrs={
                'style': 'width: 100%;',
                'placeholder': 'Faculty involved',
            }),
        }
class LectureForm(forms.ModelForm):
    """def __init__(self, *args, **kwargs):
        user = kwargs.pop('user','')
        super(GrantForm, self).__init__(*args, **kwargs)
        self.fields['PI']=forms.ModelChoiceField(queryset=Profile.objects.all())
        self.fields['CO_PI']=forms.ModelChoiceField(queryset=Profile.objects.all())"""

    class Meta:
        model = Lecture
        exclude = ['date_added']

        widgets = {
            'topic': TextInput(attrs={
                'style': 'width: 100%;',
                'placeholder': 'Topic'
                }),
            'res_person' : TextInput(attrs={
                'style': 'width: 100%',
                'placeholder': 'Resource Person',
            }),
            'organisation': TextInput(attrs={
                'style': 'width: 100%;',
                'placeholder': 'Organisation',
            }),
            'n_stud': NumberInput(attrs={
                'style': 'width: 100%;',
                'placeholder': 'No of students',
            }),
            'n_fac': NumberInput(attrs={
                'style': 'width: 100%;',
                'placeholder': 'No of faculty',
            }),
            'n_ind': NumberInput(attrs={
                'style': 'width: 100%;',
                'placeholder': 'No from industry',
            }),
            'f_id': Select(attrs={
                'style': 'width: 100%;',
                'placeholder': 'Faculty involved',
            }),
        }
class TalkForm(forms.ModelForm):
    """def __init__(self, *args, **kwargs):
        user = kwargs.pop('user','')
        super(GrantForm, self).__init__(*args, **kwargs)
        self.fields['PI']=forms.ModelChoiceField(queryset=Profile.objects.all())
        self.fields['CO_PI']=forms.ModelChoiceField(queryset=Profile.objects.all())"""

    class Meta:
        model = Talk
        exclude = ['date_added']

        widgets = {
            'topic': TextInput(attrs={
                'style': 'width: 100%;',
                'placeholder': 'Topic'
                }),
            'venue' : TextInput(attrs={
                'style': 'width: 100%',
                'placeholder': 'Venue',
            }),
            'n_stud': NumberInput(attrs={
                'style': 'width: 100%;',
                'placeholder': 'No of students',
            }),
            'n_fac': NumberInput(attrs={
                'style': 'width: 100%;',
                'placeholder': 'No of faculty',
            }),
            'n_ind': NumberInput(attrs={
                'style': 'width: 100%;',
                'placeholder': 'No from industry',
            }),
            'date': SelectDateWidget(attrs={
                'style': 'width: 100%;',
                'placeholder': 'Date',
            }),
            'f_id': Select(attrs={
                'style': 'width: 100%;',
                'placeholder': 'Faculty involved',
            }),
        }
class ActivityForm(forms.ModelForm):
    """def __init__(self, *args, **kwargs):
        user = kwargs.pop('user','')
        super(GrantForm, self).__init__(*args, **kwargs)
        self.fields['PI']=forms.ModelChoiceField(queryset=Profile.objects.all())
        self.fields['CO_PI']=forms.ModelChoiceField(queryset=Profile.objects.all())"""

    class Meta:
        model = Other_Activity
        exclude = ['date_added']

        widgets = {
            'act_id': NumberInput(attrs={
                'style': 'width: 100%;',
                'placeholder': 'Activity ID'
                }),
            'activity' : TextInput(attrs={
                'style': 'width: 100%',
                'placeholder': 'Activity',
            }),
            'date': SelectDateWidget(attrs={
                'style': 'width: 100%;',
                'placeholder': 'Date',
            }),
            'f_id': Select(attrs={
                'style': 'width: 100%;',
                'placeholder': 'Faculty involved',
            }),
        }
class AchievementForm(forms.ModelForm):
    """def __init__(self, *args, **kwargs):
        user = kwargs.pop('user','')
        super(GrantForm, self).__init__(*args, **kwargs)
        self.fields['PI']=forms.ModelChoiceField(queryset=Profile.objects.all())
        self.fields['CO_PI']=forms.ModelChoiceField(queryset=Profile.objects.all())"""

    class Meta:
        model = Achievement
        exclude = ['date_added']

        widgets = {
            'title' : TextInput(attrs={
                'style': 'width: 100%',
                'placeholder': 'Title',
            }),
            'organisation': TextInput(attrs={
                'style': 'width: 100%;',
                'placeholder': 'Organisation'
            }),
            'f_id': Select(attrs={
                'style': 'width: 100%;',
                'placeholder': 'Faculty involved',
            }),
        }
class ConferenceForm(forms.ModelForm):
    """def __init__(self, *args, **kwargs):
        user = kwargs.pop('user','')
        super(GrantForm, self).__init__(*args, **kwargs)
        self.fields['PI']=forms.ModelChoiceField(queryset=Profile.objects.all())
        self.fields['CO_PI']=forms.ModelChoiceField(queryset=Profile.objects.all())"""

    class Meta:
        model = Conference
        exclude = ['date_added']

        widgets = {
            'title': TextInput(attrs={
                'style': 'width: 100%;',
                'placeholder': 'Title'
                }),
            'conference' : TextInput(attrs={
                'style': 'width: 100%',
                'placeholder': 'Conference',
            }),
            'volume': NumberInput(attrs={
                'style': 'width: 100%;',
                'placeholder': 'Volume#',
            }),
            'issue': NumberInput(attrs={
                'style': 'width: 100%;',
                'placeholder': 'Issue#',
            }),
            'n_page': NumberInput(attrs={
                'style': 'width: 100%;',
                'placeholder': 'Page#',
            }),
            'nat_int': Select(attrs={
                'style': 'width: 100%;',
                'placeholder': 'National/International',
            }),
            'u_id': Select(attrs={
                'style': 'width: 100%;',
                'placeholder': 'Faculty involved',
            }),
        }
class IndustrialForm(forms.ModelForm):
    """def __init__(self, *args, **kwargs):
        user = kwargs.pop('user','')
        super(GrantForm, self).__init__(*args, **kwargs)
        self.fields['PI']=forms.ModelChoiceField(queryset=Profile.objects.all())
        self.fields['CO_PI']=forms.ModelChoiceField(queryset=Profile.objects.all())"""

    class Meta:
        model = Industrial_visit
        exclude = ['date_added']

        widgets = {
            'visit_no': NumberInput(attrs={
                'style': 'width: 100%;',
                'placeholder': 'Visit#'
                }),
            'purpose' : TextInput(attrs={
                'style': 'width: 100%',
                'placeholder': 'Purpose of visit',
            }),
            'industry': TextInput(attrs={
                'style': 'width: 100%;',
                'placeholder': 'Industry',
            }),
            'semester': NumberInput(attrs={
                'style': 'width: 100%;',
                'placeholder': 'Semester',
            }),
            'n_stud': NumberInput(attrs={
                'style': 'width: 100%;',
                'placeholder': 'No of students',
            }),
            'u_id': SelectMultiple(attrs={
                'style': 'width: 100%;',
                'placeholder': 'Faculty involved',
            }),
        }
class MembershipForm(forms.ModelForm):
    """def __init__(self, *args, **kwargs):
        user = kwargs.pop('user','')
        super(GrantForm, self).__init__(*args, **kwargs)
        self.fields['PI']=forms.ModelChoiceField(queryset=Profile.objects.all())
        self.fields['CO_PI']=forms.ModelChoiceField(queryset=Profile.objects.all())"""

    class Meta:
        model = Membership
        exclude = ['date_added']

        widgets = {
            'mem_id': NumberInput(attrs={
                'style': 'width: 100%;',
                'placeholder': 'Membership ID'
             }),
            'membership' : TextInput(attrs={
                'style': 'width: 100%',
                'placeholder': 'Membership',
            }),
            'association': TextInput(attrs={
                'style': 'width: 100%;',
                'placeholder': 'Association',
            }),
            'term': NumberInput(attrs={
                'style': 'width: 100%;',
                'placeholder': 'Date',
            }),
            'u_id': SelectMultiple(attrs={
                'style': 'width: 100%;',
                'placeholder': 'Faculty involved',
            }),
        }
class PatentForm(forms.ModelForm):
    """def __init__(self, *args, **kwargs):
        user = kwargs.pop('user','')
        super(GrantForm, self).__init__(*args, **kwargs)
        self.fields['PI']=forms.ModelChoiceField(queryset=Profile.objects.all())
        self.fields['CO_PI']=forms.ModelChoiceField(queryset=Profile.objects.all())"""

    class Meta:
        model = Patent
        exclude = ['date_added']

        widgets = {
            'title': TextInput(attrs={
                'style': 'width: 100%;',
                'placeholder': 'Title'
                }),
            'topic' : TextInput(attrs={
                'style': 'width: 100%',
                'placeholder': 'Topic',
            }),
            'status': Select(attrs={
                'style': 'width: 100%;',
                'placeholder': 'Status',
            }),
            'u_id': SelectMultiple(attrs={
                'style': 'width: 100%;',
                'placeholder': 'Faculty involved',
            }),
        }
