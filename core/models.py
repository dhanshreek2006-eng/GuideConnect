from django.db import models
from django.contrib.auth.models import User


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Enrollment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    program = models.CharField(max_length=100)
    enrolled_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='Pending')

    def __str__(self):
        return self.name


class Goal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    progress = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class LearningProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    skill = models.CharField(max_length=100)
    progress = models.IntegerField(default=0)
    status = models.CharField(max_length=30, default='In Progress')

    def __str__(self):
        return self.skill


class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mentor_name = models.CharField(max_length=100)
    rating = models.IntegerField(default=5)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.mentor_name


class Session(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mentor_name = models.CharField(max_length=100)
    topic = models.CharField(max_length=200)
    session_date = models.DateField()
    session_time = models.TimeField()
    status = models.CharField(max_length=20, default='Confirmed')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.mentor_name} - {self.topic}"


class Mentor(models.Model):
    name = models.CharField(max_length=100)
    expertise = models.CharField(max_length=200)
    experience = models.CharField(max_length=100)
    bio = models.TextField()
    image = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name


class Program(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.CharField(max_length=50)
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    skills = models.TextField()
    image = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name