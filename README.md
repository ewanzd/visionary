pip list
pip install django==2.0
django-admin --version
pip install djangorestframework

django-admin startproject visionary

python .\manage.py startapp idea_collector

python .\manage.py runserver

python .\manage.py makemigrations idea_collector
python .\manage.py migrate

python .\manage.py sqlmigrate idea_collector 0001

python .\manage.py shell
Person.objects.all()
a = Person(name="Stefan")
a.save()
a.id
b = Notebook()
b.title="django"
b.describotion="Some ideas about the visionary project"
b.save()
Person.objects.filter(id=1)
Person.objects.filter(name__startswith='Ste')

python manage.py createsuperuser

