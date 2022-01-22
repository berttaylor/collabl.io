from django.forms import ModelForm, HiddenInput, CharField, DateInput, ModelChoiceField, Textarea, \
    SelectMultiple, FileField
from django.forms.widgets import Select

from collaborations.models import CollaborationMilestone, CollaborationTask


class TaskForm(ModelForm):
    # We hide the collaboration section, as this is set by the view

    assigned_to = ModelChoiceField(queryset=None, required=False)

    def __init__(self, *args, **kwargs):
        """
        We override init to grab the collaboration, and use it to populate the assigned_to with the group members,
        so that they can be selected
        """
        super(TaskForm, self).__init__(*args, **kwargs)
        if kwargs.get('initial'):
            collaboration = kwargs['initial']['collaboration']
            group_members = collaboration.related_group.members.all()
            self.fields['assigned_to'].queryset = group_members
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = CollaborationTask
        fields = ["name", "description", "assigned_to",]
        widgets = {
            "assigned_to": Select(
                attrs={
                    "class": "form-control",
                    "id": "task_name",
                    "rows": "1",
                    "required": True
                }
            ),
            "description": Textarea(
                attrs={
                    "class": "validate form-control",
                    "rows": 4,
                    "cols": 5,
                }
            ),
        }


class DateInputLocal(DateInput):
    input_type = 'datetime-local'


class MilestoneForm(ModelForm):
    # We hide the collaboration section, as this is set by the view
    collaboration = CharField(widget=HiddenInput(), required=False)

    class Meta:
        model = CollaborationMilestone
        fields = ["name", "target_date", "collaboration"]
        widgets = {
            'target_date': DateInputLocal()
        }

    def __init__(self, *args, **kwargs):
        super(MilestoneForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
