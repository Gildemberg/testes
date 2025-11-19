FROM python:3.11-slim
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt


COPY . /app


ENV DJANGO_SETTINGS_MODULE=qualidade_software.settings
ENV PORT=8000


RUN python manage.py collectstatic --noinput || true


CMD ["gunicorn", "qualidade_software.wsgi:application", "--bind", "0.0.0.0:8000"]