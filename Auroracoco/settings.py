SECRET_KEY = 'your-secret-key'

DEBUG = False

ALLOWED_HOSTS = [
    "auroracoco-6gitbns5t-anju11.vercel.app",
    "127.0.0.1",
    "localhost",
]

CSRF_TRUSTED_ORIGINS = [
    "https://auroracoco-6gitbns5t-anju11.vercel.app",
]

STATIC_URL = "/static/"

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"