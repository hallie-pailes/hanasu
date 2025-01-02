from django.db import models

# Create models here.
class Question(models.Model):
    question_text = models.CharField(max_length=255)
    correct_answer = models.CharField(max_length=255)

    def __str__(self):
        return self.question_text

class Answer(models.Model):
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text

class Quiz(models.Model):
    name = models.CharField(max_length=255)
    total_questions = models.IntegerField() 
    total_correct = models.IntegerField()

    def __str__(self):
        return self.name
