from django import forms

from course.models import Course, AdviseFromPeople


class CourseForm(forms.ModelForm):
    # cover = forms.CharField(widget=forms.FileInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Course
        fields = [
            "title",
            "description",
            "video",
        ]


class CommentForm(forms.ModelForm):
    class Meta:
        model = AdviseFromPeople
        fields = [
            "mess",
        ]