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
    postactive = 'active'
    post = get_object_or_404(BlogPost, name_slug=slug)
    pageTitle = post.page_title
    pageDescription = post.page_description
    pageKeywords = post.page_keywords
    return render(request, 'pages/post.html', locals())

def about(request):
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
    contactsactive = 'active'

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
    servicesactive = 'active'
    currentService = get_object_or_404(ServiceName, name_slug=slug)
    allServices = ServiceName.objects.all().order_by('order')
    servicesInCalc = allServices.filter(isInCalc=True)
    all_steps = ServiceSteps.objects.filter(service=currentService)
    pageTitle = currentService.page_title
    pageDescription = currentService.page_description
    pageKeywords = currentService.page_keywords
    allComments = Comment.objects.filter(service=currentService)
    allVideoComments = VideoComment.objects.filter(service=currentService)
    return render(request, 'pages/service.html', locals())


def robots(request):
    robotsTxt = f"User-agent: *\nDisallow: /admin/\nHost: https://www.misterclean.ru/\nSitemap: https://www.misterclean.ru/sitemap.xml"
    return HttpResponse(robotsTxt, content_type="text/plain")