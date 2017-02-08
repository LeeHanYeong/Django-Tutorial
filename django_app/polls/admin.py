from django.contrib import admin

from .models import Question, Choice

admin.site.register(Question)
admin.site.register(Choice)

"""
Django shell을 이용해서
임의의 Question객체 하나에 해당하는
Choice를 2개 이상 만들어준다
"""