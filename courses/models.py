from django.core.urlresolvers import reverse
from django.db import models


class Course(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    
    def __str__(self):
        return self.title


class Step(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    order = models.IntegerField(default=0)
    course = models.ForeignKey(Course)
    
    class Meta:
        abstract = True
        # this wil get rid of the table(can't have abstract models in Admin), usually will not start with a table
        ordering = ['order', ]
    
    def __str__(self):
        return self.title


class Text(Step):
    content = models.TextField(blank=True, default='')

    def get_absolute_url(self):
        return reverse('courses:text', kwargs={
            'course_pk': self.course_id,  # could also do self.course.pk but id requires one less lookup
            'step_pk': self.id
        })


class Quiz(Step):
    total_questions = models.IntegerField(default=4)

    class Meta:
        verbose_name_plural = "Quizzes"  # renames to correct spelling for quizzes

    def get_absolute_url(self):
        return reverse('courses:quiz', kwargs={
            'course_pk': self.course_id,  # could also do self.course.pk but id requires one less lookup
            'step_pk': self.id
        })


class Question(models.Model):
    quiz = models.ForeignKey(Quiz)
    order = models.IntegerField(default=0)
    prompt = models.TextField()

    class Meta:
        ordering = ['order', ]

    def get_absolute_url(self):
        return self.quiz.get_absolute_url()

    def __str__(self):
        return self.prompt

