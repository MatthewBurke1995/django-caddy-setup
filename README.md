```sudo docker-compose run django django-admin startproject project .

vi project/settings.py```

write in the following:
```
# settings.py
   
import os
   
[...]
   
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_NAME'),
        'USER': os.environ.get('POSTGRES_USER'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
        'HOST': 'db',
        'PORT': 5432,
    }
}
```

```
docker-compose run django python manage.py startapp app
docker-compose run django python manage.py migrate
docker-compose run django python manage.py createsuperuser

echo '\n\nCSRF_TRUSTED_ORIGINS=["https://localhost"]' >> project/settings.py
```

