FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r /app/requirements.txt

# Run with: docker run -p 8000:8000 messaging_app


EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
