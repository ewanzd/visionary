from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

class Notebook(models.Model):
    title = models.CharField(max_length=256)
    description = models.CharField(max_length=512)

    def __str__(self):
        return self.title

class Note(models.Model):
    subject = models.CharField(max_length=256)
    content = models.CharField(max_length=1024)
    keyword = models.CharField(max_length=256)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    created = models.DateTimeField()
    notebook = models.ForeignKey(Notebook, on_delete=models.CASCADE)

    def __str__(self):
        return self.subject
