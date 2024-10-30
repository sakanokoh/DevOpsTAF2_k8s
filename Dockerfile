# Utiliser l'image Python alpine pour réduire la taille de l'image
FROM python:3.9-alpine

# Définir le répertoire de travail
WORKDIR /code

# Copier et installer les dépendances
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copier les fichiers de l'application
COPY ./app /code/app

# Exposer le port de l'application
EXPOSE 8000

# Lancer l'application FastAPI
CMD ["uvicorn", "app.app:app", "--host", "0.0.0.0", "--port", "8000"]