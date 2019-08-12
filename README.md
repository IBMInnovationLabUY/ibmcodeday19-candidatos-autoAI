# Workshop sobre Watson Maching Learning y autoAI sobre Watson Studio - Realmente estoy seguro de a quien voy a votar?

<p align="center">
  <img src="assets/machinglearning.png" width="150" length="200">
  <img src="assets/watsonstudio.png" width="150" length="200">
</p>

## Flujo

* Crear una instancia de Watson Studio en IBM Cloud.
* Crear un proyecto Watson Studio.
* Agregar como un asset, el archivo csv.
* Refinar el dataset:
  * Declarar la primer fila como encabezado.
  * Eliminar fila Fecha.
  * Eliminar fila id.
  * Unificar candidatos de partidos tradicionales.
  * Filtrar y dejar solo los registros de los partidos tradicionales.
* Crear un Job, al completarse, obtendremos un nuevo archivo csv refinado.
* Agregar un servicio de Machine Learning.
* Agregar como un nuevo asset una instancia de AutoAI Experiment.
* Seleccionar como archivo de datos el nuevo archivo que genero nuestro Job.
* Seleccionar la variable a predecir.
* Ejecutar Run Experiment.


## Descripción

En este workshop se presentaran los conceptos principales sobre el servicio autoAI el cual se ofrece a traves de Watson Studio, ademas se presentara utilizaremnos otro de los servicios que nos ofrece IBM sobre Inteligencia Artificial, concretamente Watson Maching Learning. Con autoAI seremos capaces de generar distintos modelos de maching learning sobre un conjunto de datos especifico, permitiendos manipular el dataset para por ejemplo refinarlo. Adicionalmente nos brinda la capacidad de predecir distintas variables contenidas dentro de nuestro data set. 

## ¿Qué tiene el repositorio?
- Assets
- README.md

