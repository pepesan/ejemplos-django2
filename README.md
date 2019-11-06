# Repositorio de ejemplos de Django 2

# Descargar las dependencias de Django ejecutando:
pip install -r ./requirements.txt
# Arrancar la aplicación Django
python3 ./manage.py runserver

Después podremos acceder desde la URL:
[http://localhost:8000/](http://localhost:8000/)

# Notas del proyecto
El proyecto se ha creado con la herramenta django-admin, para empezar el desarrollo es necesario instalar django
pip install django==2.2.7
# Creación del proyecto
django-admin startproject miproyecto
cd miproyecto
# Creación de la aplicación
django-admin startapp miapp

# Módulos de ejemplo
El módulo miapp es el módulo más básico, que incluye uso básico de URLS, Views (Controladores) y Plantillas (Vista)
