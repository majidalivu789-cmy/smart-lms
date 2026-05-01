from django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
# -----login page authentication-----
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from Dashboard_Page.models import Quiz, Question, Option


from django.utils import timezone
from django.http import JsonResponse
import json
# ----end----
from Mycourses.models import myCourses
from Home_Page.models import Logo
from Home_Page.models import Top_Courses
from Home_Page.models import FounderMessage
from Home_Page.models import Instructor, InstructorCourse, InstructorDetail, InstructorReview
from Home_Page.models import Feature
from About_Page.models import AboutSml
from About_Page.models import AboutFeature
from About_Page.models import StudentReview
from Dashboard_Page.models import DashboardCourse
from Dashboard_Page.models import ProfileImage
from Dashboard_Page.forms import StudentForm
from Dashboard_Page.models import Updates
from Dashboard_Page.models import ImportantLinks
#Contact page 
from Contact_Page.forms import ContactForm
from Contact_Page.models import ContactMessage,MapSide
#Send email message by Contact page 
from django.core.mail import send_mail
from django.conf import settings
from django.core.paginator import Paginator
from datetime import timedelta

#Home Page
def index(request):
    Title = Logo.objects.all()
    fav_icon = Logo.objects.first()
    topCourses = Top_Courses.objects.all()
    founder_msg = FounderMessage.objects.all()
    instructor =Instructor.objects.all()
    Features = Feature.objects.all()
    data ={
        'Title':Title,
        'fav_icon' : fav_icon,
        'topCourses':topCourses,
        'founder_msg':founder_msg,
        'instructor':instructor,
        'Features': Features,
        'title' : 'Home',
    }
    return render(request, 'index.html',data)

#About Page
def about(request):
    fav_icon = Logo.objects.first()
    Title = Logo.objects.all()
    about = AboutSml.objects.all()
    features = AboutFeature.objects.all()
    reviews = StudentReview.objects.filter(is_active=True).order_by('display_order', '-created_at')
    data ={
        'fav_icon' : fav_icon,
        'Title':Title,
        'about':about,
        'features':features,
        'reviews': reviews,
        'title' : 'About',
    }
    return render(request,'about.html',data)

#courses Page
# Paginator 
from django.core.paginator import Paginator
def courses(request):
    fav_icon = Logo.objects.first()
    Title = Logo.objects.all()
    courseData = myCourses.objects.all().order_by('id') 
    paginator = Paginator(courseData,8)
    page_number = request.GET.get('page')
    courseDataFinal = paginator.get_page(page_number)

    if request.method == 'GET':
        des = request.GET.get('c_title')
    if des != None:
      courseDataFinal  = myCourses.objects.filter(course_des__icontains = des).order_by('id')

    data = {
        'fav_icon' : fav_icon,
        'courseData':courseDataFinal,
        'Title':Title,
        'title' : 'Courses',
        
    }
    return render(request,'courses.html',data)


def top_course_detail(request, course_id):
    fav_icon = Logo.objects.first()
    Title = Logo.objects.all()
    course = get_object_or_404(Top_Courses.objects.select_related('instructor', 'instructor__detail'), id=course_id)
    data = {
        'fav_icon': fav_icon,
        'Title': Title,
        'course': course,
        'course_source': 'top',
        'back_url': '/',
        'title': course.course_title,
        'outline': [item.strip() for item in course.course_outline.splitlines() if item.strip()],
        'outcomes': [item.strip() for item in course.course_outcomes.splitlines() if item.strip()],
        'requirements': [item.strip() for item in course.course_requirements.splitlines() if item.strip()],
        'projects': [item.strip() for item in course.course_projects.splitlines() if item.strip()],
    }
    return render(request, 'public_course_detail.html', data)


