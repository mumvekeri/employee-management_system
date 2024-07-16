INSTALLED_APPS = [
    ...
    'employees',
    'rest_framework',  # Add this for Django REST framework
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / "db.sqlite3",
    }
}
