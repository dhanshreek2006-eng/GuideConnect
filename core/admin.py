from django.contrib import admin

from .models import (
    Enrollment,
    Goal,
    LearningProgress,
    Feedback,
    Session,
    ContactMessage,
    Mentor,
    Program
)


admin.site.register(Enrollment)
admin.site.register(Goal)
admin.site.register(LearningProgress)
admin.site.register(Feedback)
admin.site.register(Session)
admin.site.register(ContactMessage)
admin.site.register(Mentor)
admin.site.register(Program)