def public_course_detail(request, course_id):
    fav_icon = Logo.objects.first()
    Title = Logo.objects.all()
    course = get_object_or_404(myCourses.objects.select_related('instructor', 'instructor__detail'), id=course_id)
    data = {
        'fav_icon': fav_icon,
        'Title': Title,
        'course': course,
        'course_source': 'public',
        'back_url': '/courses/',
        'title': course.course_title,
        'outline': [item.strip() for item in course.course_outline.splitlines() if item.strip()],
        'outcomes': [item.strip() for item in course.course_outcomes.splitlines() if item.strip()],
        'requirements': [item.strip() for item in course.course_requirements.splitlines() if item.strip()],
        'projects': [item.strip() for item in course.course_projects.splitlines() if item.strip()],
    }
    return render(request, 'public_course_detail.html', data)

#contact Page
def contacts(request):
    fav_icon = Logo.objects.first()
    map_side = MapSide.objects.all()
    form = ContactForm()
    contact =''
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
           contact = form.save()
           send_mail(
               'Thanks for contancting us',
               'We have received your message. Our team will reply soon.',
                settings.DEFAULT_FROM_EMAIL,
                [contact.email],
                fail_silently=False,
           )
           messages.success(request, "Message Sent Successfuly!")
           return redirect('/contact/') 
        else:
            form = ContactForm()
            messages.error(request,"Message is Invalid!")

            return render(request,'contact.html')

    Title = Logo.objects.all()
    data ={
        'fav_icon' : fav_icon,
        'Title':Title,
        'form':form,
        'map_side' : map_side,
        'title' : 'Contact Us',
    }
    return render(request,'contact.html',data)



# Signup View
@never_cache
@csrf_protect
def signup_view(request):
    fname = ''
    email = ''
    if request.method == 'POST':
        full_name = (request.POST.get('fname') or '').strip()
        email = (request.POST.get('email2') or '').strip().lower()
        password = request.POST.get('password2')
        confirm_password = request.POST.get('confirm_password')
        fname = full_name or ''

        if not full_name:
            messages.error(request, "Full name is required.")
        elif not email:
            messages.error(request, "Email is required.")
        elif User.objects.filter(username=email).exists():
            messages.error(request, "Email already registered!")
        elif not password:
            messages.error(request, "Password is required.")
        elif password != confirm_password:
            messages.error(request, "Passwords do not match.")
        else:
            try:
                validate_password(password)
            except ValidationError as err:
                messages.error(request, " ".join(err.messages))
            else:
                user = User.objects.create_user(
                    username=email.lower(),
                    email=email.lower(),
                    first_name=full_name.strip(),
                    password=password
                )
                user.save()
                messages.success(request, "Signup successful! Please login.")
                return redirect('login')

    return render(request, 'signUp.html', {'fname': fname, 'email': email})
    
# Login View
@never_cache
@csrf_protect
def login_view(request):
    email = ''
    if request.method == 'POST':
        email = (request.POST.get('email') or '').strip().lower()
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect('/dashboard/')  # redirect to welcome or home page
        else:
            messages.error(request, 'Invalid email or password!')
    response = render(request, 'login.html', {'email': email})
    response['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    return response
    # return render(request, 'login.html',{'email':email,'password':password})


@never_cache
@csrf_protect
def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, "You have been logged out.")
    return redirect('login')
# Payment information
from django.contrib.auth.decorators import login_required
def enrollnow(request):
    return render(request,'enrollNow.html')

#Dashboard 
@login_required
def dashboard(request):
    
    profile = ProfileImage.objects.first()

    enrollments = Enrollment.objects.filter(
        user=request.user,
        is_paid=True
    )

    return render(request, 'dashboard.html', {
        'profile': profile,
        'enrollments': enrollments
    })

# profile
def profile(request):
    # ======Profile image start=====
    profile = ProfileImage.objects.first()
    if not profile:
        profile = ProfileImage.objects.create() 

    if request.method == 'POST' and 'photo' in request.FILES:
        profile.photo = request.FILES['photo'] 
        profile.save()
        return redirect("profile_page")
        #=====Profile Image End ======

    #===========Student Form Start=======
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile')
        else:
            form = StudentForm()    

    return render(request, 'profile.html',{'profile':profile,'form':form})


