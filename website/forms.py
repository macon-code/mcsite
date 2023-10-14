from django.forms import ModelForm

from .models import ProjectRequest


class ProjectRequestForm(ModelForm):
    class Meta:
        model = ProjectRequest
        fields = ["name", "contact_email", "description"]

    def __init__(self, *args, **kwargs):
        super(ProjectRequestForm, self).__init__(*args, **kwargs)
        self.fields["name"].widget.attrs["placeholder"] = "Project Name"
        self.fields["contact_email"].widget.attrs["placeholder"] = "email@example.com"
        self.fields["description"].widget.attrs["placeholder"] = "A detailed description of the project..."
