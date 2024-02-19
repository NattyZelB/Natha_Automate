from django.conf import settings
from django.core.management import call_command
from awd_main.celery import app
from django.core.mail import EmailMessage
from .utils import send_email_notification, generate_csv_file
import time
@app.task
def celery_test_task():
    time.sleep(5)  # simulation of any task that's going take 10 seconds
    #send an email
    mail_subject = 'Test subject'
    message = 'This is a test mail'
    to_email = settings.DEFAULT_TO_EMAIL
    send_email_notification(mail_subject, message, to_email)
    return 'Email sent successfully.'

@app.task
def import_data_task(file_path, model_name):
    try:
        call_command('importdata', file_path, model_name)
    except Exception as e:
        raise e
    #notify the user by email
    mail_subject = 'Import data completed'
    message = 'Your data import has been Completed'
    to_email = settings.DEFAULT_TO_EMAIL
    send_email_notification(mail_subject, message, to_email)
    return 'Data imported successfully!'

@app.task
def export_data_task(model_name):
    try:
        call_command('exportdata', model_name)
    except Exception as e:
        raise e

    file_path = generate_csv_file(model_name)

    # send email with the attachment
    mail_subject = 'Export data completed'
    message = 'Your data exported successfully, please find in attachment..'
    to_email = settings.DEFAULT_TO_EMAIL
    send_email_notification(mail_subject, message, to_email, attachment=file_path)
    return 'Data exported successfully!'


