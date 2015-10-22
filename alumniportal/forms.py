from alumniportal import models
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, HTML
from crispy_forms.bootstrap import TabHolder, Tab, Div, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, InlineCheckboxes
from crispy_forms.bootstrap import Accordion, AccordionGroup
from crispy_forms.bootstrap import FormActions
from django.contrib.auth.models import User
from django import forms
from django.forms.extras.widgets import SelectDateWidget
from django.contrib.admin.widgets import AdminSplitDateTime
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import forms as UserForms
from django.core.validators import RegexValidator
from datetime import datetime
from bootstrap3_datetime.widgets import DateTimePicker

####edited
from multiupload.fields import MultiFileField


class EditProfileForm(forms.ModelForm):
    """
    Form for alumnus to edit profile
    """
    # date_of_birth = forms.DateTimeField(widget=DateTimePicker(options={"format": "DD-MM-YYYY", "pickTime":False}))

    class Meta:
        model = models.Profile
        exclude = ('blog_id', 'user', 'current_job_id', 'room_no')
        dateOptions = {
            'startView': 4,
        }

    def __init__(self, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        for index, field in enumerate(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'tabindex': index+1,
            })
        for field in self.fields.values():
            field.error_messages = {'required':''}
        self.helper = FormHelper()
        self.helper.form_id = 'id_edit_profile_form'
        self.helper.form_class = 'form-horizontal col-md-10'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.form_method = 'post'
        self.helper.form_action = '/edit-profile/'
        self.helper.layout = Layout(
            Accordion(
                AccordionGroup('Personal',
                    'name', 
                    'gender',
                    'date_of_birth',
                    'alternate_email',
                    'hostel',
                    'roll_no',
                    'batch',
                    'department',
                ),
                AccordionGroup('Contact',
                    'home_contact_no',
                    'work_contact_no',
                    'current_address', 
                    'city',
                    'country',
                    'nationality',
                ),
                AccordionGroup('Social',
                    'google_link',
                    'linkedin_link',
                    'facebook_link', 
                    'github_link',
                    'twitter_link',
                ),
            ),
            FormActions(Submit('Save', 'Save changes', css_class='btn-primary')),
        )

#### my edits
class AddActivityForm(forms.ModelForm):
    """
    Form to create a new Activity
    """
    files = MultiFileField(max_num = 10, min_num = 1, max_file_size = 1024*1024*5)
    # date_of_birth = forms.DateTimeField(widget=DateTimePicker(options={"format": "DD-MM-YYYY", "pickTime":False}))

    class Meta:
        model = models.Activity
        exclude = ('profile','created','images')
    def __init__(self, *args, **kwargs):
        super(AddActivityForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.error_messages = {'required':''}
        self.helper = FormHelper()
        self.helper.form_id = 'id_add_activity_form'
        self.helper.form_class = 'form-horizontal col-md-10'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.form_method = 'post'
        self.helper.form_action = '/activity/add/'
        self.helper.layout = Layout(
            'activity_type',
            'name',
            'purpose',
            'end_date',
            'requirement',
            'description',
            'peoples_involved',
            Field('files', style="border : none; -webkit-box-shadow: none; box-shadow: none;"),
            FormActions(Submit('Save', 'Save changes', css_class='btn-primary')),
        )

class BlogDetailsEdit(forms.ModelForm):
    """
    Form to create a new Activity
    """
    images_field = MultiFileField(max_num = 10, min_num = 1, max_file_size = 1024*1024*5)
    videos_field = MultiFileField(max_num = 10, min_num = 1, max_file_size = 1024*1024*5)
    
    class Meta:
        model = models.Blog
        exclude = ('profile','videos','images','recent')
    def __init__(self, *args, **kwargs):
        super(BlogDetailsEdit, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.error_messages = {'required':''}
        self.helper = FormHelper()
        self.helper.form_id = 'id_add_activity_form'
        self.helper.form_class = 'form-horizontal col-md-10'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.form_method = 'post'
        self.helper.form_action = '/blog/edit/'
        self.helper.layout = Layout(
            'profile_picture',
            'about_me',
            'interests',
            'message_to_the_world',
            Field('images_field', style="border : none; -webkit-box-shadow: none; box-shadow: none;"),
            Field('videos_field', style="border : none; -webkit-box-shadow: none; box-shadow: none;"),
            FormActions(Submit('Save', 'Save changes', css_class='btn-primary')),
        )


class EditEducationForm(forms.ModelForm):
    """
    Form for alumnus to edit education details (a tab within the profile edit page)
    """
    # date_of_birth = forms.DateTimeField(widget=DateTimePicker(options={"format": "DD-MM-YYYY", "pickTime":False}))

    class Meta:
        model = models.Profile
        exclude = ('profile',)

    def __init__(self, *args, **kwargs):
        super(EditEducationForm, self).__init__(*args, **kwargs)
        for index, field in enumerate(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'tabindex': index+1,
            })
        for field in self.fields.values():
            field.error_messages = {'required':''}
        self.helper = FormHelper()
        self.helper.form_id = 'id_edit_education_form'
        self.helper.form_class = 'form-horizontal col-md-10'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.form_method = 'post'
        self.helper.form_action = '/edit-profile/'
        self.helper.layout = Layout(
            'degree',
            'institute',
            'in_iitg',
            'start_year',
            'end_year',
            'department',
            'specialization',
            FormActions(Submit('Save', 'Save changes', css_class='btn-primary')),
        )


