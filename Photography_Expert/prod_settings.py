import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = '-j=ri%2l3kknt5i!34b]8x-hg*rje*3v+%dy#sxo-stby456*^@'

DEBUG = False

AWS_ACCESS_KEY_ID = 'AKIAQWPVTWVA6HW7H74K'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'phtography-expert'
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}
DEFAULT_FILE_STORAGE = 'Photography_Expert.storages.MediaStorage'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
