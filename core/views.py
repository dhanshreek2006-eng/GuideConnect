from django.shortcuts import render, redirect, get_object_or_404
from .models import Enrollment, Goal, LearningProgress, Feedback, Session, ContactMessage, Program, Mentor
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'home.html')


def mentors(request):
    mentors = Mentor.objects.all()

    return render(request, 'mentors.html', {
        'mentors': mentors
    })


def mentor_profile(request, mentor_id):

    mentor = get_object_or_404(Mentor, id=mentor_id)

    return render(request, 'mentor_profile.html', {
        'mentor': mentor
    })


def programs(request):

    programs = Program.objects.all()

    return render(request, 'programs.html', {
        'programs': programs
    })


def program_details(request, program_id):

    program = get_object_or_404(Program, id=program_id)

    return render(request, 'program_details.html', {
        'program': program
    })


def enrollment(request):

    if request.method == 'POST':

        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        program = request.POST.get('program')

        Enrollment.objects.create(
            name=name,
            email=email,
            phone=phone,
            program=program
        )

        return render(request, 'enrollment.html', {
            'success': True
        })

    return render(request, 'enrollment.html')


def sessions(request):
    return render(request, 'sessions.html')


@login_required
def book_session(request):

    if request.method == 'POST':

        mentor_name = request.POST.get('mentor_name')
        topic = request.POST.get('topic')
        session_date = request.POST.get('session_date')
        session_time = request.POST.get('session_time')

        Session.objects.create(
            user=request.user,
            mentor_name=mentor_name,
            topic=topic,
            session_date=session_date,
            session_time=session_time
        )

        return render(request, 'book_session.html', {
            'success': True
        })

    return render(request, 'book_session.html')


@login_required
def my_sessions(request):

    sessions = Session.objects.filter(user=request.user)

    return render(request, 'my_sessions.html', {
        'sessions': sessions
    })


def register(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        return redirect('/login/')

    return render(request, 'register.html')


def user_login(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect('/dashboard/')

        return render(request, 'login.html', {
            'error': 'Invalid username or password.'
        })

    return render(request, 'login.html')


@login_required
def dashboard(request):

    goals = Goal.objects.filter(user=request.user)
    progress = LearningProgress.objects.filter(user=request.user)
    sessions = Session.objects.filter(user=request.user)
    feedback = Feedback.objects.filter(user=request.user)

    return render(request, 'dashboard.html', {
        'goals': goals,
        'progress': progress,
        'sessions': sessions,
        'feedback': feedback,
    })


def about(request):
    return render(request, 'about.html')


def contact(request):

    if request.method == 'POST':

        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        ContactMessage.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )

        return render(request, 'contact.html', {
            'success': True
        })

    return render(request, 'contact.html')


@login_required
def session_history(request):

    sessions = Session.objects.filter(
        user=request.user,
        status='Completed'
    )

    return render(request, 'session_history.html', {
        'sessions': sessions
    })


def user_logout(request):

    logout(request)

    return redirect('/login/')