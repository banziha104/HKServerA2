import datetime
AWS_ACCESS_KEY_ID = "AKIAI6V4JAJ2JADKTZKA"
AWS_SECRET_ACCESS_KEY = "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"
AWS_REGION = 'ap-northeast-2'

AWS_FILE_EXPIRE = 200
AWS_PRELOAD_METADATA = True
AWS_QUERYSTRING_AUTH = True
# AWS_REGION = 'ap-northeast-2'
# https://ishkstorage.s3.amazonaws.com/media/HKmodel/2017/&m/12/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2017-11-09_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_3.58.10.png?Expires=1510485915&Signature=YKXjcVliNdCJ0MUigesVcQ4DT8U%3D&AWSAccessKeyId=AKIAI6V4JAJ2JADKTZKA a
# https://s3.ap-northeast-2.amazonaws.com/ishkstorage/media/HKmodel/2017/&m/12/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2017-11-09_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_3.58.10.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAI6V4JAJ2JADKTZKA%2F20171112%2Fap-northeast-2%2Fs3%2Faws4_request&X-Amz-Date=20171112T102616Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Signature=4df13d45888ad427c35d4a6c731f314e667e1b245088a56e5e6f5a5ea4a9d36b
DEFAULT_FILE_STORAGE = 'mysite.storage.MediaRootS3BotoStorage'
STATICFILES_STORAGE = 'mysite.storage.StaticRootS3BotoStorage'
AWS_STORAGE_BUCKET_NAME = 'ishkstorage'
S3DIRECT_REGION = 'ap-northeast-2'
AWS_S3_HOST = 's3.%s.amazonaws.com' % AWS_REGION
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

# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

# AWS Setting
# AWS_REGION = 'ap-northeast-2'
# AWS_STORAGE_BUCKET_NAME = 'ishkstorage'
# AWS_QUERYSTRING_AUTH = False
# AWS_S3_HOST = 's3.%s.amazonaws.com' % AWS_REGION
# AWS_ACCESS_KEY_ID = '6nCKLrwQKqiP8YiMQTS5qMuXmNI5c9gKb8XRzAge'
# AWS_SECRET_ACCESS_KEY = 'AKIAI6V4JAJ2JADKTZKA'
# AWS_S3_CUSTOM_DOMAIN = '%s.s3.%s.amazonaws.com' % (AWS_STORAGE_BUCKET_NAME,AWS_REGION)
# AWS_S3_OBJECT_PARAMETERS = {    'CacheControl': 'max-age=86400',}
# # Static Setting
# STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN,'static')
# STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
#
# # Media Setting
# MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN,'media')
# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

