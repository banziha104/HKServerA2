from django.contrib.staticfiles.storage import CachedFilesMixin, ManifestFilesMixin
from django.conf import settings
from storages.backends.s3boto import S3BotoStorage

class StaticStorage(S3BotoStorage):
    location = settings.STATICFIL