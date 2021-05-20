from rest_framework import serializers
from App.models import Article

'''ModelSerializer'''
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        #fields = ('id', 'title', 'author')
        fields = '__all__'



''' Serializer '''
# class ArticleSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=100)
#     author = serializers.CharField(max_length=100)
#     email = serializers.EmailField(max_length=100)
#     date = serializers.DateTimeField()
#
#     def create(self, validated_data):
#         return Article.objects.create(validated_data)
#
#     def update(self, instance, validate_data):
#         instance.title = validate_data.get('title', instance.title)
#         instance.author = validate_data.get('author', instance.author)
#         instance.email = validate_data.get('email', instance.email)
#         instance.date = validate_data.get('date', instance.date)
#         instance.save()
#         return instance