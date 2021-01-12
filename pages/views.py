from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from blog.models import *
from .models import *
from comments.models import *

def index(request):
    homeactive = 'active'
    allServices = ServiceName.objects.all().order_by('order')
    servicesAtHome = allServices.filter(isAtHome=True)
    servicesInCalc = allServices.filter(isInCalc=True)
    allComments = Comment.objects.all()
    num = range(25)
    canonical_url = ''

    try:
        seotag = SeoTag.objects.first()
        pageTitle = seotag.indexTitle
        pageDescription = seotag.indexDescription
        pageKeywords = seotag.indexKeywords
    except:
        pageTitle = 'НЕ ЗАПОЛНЕНА ТАБЛИЦА СЕО ТЕГИ'
        pageDescription = 'НЕ ЗАПОЛНЕНА ТАБЛИЦА СЕО ТЕГИ'
        pageKeywords = 'НЕ ЗАПОЛНЕНА ТАБЛИЦА СЕО ТЕГИ'
    return render(request, 'pages/index.html', locals())

def allPosts(request):
    postactive = 'active'
    canonical_url = 'posts/'
    try:
        seotag = SeoTag.objects.first()
        pageTitle = seotag.postsTitle
        pageDescription = seotag.postsDescription
        pageKeywords = seotag.postsKeywords
    except:
        pageTitle = 'НЕ ЗАПОЛНЕНА ТАБЛИЦА СЕО ТЕГИ'
        pageDescription = 'НЕ ЗАПОЛНЕНА ТАБЛИЦА СЕО ТЕГИ'
        pageKeywords = 'НЕ ЗАПОЛНЕНА ТАБЛИЦА СЕО ТЕГИ'
    allPost = BlogPost.objects.filter(is_active=True)
    return render(request, 'pages/posts.html', locals())

def showPost(request,slug):
    canonical_url = request.get_full_path()
    postactive = 'active'
    post = get_object_or_404(BlogPost, name_slug=slug)
    pageTitle = post.page_title
    pageDescription = post.page_description
    pageKeywords = post.page_keywords
    canonical_url = f'posts/{post.name_slug}/'
    return render(request, 'pages/post.html', locals())

def about(request):
    canonical_url = 'about/'
    aboutactive = 'active'
    allServices = ServiceName.objects.all().order_by('order')
    servicesInCalc = allServices.filter(isInCalc=True)
    try:
        seotag = SeoTag.objects.first()
        pageTitle = seotag.aboutTitle
        pageDescription = seotag.aboutDescription
        pageKeywords = seotag.aboutKeywords
    except:
        pageTitle = 'НЕ ЗАПОЛНЕНА ТАБЛИЦА СЕО ТЕГИ'
        pageDescription = 'НЕ ЗАПОЛНЕНА ТАБЛИЦА СЕО ТЕГИ'
        pageKeywords = 'НЕ ЗАПОЛНЕНА ТАБЛИЦА СЕО ТЕГИ'
    return render(request, 'pages/about.html', locals())


def policy(request):
    return render(request, 'pages/policy.html', locals())


def services(request):
    canonical_url = 'service/'
    servicesactive = 'active'
    try:
        seotag = SeoTag.objects.first()
        pageTitle = seotag.servicesTitle
        pageDescription = seotag.servicesDescription
        pageKeywords = seotag.servicesKeywords
    except:
        pageTitle = 'НЕ ЗАПОЛНЕНА ТАБЛИЦА СЕО ТЕГИ'
        pageDescription = 'НЕ ЗАПОЛНЕНА ТАБЛИЦА СЕО ТЕГИ'
        pageKeywords = 'НЕ ЗАПОЛНЕНА ТАБЛИЦА СЕО ТЕГИ'
    allServices = ServiceName.objects.all().order_by('order')
    servicesInCalc = allServices.filter(isInCalc=True)
    return render(request, 'pages/services.html', locals())


def contacts(request):
    canonical_url = 'contacts/'
    contactsactive = 'active'
    allServices = ServiceName.objects.all().order_by('order')

    try:
        seotag = SeoTag.objects.first()
        pageTitle = seotag.contactTitle
        pageDescription = seotag.contactDescription
        pageKeywords = seotag.contactKeywords
    except:
        pageTitle = 'НЕ ЗАПОЛНЕНА ТАБЛИЦА СЕО ТЕГИ'
        pageDescription = 'НЕ ЗАПОЛНЕНА ТАБЛИЦА СЕО ТЕГИ'
        pageKeywords = 'НЕ ЗАПОЛНЕНА ТАБЛИЦА СЕО ТЕГИ'
    return render(request, 'pages/contacts.html', locals())


def service(request, slug):
    is_service_page = True
    servicesactive = 'active'
    currentService = get_object_or_404(ServiceName, name_slug=slug)
    current_Service = currentService.name
    allServices = ServiceName.objects.all().order_by('order')
    servicesInCalc = allServices.filter(isInCalc=True)
    all_steps = ServiceSteps.objects.filter(service=currentService)
    pageTitle = currentService.page_title
    pageDescription = currentService.page_description
    service_Description = f'В нашей компании вы можете заказать услуги по {current_Service.lower()} квартир и офисов по низким ценам. Быстрая и качественная {current_Service.lower()} помещений. ☎️ Звоните: +7 (351) 777-20-03.'
    pageKeywords = currentService.page_keywords
    allComments = Comment.objects.filter(service=currentService)
    allVideoComments = VideoComment.objects.filter(service=currentService)
    canonical_url = f'service/{currentService.name_slug}/'
    return render(request, 'pages/service.html', locals())


def robots(request):
    robotsTxt = """User-agent: *
Disallow:/admin/
Disallow:/media/
Disallow:/static/
Disallow:/mc/
Disallow:/*?*id=

Allow: /*.jpg
Allow: /*.jpeg
Allow: /*.png
Allow: /*.gif
Allow: /*.css
Allow: /*.js
Allow: /*.webp

Sitemap: https://www.misterclean.ru/sitemap.xml 
    """
    return HttpResponse(robotsTxt, content_type="text/plain")


def customhandler404(request, exception, template_name='404.html'):
    allServices = ServiceName.objects.all().order_by('order')
    is404 = True


    pageTitle = '404 - Такой страницы не существует'


    return render(request, 'pages/404.html', locals(),None,status=404)