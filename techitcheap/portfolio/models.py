from django.db import models

CATEGORIES = [("Website Design",'Website Design'),
                  ("Product Development", 'Product Development'),
                  ("Mobile App Development", "Mobile App Development"),
                  ("Mobile App and Web Maintenance", "Mobile App and Web Maintenance")]
# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(default="Such beautiful Projects!")
    category = models.CharField(choices=CATEGORIES, default="Website Design", max_length=255, blank=True, null=True)
    image = models.FileField(blank=True, default="hj.jpg")
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date']

    # def _get_(self, instance, owner):
    #     return [opt for opt in self.categories if opt[0] in instance.category]
    
    def __str__(self):
        return self.title
