from rest_framework import serializers
from .models import Person, Notebook, Note

class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ('id', 'name', 'url')

class NotebookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Notebook
        fields = ('id', 'title', 'description', 'url')

class NoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Note
        fields = ('__all__')
