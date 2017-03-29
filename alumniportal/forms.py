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

from multiupload.fields import MultiFileField

class EditProfileForm(forms.ModelForm):
    """
    Form for alumnus to edit profile
    """
    date_of_birth = forms.DateTimeField(widget=DateTimePicker(options={"format": "YYYY-MM-DD", "pickTime":False}, attrs={'placeholder': 'yyyy-mm-dd'}))
    roll_no = forms.IntegerField(disabled = True)
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
        # for field in self.fields.values():
            # field.error_messages = {'required':''}
        self.helper = FormHelper()

        self.helper.form_id = 'id_edit_profile_form'
        self.helper.form_class = 'form-horizontal col-md-10'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.form_method = 'post'
        self.helper.form_action = '/edit-profile/personal/'
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
            FormActions(Submit('Save', 'Save', css_class='btn-primary')),
        )

#### my edits
class AddActivityForm(forms.ModelForm):
    """
    Form to create a new Activity
    """
    files = MultiFileField(max_num = 10, min_num = 0, max_file_size = 1024*1024*5, required=False)
    end_date = forms.DateTimeField(widget=DateTimePicker(options={"format": "YYYY-MM-DD HH:MM:SS", "pickSeconds":False}))

    class Meta:
        model = models.Activity
        exclude = ('profile','created','images')
    def __init__(self, *args, **kwargs):
        super(AddActivityForm, self).__init__(*args, **kwargs)
        # for field in self.fields.values():
            # field.error_messages = {'required':''}
        self.helper = FormHelper()
        self.helper.form_id = 'id_add_activity_form'
        self.helper.form_class = 'form-horizontal col-md-12'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.form_method = 'post'
        self.helper.form_action = '/activity/add/'
        self.helper.layout = Layout(
            'activity_type',
            'name',
            'purpose',
            'image',
            'end_date',
            'requirement',
            'description',
            # 'peoples_involved',
            Field('files', style="border : none; -webkit-box-shadow: none; box-shadow: none; width: 100%; padding: 0px;"),
            FormActions(Submit('Save', 'Save', css_class='form-btn', style = 'width: 30%;')),
        )

class EditBlogDetails(forms.ModelForm):
    """
    Form to create a new Activity
    """
    images_field = MultiFileField(max_num = 10, min_num = 0, max_file_size = 1024*1024*5, required=False)
    videos_field = MultiFileField(max_num = 10, min_num = 0, max_file_size = 1024*1024*5, required=False)

    class Meta:
        model = models.Blog
        exclude = ('profile','videos','images','recent')
    def __init__(self, *args, **kwargs):
        super(EditBlogDetails, self).__init__(*args, **kwargs)
        # for field in self.fields.values():
            # field.error_messages = {'required':''}
        self.helper = FormHelper()
        self.helper.form_id = 'id_add_activity_form'
        self.helper.form_class = 'form-horizontal col-md-10'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.form_method = 'post'
        self.helper.form_action = '/edit-profile/blog/'
        self.helper.layout = Layout(
            Div(
                # AccordionGroup('Introduction',
                'profile_picture',
                Field('about_me', style = "width: 90%; height: 100px;"),
                Field('interests', style = "width: 90%; height: 100px;"),
                Field('message_to_the_world', style = "width: 90%; height: 100px;"),
                # ),
                # AccordionGroup('Photos/Videos',
                Field('images_field', style="border : none; -webkit-box-shadow: none; box-shadow: none;"),
                Field('videos_field', style="border : none; -webkit-box-shadow: none; box-shadow: none;"),
                style = "background-color: #fff; padding: 10px",
                # ),
            ),
            FormActions(Submit('Save', 'Save', css_class='btn-primary')),
        )




class IITGExperienceFormSetHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(IITGExperienceFormSetHelper, self).__init__(*args, **kwargs)
        self.form_method = 'post'
        self.form_action = '/edit-profile/iitg/'
        self.form_class = 'form-horizontal col-md-10'
        self.label_class = 'col-md-3'
        self.field_class = 'col-md-9'
        self.form_method = 'post'
        self.layout = Layout(
            Div(
                'club_name',
                'experience',
                Field('DELETE'),
                FormActions(Submit('Save', 'Save', css_class='btn-primary')),
                css_class="edit_form_container",
            ),
        )
        self.render_required_fields = True
        self.html5_required = True

class ProjectFormSetHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(ProjectFormSetHelper, self).__init__(*args, **kwargs)
        self.form_method = 'post'
        self.form_action = '/edit-profile/project/'
        self.form_class = 'form-horizontal col-md-10'
        self.label_class = 'col-md-3'
        self.field_class = 'col-md-9'
        self.form_method = 'post'
        self.layout = Layout(
            Div(
                'topic',
                'mentor',
                'description',
                'start_date',
                'end_date',
                Field('DELETE'),

                FormActions(Submit('Save', 'Save', css_class='btn-primary')),
                css_class="edit_form_container",
            ),
        )
        self.render_required_fields = True

class EducationFormSetHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(EducationFormSetHelper, self).__init__(*args, **kwargs)
        self.form_method = 'post'
        self.form_action = '/edit-profile/education/'
        self.form_class = 'form-horizontal col-md-10'
        self.label_class = 'col-md-3'
        self.field_class = 'col-md-9'
        self.form_method = 'post'

        self.layout = Layout(
            Div(
                'degree',
                Field('institute'),
                'start_year',
                'end_year',
                'department',
                'specialization',
                Field('DELETE'),
                FormActions(Submit('Save', 'Save', css_class='btn-primary')),
                css_class="edit_form_container",
            ),
        )
        self.render_required_fields = True

class JobFormSetHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(JobFormSetHelper, self).__init__(*args, **kwargs)
        self.form_method = 'post'
        self.form_action = '/edit-profile/professional/'
        self.form_class = 'form-horizontal col-md-10'
        self.label_class = 'col-md-3'
        self.field_class = 'col-md-9'
        self.form_method = 'post'
        self.layout = Layout(
            Div(
            'company',
            'position',
            'description',
            'start_date',
            'end_date',
            'city',
                Field('DELETE'),
                FormActions(Submit('Save', 'Save', css_class='btn-primary')),
                css_class="edit_form_container",
            ),
        )
        self.render_required_fields = True

class AchievementFormSetHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(AchievementFormSetHelper, self).__init__(*args, **kwargs)
        self.form_method = 'post'
        self.form_action = '/edit-profile/achievement/'
        self.form_class = 'form-horizontal col-md-10'
        self.label_class = 'col-md-3'
        self.field_class = 'col-md-9'
        self.form_method = 'post'
        self.layout = Layout(
            Div(
            'achievement',
            'achievement_type',
            'year',
            'description',
                Field('DELETE'),
                FormActions(Submit('Save', 'Save', css_class='btn-primary')),
                css_class="edit_form_container",
            ),
        )
        self.render_required_fields = True

class AddNewsForm(forms.ModelForm):
    """
    Form for admin to add news
    """

    class Meta:
        model = models.News
        exclude = ('timestamp', 'recent')

    def __init__(self, *args, **kwargs):
        super(AddNewsForm, self).__init__(*args, **kwargs)

        # for field in self.fields.values():
            # field.error_messages = {'required':''}
        self.helper = FormHelper()
        self.helper.form_id = 'id_add_news_form'
        self.helper.form_class = 'form-horizontal col-md-12'
        self.helper.label_class = 'col-md-2'
        self.helper.field_class = 'col-md-10'
        self.helper.form_method = 'post'
        self.helper.form_action = '/news/add/'
        self.helper.layout = Layout(
            'post_type',
            'heading',
            'content',
            'image',
            FormActions(Submit('Save', 'Save', css_class='form-btn', style = 'width: 30%;')),
        )


class AddPostForm(forms.ModelForm):
    """
    Form for users to add posts to their blogs
    """

    class Meta:
        model = models.Post
        exclude = ('blog', 'timestamp', 'recent')

    def __init__(self, *args, **kwargs):
        username = kwargs.pop('username', None)
        super(AddPostForm, self).__init__(*args, **kwargs)

        # for field in self.fields.values():
            # field.error_messages = {'required':''}
        self.helper = FormHelper()
        self.helper.form_id = 'id_add_post_form'
        self.helper.form_class = 'form-horizontal col-md-12'
        self.helper.label_class = 'col-md-2'
        self.helper.field_class = 'col-md-10'
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            'heading',
            'content',
            'image',
            FormActions(Submit('Save', 'Save', css_class='form-btn', style = 'width: 30%;')),
        )


class PostCommentForm(forms.ModelForm):
    """
    Form for blog post comments
    """
    class Meta:
        model = models.PostComment
        exclude = ['post']
        widgets = {
            'comment': forms.TextInput(
                attrs={
                    'id': 'comment-text',
                    'required': True,
                    'placeholder': 'Write a comment...',
                    'class': 'form-control',
                }
            ),
        }

class AddClubPostForm(forms.ModelForm):
    pass

# class EditEducationForm(forms.ModelForm):
#     """
#     Form for alumnus to edit education details (a tab within the profile edit page)
#     """
#     # date_of_birth = forms.DateTimeField(widget=DateTimePicker(options={"format": "DD-MM-YYYY", "pickTime":False}))

#     class Meta:
#         model = models.Education
#         exclude = ('profile',)

#     def __init__(self, *args, **kwargs):
#         super(EditEducationForm, self).__init__(*args, **kwargs)

#         for field in self.fields.values():
#             field.error_messages = {'required':''}
#         self.helper = FormHelper()
#         self.helper.form_id = 'id_edit_education_form'
#         self.helper.form_class = 'form-horizontal col-md-10'
#         self.helper.label_class = 'col-md-3'
#         self.helper.field_class = 'col-md-9'
#         self.helper.form_method = 'post'
#         self.helper.form_action = '/edit-profile/'

