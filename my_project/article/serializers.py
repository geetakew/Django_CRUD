from rest_framework import serializers
from .models import Article
from article.validators import StringValidator, IntegerValidator


class ArticleSerializer(serializers.Serializer):
    class Meta:
        model = Article
        fields = '__all__'
    title = serializers.CharField(max_length=120, validators=[StringValidator()])
    description = serializers.CharField(validators=[StringValidator()])
    body = serializers.CharField(validators=[StringValidator()])
    author_id = serializers.IntegerField(validators=[IntegerValidator()])
    # age = serializers.IntegerField(validators=[AgeValidator(at_least=21)])

    def create(self, validated_data):
        return Article.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.body = validated_data.get('body', instance.body)
        instance.author_id = validated_data.get('author_id', instance.author_id)

        instance.save()
        return instance
