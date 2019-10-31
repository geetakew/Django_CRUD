from rest_framework import serializers
# from article.serializers import ArticleSerializer


# class AgeValidator(object):
#
#   def __init__(self, at_least):
#     self.at_least = at_least
#
#   def __call__(self, value):
#     if value < self.at_least:
#       raise serializers.ValidationError('Must be {} to view!'.format(self.at_least))
#     return value


class StringValidator(object):
    def __call__(self, value):
        try:
            int_value = int(value)
        except Exception:
            return value
        if type(int_value) is int:
            raise serializers.ValidationError("Field must be string")


class IntegerValidator(object):
    def __call__(self, value):
        try:
            int_value = int(value)
        except Exception:
            raise serializers.ValidationError("Field must be integer")
        if type(int_value) is int:
            return value
