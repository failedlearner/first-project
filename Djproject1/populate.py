import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE','Djproject1.settings')

django.setup()


from testapp.models import *
from faker import Faker
from random import *
fake=Faker()
def phonenumbergen():
    d1=randint(7,9)
    num=''+str(d1)
    for i in range(9):
        num=num+str(randint(0,9))
    return int(num)


def populatehyd(n):
    for i in range(n):
        fdate=fake.date()
        fcompany=fake.company()
        ftitle=fake.random_element(elements=('Project Manager','Team Lead','Software Engineer'))
        feligibility=fake.random_element(elements=('B.Tech','M.Tech','MCA','PhD'))
        faddress=fake.address()
        femail=fake.email()
        fphnonenumber=phonenumbergen()
        hydjobs_record=hydjobs.objects.get_or_create(date=fdate, company=fcompany,
        title=ftitle, eligibility=feligibility, address=faddress,email=femail,phonenumber=fphnonenumber)
def populatepune(n):
    for i in range(n):
        fdate=fake.date()
        fcompany=fake.company()
        ftitle=fake.random_element(elements=('Project Manager','Team Lead','Software Engineer'))
        feligibility=fake.random_element(elements=('B.Tech','M.Tech','MCA','PhD'))
        faddress=fake.address()
        femail=fake.email()
        fphnonenumber=phonenumbergen()
        punejobs_record=punejobs.objects.get_or_create(date=fdate, company=fcompany,
        title=ftitle, eligibility=feligibility, address=faddress,email=femail,phonenumber=fphnonenumber)

def populateChennai(n):
    for i in range(n):
        fdate=fake.date()
        fcompany=fake.company()
        ftitle=fake.random_element(elements=('Project Manager','Team Lead','Software Engineer'))
        feligibility=fake.random_element(elements=('B.Tech','M.Tech','MCA','PhD'))
        faddress=fake.address()
        femail=fake.email()
        fphnonenumber=phonenumbergen()
        chennaijobs_record=chennaijobs.objects.get_or_create(date=fdate, company=fcompany,
        title=ftitle, eligibility=feligibility, address=faddress,email=femail,phonenumber=fphnonenumber)

def populateBLR(n):
    for i in range(n):
        fdate=fake.date()
        fcompany=fake.company()
        ftitle=fake.random_element(elements=('Project Manager','Team Lead','Software Engineer'))
        feligibility=fake.random_element(elements=('B.Tech','M.Tech','MCA','PhD'))
        faddress=fake.address()
        femail=fake.email()
        fphnonenumber=phonenumbergen()
        blrjobs_record=blorejobs.objects.get_or_create(date=fdate, company=fcompany,
        title=ftitle, eligibility=feligibility, address=faddress,email=femail,phonenumber=fphnonenumber)
populatepune(50)
populateBLR(50)
populateChennai(50)
populatehyd(25)
