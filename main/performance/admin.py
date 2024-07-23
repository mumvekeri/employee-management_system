from django.shortcuts import render, redirect
from .models import PerformanceReview, Goal, Feedback
from .forms import PerformanceReviewForm, GoalForm, FeedbackForm

def perfomance(request):
    if request.method == 'POST':
        if 'review_submit' in request.POST:
            review_form = PerformanceReviewForm(request.POST)
            if review_form.is_valid():
                review_form.save()
                return redirect('perfomance')
        elif 'goal_submit' in request.POST:
            goal_form = GoalForm(request.POST)
            if goal_form.is_valid():
                goal_form.save()
                return redirect('perfomance')
        elif 'feedback_submit' in request.POST:
            feedback_form = FeedbackForm(request.POST)
            if feedback_form.is_valid():
                feedback_form.save()
                return redirect('perfomance')
    else:
        review_form = PerformanceReviewForm()
        goal_form = GoalForm()
        feedback_form = FeedbackForm()
    
    reviews = PerformanceReview.objects.all()
    goals = Goal.objects.all()
    feedbacks = Feedback.objects.all()
    
    return render(request, 'perfomance.html', {
        'review_form': review_form,
        'goal_form': goal_form,
        'feedback_form': feedback_form,
        'reviews': reviews,
        'goals': goals,
        'feedbacks': feedbacks,
    })