#         self.helper.layout = Layout(
#             'degree',
#             'institute',
#             'in_iitg',
#             'start_year',
#             'end_year',
#             'department',
#             'specialization',
#             FormActions(Submit('Save', 'Save', css_class='btn-primary')),
#         )

# class EditIITGExperienceForm(forms.ModelForm):
#     """
#     Form for alumnus to edit education details (a tab within the profile edit page)
#     """
#     # date_of_birth = forms.DateTimeField(widget=DateTimePicker(options={"format": "DD-MM-YYYY", "pickTime":False}))

#     class Meta:
#         model = models.IITGExperience
#         exclude = ('profile',)

#     def __init__(self, *args, **kwargs):
#         super(EditIITGExperienceForm, self).__init__(*args, **kwargs)

#         for field in self.fields.values():
#             field.error_messages = {'required':''}
#         self.helper = FormHelper()
#         self.helper.form_id = 'id_edit_education_form'
#         self.helper.form_class = 'form-horizontal col-md-10'
#         self.helper.label_class = 'col-md-3'
#         self.helper.field_class = 'col-md-9'
#         self.helper.form_method = 'post'
#         self.helper.form_action = '/edit-profile/'
#         self.helper.layout = Layout(
#             'club_name',
#             'experience',
#             FormActions(Submit('Save', 'Save', css_class='btn-primary')),
#         )

# class EditProjectForm(forms.ModelForm):
#     """
#     Form for alumnus to edit education details (a tab within the profile edit page)
#     """
#     # date_of_birth = forms.DateTimeField(widget=DateTimePicker(options={"format": "DD-MM-YYYY", "pickTime":False}))

#     class Meta:
#         model = models.Project
#         exclude = ('profile','recent',)

#     def __init__(self, *args, **kwargs):
#         super(EditProjectForm, self).__init__(*args, **kwargs)

#         for field in self.fields.values():
#             field.error_messages = {'required':''}
#         self.helper = FormHelper()
#         self.helper.form_id = 'id_edit_education_form'
#         self.helper.form_class = 'form-horizontal col-md-10'
#         self.helper.label_class = 'col-md-3'
#         self.helper.field_class = 'col-md-9'
#         self.helper.form_method = 'post'
#         self.helper.form_action = '/edit-profile/'
#         self.helper.layout = Layout(
#             'topic',
#             'mentor',
#             'description',
#             'start_date',
#             'end_date',
#             FormActions(Submit('Save', 'Save', css_class='btn-primary')),
#         )


# class EditAchievementForm(forms.ModelForm):
#     """
#     Form for alumnus to edit education details (a tab within the profile edit page)
#     """
#     # date_of_birth = forms.DateTimeField(widget=DateTimePicker(options={"format": "DD-MM-YYYY", "pickTime":False}))

#     class Meta:
#         model = models.Achievement
#         exclude = ('profile','recent',)

#     def __init__(self, *args, **kwargs):
#         super(EditAchievementForm, self).__init__(*args, **kwargs)

#         for field in self.fields.values():
#             field.error_messages = {'required':''}
#         self.helper = FormHelper()
#         self.helper.form_id = 'id_edit_education_form'
#         self.helper.form_class = 'form-horizontal col-md-10'
#         self.helper.label_class = 'col-md-3'
#         self.helper.field_class = 'col-md-9'
#         self.helper.form_method = 'post'
#         self.helper.form_action = '/edit-profile/'
#         self.helper.layout = Layout(

#             'achievement',
#             'achievement_type',
#             'year',
#             'description',
#             FormActions(Submit('Save', 'Save', css_class='btn-primary')),
#         )



# class EditJobForm(forms.ModelForm):
#     """
#     Form for alumnus to edit education details (a tab within the profile edit page)
#     """
#     # date_of_birth = forms.DateTimeField(widget=DateTimePicker(options={"format": "DD-MM-YYYY", "pickTime":False}))

#     class Meta:
#         model = models.Job
#         exclude = ('profile',)

#     def __init__(self, *args, **kwargs):
#         super(EditJobForm, self).__init__(*args, **kwargs)

#         for field in self.fields.values():
#             field.error_messages = {'required':''}
#         self.helper = FormHelper()
#         self.helper.form_id = 'id_edit_education_form'
#         self.helper.form_class = 'form-horizontal col-md-10'
#         self.helper.label_class = 'col-md-3'
#         self.helper.field_class = 'col-md-9'
#         self.helper.form_method = 'post'
#         self.helper.form_action = '/edit-profile/'
#         self.helper.layout = Layout(
#             'company',
#             'position',
#             'description',
#             'start_date',
#             'end_date',
#             'city',
#             FormActions(Submit('Save', 'Save', css_class='btn-primary')),
#         )



