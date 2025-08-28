from django.db import models

# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Priority(BaseModel):
    priority_name = models.CharField(max_length=150)

    def __str__(self):
        return self.priority_name
    
class Category(BaseModel):
    category_name = models.CharField(max_length=150)

    def __str__(self):
        return self.category_name
    
class Task(BaseModel):
    task_title = models.CharField(max_length=150)
    task_description = models.CharField(max_length=500)
    task_deadline = models.DateField(null=True, blank=True)
    task_status = models.CharField(
        max_length=50,
        choices=[
            ("Pending", "Pending"),
            ("In Progress ", "In Progress"),
            ("Completed", "Completed"),
        ],
        default="Pending"
    )
    task_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    task_priority = models.ForeignKey(Priority, on_delete=models.CASCADE)

    def __str__(self):
        return self.task_title


class Note(BaseModel):
    note_task = models.ForeignKey(Task, on_delete=models.CASCADE)
    note_content = models.CharField(max_length=150)

    def __str__(self):
        return self.note_content

class SubTask(BaseModel):
    sub_parent_task = models.ForeignKey(Task, on_delete=models.CASCADE)
    sub_title = models.CharField(max_length=150)
    sub_status = models.CharField(
        max_length=50,
        choices=[
            ("Pending", "Pending"),
            ("In Progress ", "In Progress"),
            ("Completed", "Completed"),
        ],
        default="Pending"
    )

    def __str__(self):
        return self.sub_title