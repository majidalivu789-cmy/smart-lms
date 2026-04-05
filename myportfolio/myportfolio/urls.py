from django.contrib import admin
from django.urls import path
from myportfolio import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name='index'),
    path('about/',views.about),
    path('courses/',views.courses),
    path('login/',views.login_view,name='login'),
    path('signup/',views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path(
        'forgot-password/',
        auth_views.PasswordResetView.as_view(
            template_name='password_reset_form.html',
            email_template_name='password_reset_email.html',
            subject_template_name='password_reset_subject.txt',
            success_url='/forgot-password/done/'
        ),
        name='password_reset'
    ),
    path(
        'forgot-password/done/',
        auth_views.PasswordResetDoneView.as_view(
            template_name='password_reset_done.html'
        ),
        name='password_reset_done'
    ),
    path(
        'reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='password_reset_confirm.html',
            success_url='/reset/done/'
        ),
        name='password_reset_confirm'
    ),
    path(
        'reset/done/',
        auth_views.PasswordResetCompleteView.as_view(
            template_name='password_reset_complete.html'
        ),
        name='password_reset_complete'
    ),
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
