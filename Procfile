web: gunicorn main_proj_dir.wsgi
worker: celery -A orders.tasks worker -l info
