from rest_framework import serializers
from .models import Project, CATEGORIES


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ["id", "title", "description", "category", "image"]
    # id = serializers.IntegerField(read_only=True)
    # title = serializers.CharField(max_length=100)
    # description = serializers.CharField(style={'base_template':'textarea.html'}, default="Such beautiful Projects!") 
    # category = serializers.ChoiceField(choices=CATEGORIES, default="Website Design")
    # image = serializers.FileField(required=False,  default="hj.jpg")
    # # date = serializers.DateTimeField(auto_now_add=True)

    # def create(self, validated_data):
    #     return Project.objects.create(**validated_data)

