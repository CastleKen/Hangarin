from django.core.management.base import BaseCommand
from django.utils import timezone
from faker import Faker
from hmodels.models import Priority, Category, Task, Note, SubTask

class Command(BaseCommand):
    help = 'Create initial data for the application'

    def handle(self, *args, **kwargs):
        self.create_priorities(10)
        self.create_categories(10)
        self.create_task(10)
        self.create_note(10)
        self.create_sub_task(10)

    def create_priorities(self):
        priorities = ["High", "Medium", "Low", "Critical", "Optional"]
        for p in priorities:
            Priority.objects.get_or_create(priority_name=p)

    def create_categories(self):
        categories = ["Work", "School", "Personal", "Finance", "Projects"]
        for c in categories:
            Category.objects.get_or_create(category_name=c)

    def create_task(self, count):
        categories = list(Category.objects.all())
        priorities = list(Priority.objects.all())

        if not categories or not priorities:
            self.stdout.write(self.style.ERROR("Still no categories or priorities!"))
            return
        
        fake = Faker()
        for _ in range(count):
            Task.objects.create(
                task_title = [fake.sentence(nb_words=5)],
                task_description = [fake.paragraph(nb_sentences=3)],
                task_deadline = timezone.make_aware(fake.date_time_this_month()),
                task_status = [fake.random_element(elements=["Pending", "In Progress", "Completed"])]
            )
            
    def create_note(self, count):
        fake = Faker()
        for _ in range(count):
            Note.objects.create(
                note_content = [fake.paragraph(nb_sentences=3)]
            )

    def create_sub_task(self, count):
        fake = Faker()
        for _ in range(count):
            SubTask.objects.create(
                sub_title = [fake.sentence(nb_words=5)],
                sub_status = [fake.random_element(elements=["Pending", "In Progress", "Completed"])]
            )
            