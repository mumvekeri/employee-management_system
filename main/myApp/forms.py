# forms.py
from django import forms
from .models import PerformanceReview, Goal, Feedback

class PerformanceReviewForm(forms.ModelForm):
    class Meta:
        model = PerformanceReview
        fields = ['employee_name', 'review_date', 'review_comments']

class GoalForm(forms.ModelForm):
    class Meta:
        model = Goal
        fields = ['title', 'description', 'deadline']

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['feedback_from', 'feedback_to', 'comments']
