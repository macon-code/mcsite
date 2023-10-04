from django.forms import ModelForm


class ProjectRequestForm(ModelForm):
    class Meta:
        model = ProjectRequest
        fields = ["name", "description"]
