import datetime
AWS_ACCESS_KEY_ID = "AKIAI6V4JAJ2JADKTZKA"
AWS_SECRET_ACCESS_KEY = "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"
AWS_FILE_EXPIRE = 200
AWS_PRELOAD_METADATA = True
AWS_QUERYSTRING_AUTH = True

DEFAULT_FILE_STORAGE = 'mysite.storage.MediaRootS3BotoStorage'
STATICFILES_STORAGE = 'mysite.storage.StaticRootS3BotoStorage'
AWS_STORAGE_BUCKET_NAME = 'ishkstorage'
S3DIRECT_REGION = 'ap-northeast-2'
S3_URL = '//%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
MEDIA_URL = '//%s.s3.amazonaws.com/media/' % AWS_STORAGE_BUCKET_NAME
MEDIA_ROOT = MEDIA_URL
STATIC_URL = S3_URL + 'static/'
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

two_months = datetime.timedelta(days=61)
date_two_months_later = datetime.date.today() + two_months
expires = date_two_months_later.strftime("%A, %d %B %Y 20:00:00 GMT")

AWS_HEADERS = {
    'Expires': expires,
    'Cache-Control': 'max-age=%d' % (int(two_months.total_seconds()), ),
}


# AWS_ACCESS_KEY_ID = 'AKIAI6V4JAJ2JADKTZKA'
# AWS_SECRET_ACCESS_KEY = '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'
# AWS_STORAGE_BUCKET_NAME = 'ishkstorage'
# AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
# AWS_HEADERS = {
#         'Cache-Control': 'max-age=94608000',
#     }
# AWS_STATIC_LOCATION = 'static'
# AWS_MEDIA_LOCATION = 'media'
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'mysite/static'),
# ]
# STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_STATIC_LOCATION)
# STATICFILES_STORAGE = 'mysite.storage.StaticRootS3BotoStorage'
#
# MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN,AWS_MEDIA_LOCATION)
# MEDIA_ROOT = os.path.join(BASE_DIR,'media')
# DEFAULT_FILE_STORAGE = 'mysite.storage.MediaRootS3BotoStorage'