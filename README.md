# Database Project: Backend

Este es un proyecto realizado por estudiantes del Programa de Ingeniería en Informática del Decanato de Ciencias y tecnología de la Universidad Centroccidental "Lisandro Alvarado", para la materia de Base de datos con la finalidad de recrear una pagina web que permita realizar la preapertura de una cuenta financiera.

## Fundamentación

Este proyecto fue elaborado en base al framework de Python, Djando, en complemento de algunas librerías que son de vital importancia para el desarrollo de algunas funciones incluidas dentro del funcionamiento general del proyecto. Similarmente, destaca la implementación de la librería multiplataforma Bootstrap, dentro del diseño y desarrollo web.  Finalmente, para la gestión de la base de datos, se utilizó la herramienta SQLite.

## Requisitos previos al despliegue:

Instalación del lenguaje de programación Python
Instalación del framework Django

## Despliegue:

Para la fase del despliegue, se debe iniciar con la clonación del proyecto. Para esto se debe descargar el repositorio en una carpeta previamente creada y destinada al almacenamiento del mismo. Haciendo uso de la consola, nos ubicamos en la carpeta anteriormente mencionada y ejecutamos el comando:

git clone https://github.com/Damurq/database_backend.git

Posteriormente, resulta necesario que nos situemos desde consola en la carpeta del repositorio clonado, en este caso “database_backend”, con el comando:
```
cd database_backend
```
Luego procedemos con la instalación del manejador de dependencias en nuestro proyecto con el comando:

pip install pipenv

Para el siguiente paso que es la instalación del entorno virtual, resulta necesario que nos ubiquemos en la carpeta “Backend” con el siguiente comando:
```
cd Backend
```
Ahora, para la instalación del entorno ejecutamos el comando:
```
pipenv shell
```
Por su parte, para  la instalación de los paquetes necesarios en el entorno virtual, se ejecuta el comando:
```
pipenv install
```
Para finalizar con el despliegue de nuestro proyecto, se ejecuta el  comando:
```
python manage.py runserver
```
## Herramientas Empleadas:
Para el backend del proyecto se emplearon las siguientes herramientas de desarrollo web:

* Django: Framework web gratuito y de código abierto, escrito en python. Este framework trabaja con la estructura MTV (model template view). Django nos permite crear sitios web complejos de forma rápida y sencillos.

* DB Browser(for SQLite): Es un sistema de gestión de bases de datos relacional. El cual es uno de los gestores de base de datos oficialmente soportado por Django además es con el que trabaja por defecto.

Por su parte, para el frontend del proyecto se emplearon las siguientes herramientas de diseño web:

* Bootstrap: Frameworks de CSS de código abierto que combina javascript, HTML y CSS. Permitiendo maquetar las páginas web de forma limpia y responsive.

* HTML: Lenguaje de Marcado de Hipertexto cuyo código se utiliza para estructurar y desplegar una página web y sus contenidos. Por ejemplo, sus contenidos podrían ser párrafos, una lista con viñetas, o imágenes y tablas de datos.

* CSS: Lenguaje de hojas de estilo cuyo codigo permite aplicar estilos de manera selectiva a elementos en documentos HTML, dandole asi estilos a la pagina web.

## Colaboradores:

Este proyecto fue desarrollado en conjunto por:

* Yurisbellys Brizuela (yurisjbc23)
* Marihec Miranda (MarihecMiranda)
* Michael Montero (Damurq)
* Luis Torrealba (luisdavidwww)
