from django.contrib import admin
from Home_Page.models import Logo
from Home_Page.models import FounderMessage
from Home_Page.models import Feature
from Home_Page.models import Instructor
from Home_Page.models import Top_Courses
# Register your models here.
admin.site.register(Logo)
admin.site.register(FounderMessage)
admin.site.register(Feature)
admin.site.register(Instructor)
admin.site.register(Top_Courses)