#Dashboard Courses
@login_required
def mycourses(request):
    # show image on navbar
    profile = ProfileImage.objects.first()
    myCourses = DashboardCourse.objects.all()

    # YAHAN CHANGE HAI: Sirf wo IDs nikalni hain jinki payment ho chuki hai
    enrolled_ids = Enrollment.objects.filter(
        user=request.user,
        is_paid=True  # Sirf paid courses Already Enrolled dikhayenge
    ).values_list('course_id', flat=True)

    if request.method == 'GET':
        title = request.GET.get('c_title')
        if title:
            myCourses = DashboardCourse.objects.filter(
                course_title__icontains=title
            )

    return render(request, 'mycourses.html', {
        'myCourses': myCourses,
        'profile': profile,
        'enrolled_ids': enrolled_ids
    })

#Dashboard important links
def links(request):
    #show image on navbar
    profile = ProfileImage.objects.first() 
    links = ImportantLinks.objects.all().order_by('-created_at')
    return render(request, 'important_link.html',{'profile':profile,'links' : links})

from Dashboard_Page.models import VideoProgress, Enrollment, CourseLecture


from Dashboard_Page.models import QuizResult
# --- Is block ko copy karein aur apne views.py mein replace karein ---
from django.utils import timezone

@login_required
def quiz(request):
    profile = ProfileImage.objects.first()
    now = timezone.now()
    
    # 1. Student ke tamam enrolled courses ki list nikalo
    enrolled_course_ids = Enrollment.objects.filter(
        user=request.user
    ).values_list('course_id', flat=True).distinct()
    
    # 2. Sirf unhi enrolled courses ke quizzes uthao (expired bhi show hon, but disabled)
    quizzes = Quiz.objects.filter(
        course_id__in=enrolled_course_ids
    ).select_related('course').order_by('course_id', 'id')

    done_quiz_ids = set(
        QuizResult.objects.filter(user=request.user).values_list('quiz_id', flat=True)
    )

    for q in quizzes:
        q.already_done = q.id in done_quiz_ids
        q.not_started = bool(q.start_date and q.start_date > now)
        q.is_expired = bool(q.expiry_date and q.expiry_date <= now)
        q.is_disabled = q.already_done or q.not_started or q.is_expired

    return render(request, 'quiz.html', {'profile': profile, 'quizzes': quizzes})

@login_required
def save_quiz_result(request):
    if request.method == "POST":
        data = json.loads(request.body)
        QuizResult.objects.create(
            user=request.user,
            quiz_id=data['quiz_id'],
            score=data['score'],
            total=data['total']
        )
        return JsonResponse({"status": "success"})

# ------ Quiz App -----

# Quiz App Page
def quiz_app(request, id):
    profile = ProfileImage.objects.first()
    quiz = get_object_or_404(Quiz, id=id)
    questions = Question.objects.filter(quiz=quiz)

    data = []

    for q in questions:
        options = Option.objects.filter(question=q)
        opts = []
        correct = ""

        for o in options:
            opts.append(o.option_text)
            if o.is_correct:
                correct = o.option_text

        data.append({
            "question": q.question_text,
            "options": opts,
            "correctAnswer": correct
        })

    return render(request, 'quizApp.html', {
        'quiz': quiz,
        'quiz_data': data,
        'quiz_time': quiz.time,  # 👈 ADD THIS
        'profile':profile,
    })



# ---Dashboard News and Events---
def newsEvents(request):
    #show image on navbar
    profile = ProfileImage.objects.first() 
    # Updates here 
    updates = Updates.objects.all().order_by('updation_date')
    return render(request, 'news_and_events.html',{'profile':profile,'updates':updates})


#Dashboard Video page

# def video_page(request,course_id):
#     #show image on navbar
#     course = get_object_or_404(DashboardCourse, id=course_id)

#     if not Enrollment.objects.filter(
#         user=request.user,
#         course=course,
#         is_paid=True
#     ).exists():
#         return redirect('mycourses')

