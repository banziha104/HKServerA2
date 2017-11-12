from django.test import TestCase
import os
# Create your tests here.
from os.path import abspath, dirname, join
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = dirname(dirname(dirname(abspath(__file__))))

print(os.path.join(BASE_DIR, 'db.sqlite3'))
print(os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings.common"))
