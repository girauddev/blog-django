# Eccomerce Emperor - Python + Django - CoderHouse 2022

El siguiente proyecto fue desarrollado por Augusto Giraud en base a lo aprendido en el curso de Python brindado por CoderHouse 2022.

Profesor: Leonel Gareis
Tutor: Diego Ariel Simonelli
Alumno: Augusto Giraud

Link al template utilizado: https://startbootstrap.com/template/shop-homepage

Codeado en Python 3.9.12 / Django 4.0.3. SO: macOS Monterey 12.1

Funcionalidades:
*Base de datos
*Tres Models
*Carga de datos a DB
*Busqueda de Modelo Mouse en DB
*Herencia de HTML
*Utilización de Templates

La plataforma Emperor de ecommerce cuenta con una landing a la cual es posible igresar mediante http://127.0.0.1:8000/ecommerce/ donde tendremos una vista panoramica de los productos (modelos) ofrecidos.

Dichos modelos cuentan con su página propia donde, mientras vayamos cargando, vamos a ir dibujando una CARD de cada uno de ellos de manera ordenada**, actualmente contamos con 3 modelos: Mouse, Display y Headphones.

Todos cuentan con la posibilidad de cargarles datos mediante la DB, solo debe dirigirse al NavBar y desplegar el menu "Carga DB", donde podrá ingresar a la page de carga de cada uno de los modelos.

De estos 3, solo uno cuenta con una busqueda en la base de datos, el mismo es Mouse. Podrá ingresar a la busqueda en DB desde el NavBar, seleccionando el botón de acción "Buscar Mouses"

Dicho NavBar cuenta con un botón para dirigirse al landing page, asi como tambien ingresar a cada una de las landing correspondientes a cada modelo.

**La CARD puede llegar a dibujarse "rota" si se añaden mas de 8 objetos.
**Encontrará una carpeta llamada "media" ya que la plataforma iba a contar con un modulo de item, que traeria una página de cada uno de los articulos, lamentablemente y luego de muchos dolores de cabeza, se replanteo darle mayor importancia a la funcionalidad que al apartado de desarrollo web, sin embargo, en versiones futuras le traeremos esta funcionalidad correctamente codeada.

¡Muchas gracias!