#     course = DashboardCourse.objects.prefetch_related(
#         'weeks__lectures'
#     ).get(id=course_id)

#     profile = ProfileImage.objects.first()
#     return render(request, 'video_page.html', {
#         'profile': profile,
#         'course': course
#     })

@login_required
def video_page(request, course_id):
    # Get course or 404
    course = get_object_or_404(DashboardCourse, id=course_id)

    # Enrollment check
    if not Enrollment.objects.filter(
        user=request.user,
        course=course,
        is_paid=True
    ).exists():
        return redirect('mycourses')

    # Prefetch lectures for optimization
    course = DashboardCourse.objects.prefetch_related(
        'weeks__lectures'
    ).get(id=course_id)

    # --- NEW LOGIC: Get IDs of all lectures watched by this user in this course ---
    watched_lecture_ids = VideoProgress.objects.filter(
        user=request.user,
        lecture__week__course=course,
        watched=True
    ).values_list('lecture_id', flat=True)

    profile = ProfileImage.objects.first()
    
    return render(request, 'video_page.html', {
        'profile': profile,
        'course': course,
        'watched_lecture_ids': list(watched_lecture_ids) # Passed as list to template
    })


from Dashboard_Page.models import Enrollment
@login_required
def enroll_course(request, course_id):
    course = get_object_or_404(DashboardCourse, id=course_id)

    enrollment, created = Enrollment.objects.get_or_create(
        user=request.user,
        course=course
    )
    # agr already paid hy to dobara payment page na jaye
    if enrollment.is_paid:
        return redirect ('dashboard')

    return redirect('fees_page', enrollment_id=enrollment.id)





# ===========Fees Page==========
@login_required
def fees_page(request, enrollment_id):
    enrollment = get_object_or_404(
        Enrollment,
        id=enrollment_id,
        user=request.user
    )

    if request.method == "POST":
        enrollment.is_paid = True   # demo payment
        enrollment.save()
        return redirect('dashboard')

    return render(request, 'fees.html', {
        'enrollment': enrollment
    })

# ----- Course Deatials Page ------
@login_required
def course_detail (request, course_id):
    course = get_object_or_404(DashboardCourse.objects.select_related('instructor', 'instructor__detail'), id = course_id)

    enrollment = Enrollment.objects.filter(
        user = request.user,
        course = course
    ).first()

    data = {
        'course': course,
        'enrollment': enrollment,
        'outline': [item.strip() for item in course.course_outline.splitlines() if item.strip()],
        'outcomes': [item.strip() for item in course.course_outcomes.splitlines() if item.strip()],
        'requirements': [item.strip() for item in course.course_requirements.splitlines() if item.strip()],
        'projects': [item.strip() for item in course.course_projects.splitlines() if item.strip()],
    }
    return render(request, 'course_detail.html', data)


# --------- Dynamic Video page -------
from django.http import JsonResponse
from Dashboard_Page.models import VideoProgress, CourseLecture

from Dashboard_Page.models import DailyLearning


