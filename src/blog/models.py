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

    in admin.py admin.site.register(job)
    i see the migration 1 0001 (id title)
    migration 2 0002 (jobtype)
    everytime i do migration isee it in migrations folder
    we see the filed added in 8000/admin/
'''
JOB_TYPE=(
    ('full ','part'),
    ('part ','full'),

)
class job (models.Model):#tab(class)
    title=models.CharField(max_length=100) #100 #first column (field)
    #location external bib
    job_type=models.CharField(max_length=15,choices=JOB_TYPE)##non nullable option 1 ''(when the is nothing)
    #big text i use textfield
    description=models.TextField(max_length=1000)
    #time of publication ,auto_now when its added ,auto_now_add time when its edited
    published_at=models.DateTimeField(auto_now=True)#wont show in admin/ cause it take the time by it self when the job is created
    #number of plcaes available
    vacancy=models.IntegerField(default=1)#number of person for this job
    salary=models.IntegerField(default=1)
    experience=models.IntegerField(default=1)

    def __str__(self):
        return self.title 
    #afficher le title du job (cest comme un lien pour voir les donnes de chaque job)