# Usa una imagen base oficial de Python.
FROM python:3.9-slim

# Establece el directorio de trabajo dentro del contenedor.
WORKDIR /code

# Copia el archivo de requerimientos y luego instálalos.
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del código del proyecto.
COPY . /code/

# Ejecuta migraciones y arranca el servidor.
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
