from celery import Celery
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shopping_mall.setting.dev")
celery_app = Celery("shopping_mall")
celery_app.configu_from_object("celery_tasks.configu")
celery_app.autodiscover_tasks("celery_tasks.sms", "celery_tasks.email")

