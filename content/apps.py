from django.apps import AppConfig
from apscheduler.schedulers.background import BackgroundScheduler
from .tasks import get_columns

class ContentConfig(AppConfig):
    name = 'content'
    def ready(self):
        scheduler = BackgroundScheduler()
        # Create a schedule to run the get_dailymail_columns function in the background
        scheduler.add_job(func=get_columns, trigger="interval", seconds=15)
        # Starts the schedule
        scheduler.start()
