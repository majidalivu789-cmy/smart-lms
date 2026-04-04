from django.contrib import admin
from django.urls import path
from myportfolio import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name='index'),
    path('about/',views.about),
    path('courses/',views.courses),
    path('login/',views.login_view,name='login'),
    path('signup/',views.signup_view),
    path('contact/',views.contacts),
    path('enrollnow/',views.enrollnow),
    path('dashboard/',views.dashboard, name = 'dashboard'),
    path('profile/',views.profile,name='profile_page'),
    path('mycourses/', views.mycourses,name = 'mycourses'),        #Dashboard Courses
    #Dashboard Quiz  Details Page
    path('quiz-detail/', views.quiz),
    path('quiz-app/<int:id>/', views.quiz_app),
    # urls.py mein ye line add karein
    path('save-quiz-result/', views.save_quiz_result, name='save_quiz_result'),
    
    path('links/', views.links),            #Dashboard myNotes
    path('news-events/',views.newsEvents),
    path('progress/',views.progress),           #Dashboard progress
    path('videos/', views.video_page),          #Dashboard video page
    path('course/<int:course_id>/videos/', views.video_page, name='video_page'),
    path('enroll/<int:course_id>/', views.enroll_course, name='enroll_course'),
    path('fees/<int:enrollment_id>/', views.fees_page, name='fees_page'),
    # Confirmation page
    path('course/<int:course_id>/', views.course_detail, name='course_detail'),
    # dynamic vidoe page 
    path('save-progress/', views.save_progress, name='save_progress'),
   
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