## Prerrequisitos
* Registrarse en IBM Cloud: [Aquí](https://ibm.biz/Bd26aa)

* Descargar el dataset

## Crear la instancia de Watson Studio desde IBM Cloud

Ir al catalogo de IBM, y seleccionar "AI".

![](/./assets/catalogo.png)

En las opciones que aparecen seleccionamos Watson Studio.

![](/./assets/studio.png)

Asignamos un nombre, en nuestro caso "Watson Studio-candidatos" y pulsamos en crear.

![](/./assets/crearstudio.png)

Si vamos a la pestaña "Manage", encontraremos links a la documentación del servicio recien creado. En dicha pantalla seleccionamos "Get Started" lo cual nos redirigirá hacia la plataforma de Watson Studio.

![](/./assets/getstarted.png)

## Crear un pryecto en Watson Studio

Una vez en Watson Studio es hora de crear el proyecto en el cual trabajaremos durante el workshop. Para ello presionamos sobre "Create Proyect".

![](/./assets/createproyect.png)

Y elegimos la opción de crear un proyecto vacío.

![](/./assets/emptyproyect.png)

Asigamos un nombre al proyecto. En este caso utilizaremos "candidatos-codeday". Posteriormente le damos "Create".

![](/./assets/nameproyect.png)

En este punto si hemos seguido todos los pasos, deberíamos tener creado nuestro nuevo proyecto vacío.

![](/./assets/newproyect.png)


## Agregar como un asset, el dataset previamente descargado.

Una vez que hemos creado el proyecto es hora de agregar el dataset que descargamos anteriormente como un asset en nuestro proyecto. Para ello vamos a la pestaña assets y en el cuadro que se muestra a la derecha de la pantalla presionamos sobre "browse" y seleccionamos el dataset.

![](/./assets/addcsv.png)


![](/./assets/selectassets.png)

Y deberíamos ver que se cargo correctamente el conjunto de datos.

![](/./assets/dataset.png)

## Refinar el dataset

Ahora que tenemos agregado el conjunto de datos en el proyecto, debemos refinar dicho conjunto para lograr un correcto procesamiento por parte de la herramienta.

Para ello vamos a la opción "actions" y seleccionamos "refine".

![](/./assets/refine.png)

### Declarar la primer fila como encabezado

Una vez que accedemos al panel de refinamiento debemos estipular que la primer fila es un encabezado en nuestro dataset. 

Para ello debemos seleccionar el icono que se encuentra en la parte inferior de la pantalla en la sección "Source file: ", en este paso deberíamos ver una pantalla como la que se muestra a continuación, en donde marcaremos el checkbox correspondiente para indicar que la primer fila de nuestro dataset es un encabezado. 

Para confirmar los cambios damos "apply" en la parte inferior de la ventana emergente que se nos presenta.

![](/./assets/encabezado.png)

### Eliminar columna Fecha e Id

Una vez que hemos indicado que la primer fila en el dataset se trata de un encabezado, es hora de eliminar las columnas "fecha" e "id" ya que no aportan datos útiles para el proposito de este workshop. 

Para realizar esto debemos ubicar dichas columnas haciendo scroll hacia el lado derecho del dataset.

![](/./assets/ubifila.png)

Una vez localizada la columna a eliminar, simplemente debemos acceder al panel de opciones clickeando en el icono que aparece a la derecha del nombre (icono de tres puntos en posicion vertical), y una vez alli seleccionamos la opción "remove".

![](/./assets/remove.png)

### Unificar candidatos de partidos tradicionales

Una vez realizado este procedimiento para las dos columnas en cuestión podemos seguir avanzando en nuestro refinamiento. 

En concreto, debemos unificar a los candidatos de cada partido de modo tal que quede solo un representante de cada uno. Este procedimiento lo hacemos con el fin de simplificar el dataset ya que el valor de los resultados de este workshop radican en marcar la distinción entre partidos politicos y no entre distintos candidatos de un mismo partido.

Asi que, manos a la obra. 

Empecemos por unificar a los candidatos del Frente Amplio, debemos sustituir a Carolina Cosse cuyo id es 3, a Mario Bergara con id 2 y a Oscar Andrada cuyo id es 1 por el valor 4 correspondiente en este caso a Daniel Martinez quien representará al Frente Amplio.

A continuación unificaremos a los candidatos del Partido Nacional, para ello debemos suprimir a Veronica Alonso con id 5, a Enrique Antía con id 6, a Carlos Iafigliola con id 8, a Jorge Larrañaga con id 10 y a Juan Sartori con id 11, por el valor 9 correspondiente a Luis Lacalle Pou quien representará al Partido Nacional.

Finalmente, repetimos el proceso para el Partido Colorado. En este caso sustiuiremos a José Amorín Batlle con id 12, a Pedro Etchegaray con id 13, a Edgardo Martínez Zimarioff con id 14, a Héctor Rovira con id 15, a Julio María Sanguinetti con id 16, por el valor 17 correspondiente a Ernesto Talvi quien representará al Partido Colorado.

Notemos que a los efectos de clarificar la información presentada se suprimieron el resto de los partidos menos La Alternativa debido a que la cantidad de votos obtenidos en forma conjunta esta muy alejada de los partidos tradicionales por lo cual no aporta demaciado al trabajo presentado en este documento.

Veamos ahora como realizar el proceso para un caso. Haciendo la salvedad de que debemos repetir este proceso para lograr realizar todos los cambios antes mencionados.

Para realizar una sustitución en el valor del campo Id debemos acceder a las opciones de dicha columna mediante la selección del icono que se encuentra a la derecha del nombre (icono de tres puntos en posición vertical) y accedemos a la sección "view all".

![](/./assets/all.png)

Luego, dentro de la sección "ORGANIZE" de las opciones, seleccionamos "Conditional replace". Dicha acción desplegara el menú donde completaremos los datos del reemplazo que queremos ejecutar, en el ejemplo sustituimos el cadidato con candidateId 1 (Carolina Cosse) por el valor 4 (Daniel Martinez).  

En la sección "operator" seleccionaremos la opción "Is equal to" para todas las sustituciones.

![](/./assets/replace.png)

Una vez completado los datos damos "add condition".

Cuando se halla completado este proceso para todas las sustituciones (agregamos una condición por cada sustitución que deseamos realizar) antes mencionadas estamos listos para continuar, para ello debemos confirmar las operaciones antes definidas dando click en "Apply" en la parte inferior del cuadro. (Notemos que debemos tener al finalizar el proceso 13 condiciones denotando las 13 sustituciones a realizar).

### Filtrar y dejar solo los registros de los Partidos Tradicionales

Una vez hechos todos los reemplazos es hora de filtrar el conjunto de datos de modo tal que solo queden los candidatos de los partidos tradicionales, para ello eliminaremos todos los candidatos menos los de candidateId: 4 (Daniel Martinez), 9 (Luis Lacalle Pou), 17 (Ernesto Talvi) y 18 (Pablo Mieres).

Desde el mismo panel de opciones de la columna candidatoId al que accedimos anteriormente para sustituir los valores, ahora elegiremos la opcion "Filter".

![](/./assets/filter.png)

En el panel que se desplega completamos los datos necesarios, en este caso al igual que en el anterior seleccionamos en el campo "operator" la alternativa "Is equal to". Realizamos este proceso para los 4 candidatoId que deseamos mantener, por lo que al final del proceso nos deberían quedar 4 condiciones las cuales aplicaremos clickeando en "Apply" en la parte inferior del cuadro.

![](/./assets/filter4.png)

Nota: Recordar seleccionar siempre la columna candidatoID para aplicar la condición y marcar la opcion "or" entre todas las condiciones creadas.

## Crear un nuevo Job

Para poder ejecutar las ordenes de refinamiento que acabamos de generar es necesario crear un Job que se encargue de dicha tarea.

Para ello debemos acceder al boton de Jobs que se encuentra en la parte superior derecha (Un icono con el simbolo de "play" . y un reloj). En las opciones que se desplegan seleccionamos "Save and create a Job".

![](/./assets/job1.png)

Le asignamos como nombre "candidatos-job" y pulsamos en "Create and Run"

![](/./assets/createjob.png)

Esperamos unos segundo a que se termine de crear el nuevo Job creado, y deberíamos tener una pantalla como la que se muestra a continuación. Donde el campo "Status" tiene el valor "Completed".

![](/./assets/finish.png)


## Agregar un servicio de Machine Learning

Una vez que hemos completado los pasos anteriores, estamos listos para agregar a nuestro proyecto una instancia de un nuevo servicio, concretamente una instancia de Maching Learning.

Para realizar esto, volvemos a nuestro proyecto y accedemos a la pestaña "Settings", vamos a la sección "Asociated Services" y agregamos uno nuevo.

![](/./assets/addML.png)

En el menú que se desplega seleccionamos la opción "Watson" lo que nos desplegará la distintas opciones que ofrece Watson dentro de las cuales seleccionamos Maching Learning.

![](/./assets/ml.png)

Nos redireccionará a la vista presentada a continuación, donde desde la parte inferior seleccionaremos "Create".

![](/./assets/newml.png)

Dejamos la configuración como se muestra por defecto, y confirmamos.

![](/./assets/dataml.png)


## Agregar como un nuevo asset una instancia de AutoAI Experiment

Posteriormente, nos dirigiremos a la pestaña "assets" desde donde agregaremos un nuevo AutoAI experiment

![](/./assets/autoAI.png)

Asignamos como nombre "candidatos-autoAI" y lo creamos.

![](/./assets/newautoAI.png)

## Seleccionar como archivo de datos el nuevo archivo que genero nuestro Job

Luego, agregamos como dato el nuevo dataset producto de aplicar el Job antes creado.

![](/./assets/addautoAI.png)

![](/./assets/adddata.png)

## Selecionar la columna a predecir

Una vez que agregamos el dataset, tenemos que seleccionar que columna queremos predecir. En este caso seleccionaremos la columna candidatoId desde el cuadro que se muestra en la parte derecha.

![](/./assets/selectautoAI.png)

## Ejecutar Run Experiment

Y finalmente corremos el experimento creado. Notemos que el servicio por defecto ya detecta que estamos queriendo aplicar un experimiento clasificador multiclase.

![](/./assets/runautoAI.png)

Una vez finalizados todos los pasos, entramos en la fase de entrenamiento.

![](/./assets/entrenamiento.png)












