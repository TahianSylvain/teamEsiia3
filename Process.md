

time_zone: UTC+2
    Afrika/Madagascar == 'Asia/Qatar' 
load css: 
    python manage.py collectstatic
pip: 
    redis
    
    markdown3.0
    django-filter
    django-guardian


    django-celery-results-2.1.0
    django-celery-beat-2.2.0

download & install @github:
    redis at https://redis.io/download/

INSTALLED_APPS: 
    'django_celery_results'
    'django_celery_beat'

run:
    runserver 
    celery -A lvlind.celery worker --pool=solo -l info
    celery -A lvlind beat -l INFO