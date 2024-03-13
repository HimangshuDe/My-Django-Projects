from django import forms

from todo_app.models import Tasks, Category


class TasksAddForm(forms.ModelForm):
    cat_name = forms.ModelChoiceField(
        queryset=Category.objects.all(), label="Select Category"
    )

    class Meta:
        model = Tasks
        fields = "__all__"
        widgets = {
            "due_date": forms.DateTimeInput(attrs={"type": "datetime-local"}),
        }


class CategoryAddForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"