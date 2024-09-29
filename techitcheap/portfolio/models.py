from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    categories = [("Website Design",'option1'),
                  ("Product Development", 'option2'),
                  ("Graphics Design", 'option3'),]
    category = models.CharField(max_length=255, choices=categories, blank=True, null=True)
    image = models.FileField(blank=True)
    date = models.DateTimeField(auto_now_add=True)

    # def _get_(self, instance, owner):
    #     return [opt for opt in self.categories if opt[0] in instance.category]
    
    def __str__(self):
        return self.title
