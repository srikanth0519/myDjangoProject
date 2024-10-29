import os
import sys
import django
from faker import Faker

# Add the project directory to the system path
sys.path.append("D:\my_django_project\myDjangoProject")

# Setup Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myDjangoProject.settings")
django.setup()

# Import the model`
from myDjangoProject_app1.models import Student

# Populate script
fake = Faker()  # Use Faker from faker module directly

def create_students(n=50):
    for _ in range(n):
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.unique.email()
        enrollment_date = fake.date_between(start_date='-30d', end_date='today')

        Student.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            enrollment_date=enrollment_date
        )

if __name__ == '__main__':
    print("Populating the database with student data...")
    create_students(50)
    print("Database populated successfully...")
