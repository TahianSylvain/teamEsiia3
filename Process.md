time_zone: UTC+2
    Afrika/Madagascar == 'Asia/Qatar' 

pip: 
    redis
    django-celery-results-2.1.0
    django-celery-beat-2.2.0

download & install @github:
    redis

INSTALLED_APPS: 
    'django_celery_results'
    'django_celery_beat'

run:
    runserver 
    celery -A django_celery_project.celery worker --pool=solo -l info
    celery -A django_celery_project beat -l INFO