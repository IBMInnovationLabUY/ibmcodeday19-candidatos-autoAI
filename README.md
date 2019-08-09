# Workshop sobre Watson Maching Learning y autoAI sobre Watson Studio - Realmente estoy seguro de a quien voy a votar?

<p align="center">
  <img src="assets/machinglearning.png" width="150" length="200">
  <img src="assets/watsonstudio.png" width="150" length="200">
</p>

## Flujo

* Crear una instancia de Watson Studio en IBM Cloud.
* Crear un proyecto Watson Studio
* Agregar como un asset, el archivo csv
* Refinar el dataset:
  * Declarar la primer fila como encabezado
  * Eliminar fila Fecha
  * Eliminar fila id
  * Sustituir en candidatoId 1,2 y 3 por 4; 5,6,8,10,11 por 9; 12,13,14,15,16 por 17
  * Filtrar y dejar solo los registros que en candidatoId tenga 4,9,17 o 18
* Crear un Job
* Al completarse, obtendremos un nuevo archivo csv refinado.
* Agregamos un servicio de Machine Learning
* Agregar como un nuevo asset una instancia de AutoAI Experiment
* Seleccionar como archivo de datos el nuevo archivo que genero nuestro Job
* Seleccionar la variable a predecir
* Ejecutar Run Experiment


## Descripción

En este workshop se presentaran los conceptos principales sobre el servicio autoAI el cual se ofrece a traves de Watson Studio, ademas se presentara utilizaremnos otro de los servicios que nos ofrece IBM sobre Inteligencia Artificial, concretamente Watson Maching Learning. Con autoAI seremos capaces de generar distintos modelos de maching learning sobre un conjunto de datos especifico, permitiendos manipular el dataset para por ejemplo refinarlo. Adicionalmente nos brinda la capacidad de predecir distintas variables contenidas dentro de nuestro data set. 

## ¿Qué tiene el repositorio?
- Assets
- README.md


## Prerrequisitos
* Registrarse en IBM Cloud: [Aquí](https://cloud.ibm.com/registration)

* Descargar el dataset

## Crear la instancia de Watson Studio desde IBM Cloud

Ir al catalogo de IBM, y seleccionar "AI".

![](/./assets/catalogo.png)

En las opciones que aparecen seleccionamos Watson Studio.

![](/./assets/studio.png)

Asignamos un nombre, en nuestro caso "Watson Studio-candidatos" y pulsamos en crear.\

![](/./assets/crearstudio.png)

Si vamos a la pestaña "Manage", encontramos links a la documentacion del servicio recien creado. En dicha pantalla seleccionamos "Get Started" lo cual nos redirigira hacia la plataforma de Watson Studio.

![](/./assets/getstarted.png)

## Crear un pryecto en Watson Studio

Una vez en Watson Studio es hora de crear el proyecto en el cual trabajaremos durante el workshop. Para ello presionamos sobre "Create Proyect".

![](/./assets/createproyect.png)

Y elegimos la opcion de crear un proyecto vacio.

![](/./assets/emptyproyect.png)

Asigamos un nombre al proyecto. En este caso utilizaremos "candidatos-codeday". Posteriormente le damos "Create".

![](/./assets/nameproyect.png)

En este punto si seguimos todos los pasos, deberiamos tener creado nuestro nuevo proyecto vacio.

![](/./assets/newproyect.png)


## Agregar como un asset, el dataset previamente descargado.

Una vez que hemos creado el proyecto es hora de agregar el dataset que descargamos anteriormente como un assets en nuestro proyecto. Para ello vamos a la pestaña assets y en el cuadro que se muestra a la derecha de la pantalla presionamos sobre "browse" y seleccionamos el dataset.

![](/./assets/addcsv.png)


![](/./assets/selectassets.png)

Y deberiamos ver que se cargo correctamente el conjunto de datos.

![](/./assets/dataset.png)

## Refinar el dataset

Ahora que tenemos agregado el conjunto de datos en el proyecto, debemos refinar dicho conjunto para lograr un correcto procesamiento por parte de la herramienta.

Para ello hacemos click las opciones y seleccionamos "refine".

![](/./assets/refine.png)















