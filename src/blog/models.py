from django.db import models

# Create your models here.
#on dirait on a creer un tableau nome profile et on y ajoute des colonnes 
'''
#django model field :
    -html widget dans admin page de django
    -validation(ex verifer si un email par exemple)
    -db size of the field
    python manage.py makemigrations #verifier si cest correcte ou pas
    python manage.py migrate # do it
'''

class job (models.Model):#tab(class)
    title=models.CharField(max_length=100) #100 #first column (field)