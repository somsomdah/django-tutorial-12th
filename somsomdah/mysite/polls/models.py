from django.db import models
from django.utils import timezone
import datetime


class Question(models.Model):
    question_text = models.CharField(max_length=200)  # 필드의 자료형, max_length 필수
    pub_date = models.DateTimeField('date published')  # 첫번재 위치 인수를 'date published' 라고 정함..?

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)  # Choice가 Question 에 관계됨
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
