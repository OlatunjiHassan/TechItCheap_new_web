from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    categories = [("Website Design",'Website Design'),
                  ("Product Development", 'Product Development'),
                  ("Mobile App Development", "Mobile App Development"),
                  ("Mobile App and Web Maintenance", "Mobile App and Web Maintenance")]
    category = models.CharField(max_length=255, choices=categories, blank=True, null=True)
    image = models.FileField(blank=True)
    date = models.DateTimeField(auto_now_add=True)

    # def _get_(self, instance, owner):
    #     return [opt for opt in self.categories if opt[0] in instance.category]
    
    def __str__(self):
        return self.title
