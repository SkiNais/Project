from django.shortcuts import render


def home(requests):
    return render(requests, 'website_app/home.html')

def statistic(requests):
    return render(requests, 'website_app/statistic.html')

def demand(requests):
    return render(requests, 'website_app/demand.html')

def geography(requests):
    return render(requests, 'website_app/geography.html')

def skills(requests):
    return render(requests, 'website_app/skills.html')

def last_vacancies(requests):
    return render(requests, 'website_app/last_vacancies.html')

def test(requests):
    return render(requests, 'website_app/test.html')