@login_required
def progress(request):
    profile = ProfileImage.objects.first()
    enrollments = Enrollment.objects.filter(user=request.user, is_paid=True)

    # --- 1. QUIZ DATA ---
    quiz_results = QuizResult.objects.filter(user=request.user)
    unique_quizzes_done = quiz_results.values('quiz').distinct().count()
    scores_list = [(r.score / r.total * 100) for r in quiz_results if r.total > 0]
    avg_score = int(sum(scores_list) / len(scores_list)) if scores_list else 0
    highest = int(max(scores_list)) if scores_list else 0
    lowest = int(min(scores_list)) if scores_list else 0

    # --- 2. VIDEO PROGRESS LOGIC ---
    course_progress = []
    total_videos_all = 0
    watched_videos_all = 0

    for enroll in enrollments:
        course = enroll.course
        lectures = CourseLecture.objects.filter(week__course=course)
        total_v = lectures.count()
        watched_v = VideoProgress.objects.filter(user=request.user, lecture__in=lectures, watched=True).count()
        percent = int((watched_v / total_v) * 100) if total_v > 0 else 0
        total_videos_all += total_v
        watched_videos_all += watched_v
        course_progress.append({'course': course, 'total': total_v, 'watched': watched_v, 'percent': percent})

    # --- 3. OVERALL PROGRESS ---
    total_system_quizzes = Quiz.objects.count()
    total_items = total_videos_all + total_system_quizzes
    completed_items = watched_videos_all + unique_quizzes_done
    progress_percent = min(int((completed_items / total_items) * 100), 100) if total_items > 0 else 0

    # --- 4. NEW: WEEKLY CHART DYNAMIC LOGIC ---
    today = timezone.now().date()
    week_data = []
    start_of_week = today - timedelta(days=today.weekday()) # Monday se start
    
    for i in range(7):
        day_date = start_of_week + timedelta(days=i)
        day_name = day_date.strftime('%a')
        entry = DailyLearning.objects.filter(user=request.user, date=day_date).first()
        hrs = entry.hours if entry else 0
        # Height calculate karein (Max 8 hours k hisab se percentage)
        h_percent = min(int((hrs / 8) * 100), 100)
        week_data.append({'day': day_name, 'hours': hrs, 'height': h_percent})

    context = {
        'profile': profile,
        'course_progress': course_progress,
        'progress_percent': progress_percent,
        'total_quizzes': unique_quizzes_done, 
        'avg_score': avg_score,
        'highest': highest,
        'lowest': lowest,
        'total_courses': enrollments.count(),
        'enrollments': enrollments,
        'week_data': week_data # Ye naya variable chart k liye
    }
    return render(request, 'progress.html', context)

@login_required
def save_progress(request):
    if request.method == "POST":
        lecture_id = request.POST.get('lecture_id')
        lecture = CourseLecture.objects.get(id=lecture_id)

        progress, created = VideoProgress.objects.get_or_create(user=request.user, lecture=lecture)

        if not progress.watched:
            progress.watched = True
            progress.save()
            # --- NEW: Daily hours update ---
            day_rec, _ = DailyLearning.objects.get_or_create(user=request.user, date=timezone.now().date())
            day_rec.hours += 0.5 # Aik video dekhne par 0.5 hours add honge
            day_rec.save()

        return JsonResponse({'status': 'saved'})

def instructor(request, id):
    instructor_single = get_object_or_404(Instructor, id = id)
    detail = InstructorDetail.objects.filter(instructor=instructor_single).first()
    courses = InstructorCourse.objects.filter(instructor=instructor_single)
    reviews = InstructorReview.objects.filter(instructor=instructor_single, is_active=True)
    skills = []
    projects = []
    qualifications = []

    if detail:
        if detail.skills:
            skills = [skill.strip() for skill in detail.skills.split(',') if skill.strip()]

        if detail.project_title_1:
            projects.append({
                'title': detail.project_title_1,
                'description': detail.project_des_1,
                'link': detail.project_link_1,
            })
        if detail.project_title_2:
            projects.append({
                'title': detail.project_title_2,
                'description': detail.project_des_2,
                'link': detail.project_link_2,
            })

        if detail.qualification_1:
            qualifications.append({
                'name': detail.qualification_1,
                'from': detail.qualification_from_1,
            })
        if detail.qualification_2:
            qualifications.append({
                'name': detail.qualification_2,
                'from': detail.qualification_from_2,
            })

    Title = Logo.objects.all()
    fav_icon = Logo.objects.first()
    data = {
        'fav_icon' : fav_icon,
        'Title':Title,
        'title' : 'Instructors',
        'ins' : instructor_single,
        'detail': detail,
        'skills': skills,
        'projects': projects,
        'qualifications': qualifications,
        'courses': courses,
        'reviews': reviews,
    }
    return render(request, 'instructor_detail.html',data)
