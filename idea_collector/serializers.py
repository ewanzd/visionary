from rest_framework import serializers
from .models import Person, Notebook, Note

class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ('__all__')

class NotebookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Notebook
        fields = ('title', 'description')

class NoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Note
        fields = ('subject', 'content', 'keyword', 'person', 'created', 'notebook')
