# Biblioteca
## Jose Luis Jiménez Bayona - 1152384

**Ejecutar Localmente** 

**1. Clonar el repositorio**

`https://github.com/joseluisjb/Biblioteca.git`

Cambiar al directorio:

`cd carpeta_donde_se_clono`

**2. Crear un entorno virtual**

`python -m venv venv`

Activar el entorno:

`venv\Scripts\activate`

**3. Instalar dependencias**

`pip install django`

**4. Configurar la base de datos**

`python manage.py makemigrations`

`python manage.py migrate`

**5. Crear un superusuario para el panel de administración**

`python manage.py createsuperuser`

**6. Ejecutar el servidor local**

`python manage.py runserver`

Luego iniciar sesión con el superusuario creado anteriormente

**7. Cargar datos iniciales**

`python manage.py shell`

`>>> exec(open('poblar_datos.py').read())`
