from rest_framework import viewsets
from .models import Person, Notebook, Note
from .serializers import PersonSerializer, NotebookSerializer, NoteSerializer

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class NotebookViewSet(viewsets.ModelViewSet):
    queryset = Notebook.objects.all()
    serializer_class = NotebookSerializer

class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

#def index(request):
#    return HttpResponse("<h1>MyHomepage</h1>")

"""class PersonList(APIView):

    def get(self, request):
        persons = Person.objects.all()
        serializer = PersonSerializer(persons, many=True)
        return Response(serializer.data)

    def post(self):
        pass
"""
