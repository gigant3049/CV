from django.shortcuts import render

from main.models import AboutMe, Partners, Education, Experience, Skills, Awards, Services, Projects, Achievements
from articles.models import Article


def index(request):
    aboutme = AboutMe.objects.get()
    partners = Partners.objects.all()
    education = Education.objects.all()
    experience = Experience.objects.all()
    skills = Skills.objects.all()
    awards = Awards.objects.all()
    services = Services.objects.all()
    projects = Projects.objects.all()
    achivements = Achievements.objects.all()
    articles = Article.objects.all()

    ctx = {
        'object': aboutme,
        'partners': partners,
        'education': education,
        'experience': experience,
        'skills': skills,
        'awards': awards,
        'services': services,
        'projects': projects,
        'achievements': achivements,
        'articles': articles
    }
    return render(request, 'index.html', ctx)
