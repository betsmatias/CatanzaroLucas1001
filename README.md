Trabajo Práctico Integrador (TPI): Gestión de Datos de Países en Python 

Alumnos: Lucas Matias Catanzaro y Emiliano Fiscina. Grupo 27. 

Docentes: Cinthia Rigoni, Tutor Brian Lara c3 y Tutor Ana Mutti c4 

 Etapa 1: Carga y Visualización de Datos 

Carga de Datos: Crear una función en Python que lea los datos de los países desde un archivo.CSV 

Mostrar Datos: Implementar una función que imprima en la consola una tabla con la información básica de todos los países (nombre, superficie, población, continente). 

Etapa 2: Insertar datos 

Carga de País: Una función que solicite al usuario el ingreso de País, Población, Superficie y Continente que considere faltante. 

Etapa 3: Actualización de datos 

Modificar datos: El usuario podrá modificar los datos que fueron cargados inicialmente por el archivo, ingresará País y podrá modificar Población y Superficie. 

Etapa 4: Búsqueda: 

Búsqueda de información: El usuario podrá realizar la búsqueda de los datos que el desee. 

Etapa 5: Filtros de Información 

Permitirá al usuario filtrar la lista de países según los siguientes criterios: 

Filtrar por Continente: El usuario podrá filtrar como parámetro el nombre de un continente y devuelva una lista con los países que pertenecen a ella. 

Filtrar por Población: El usuario podrá filtrar ingresando un número mínimo y máximo que muestre los países que cumplen con lo solicitado. 

Filtrar por Superficie: El usuario podrá filtrar ingresar un número mínimo y máximo que muestre los países que cumplen con lo solicitado. 

Etapa 6: Ordenamiento de Datos 

Permitirá al usuario ordenar la lista de países de acuerdo a diferentes atributos: 

Ordenar por Nombre: El usuario podrá ordenar los países alfabéticamente por su nombre de forma ascendente o descendente. 

Ordenar por Población: El usuario podrá ordenar los países de mayor a menor población y viceversa. 

Ordenar por Superficie: El usuario podrá ordenar los países según su superficie de forma ascendente o descendente. 

Etapa 7: Cálculos Estadísticos 

Esta etapa le dará al usuario la información necesaria de estadísticas según cálculos sobre el conjunto de datos: 

País más y menos poblado: Determinar cuál es el país con la mayor y menor población. 

Promedio de Población: Calcular la población promedio de todos los países. 

Promedio de Superficie: Sumar la población de todos los países para obtener un total. 

Países por Continente: Contar cuántos países hay en cada región y mostrar los resultados. 

Conceptos de Programación Aplicados en el Proyecto de Gestión de Países 

Para el armado de nuestro código utilizamos los siguientes conceptos. 

1. Estructuras de Datos 

a. Listas  

Una lista es una colección ordenada y mutable de elementos. 

La variable lista_paises es una lista que almacena todos los registros de países. 

Almacenar resultados temporales: Se utilizan listas para guardar los resultados de búsquedas (buscar_pais), filtrados (filtrar_paises) u ordenamientos (ordenar_paises). 

Iteración: Permite recorrer uno por uno todos los países para realizar cálculos (como en mostrar_estadisticas) o comparaciones. 

b. Diccionarios 

Un diccionario es una colección desordenada de pares clave-valor. Es la forma más natural de representar un objeto o registro. En el código, cada país individual es un diccionario: 

Claves fijas: Cada diccionario de país tiene claves definidas ('nombre', 'poblacion', 'superficie', 'continente'). 

Acceso rápido: Permite acceder a los atributos del país por su nombre (clave), por ejemplo: pais['poblacion']. 

Mutabilidad: Permite actualizar valores específicos de un país, como su población y superficie, en la función actualizar_pais. 

2. Principios de Programación 

a. Funciones 

Las funciones son bloques de código reutilizable diseñados para realizar una tarea específica. Su uso promueve el modularidad y la legibilidad del código. 

Modularidad: El código está dividido en funciones pequeñas y enfocadas (ejemplos: agregar_pais, limpiar_pantalla, obtener_nombre). 

Función Principal (main): El programa inicia y se controla desde la función main(), que actúa como el bucle central de la aplicación. 

Funciones Auxiliares: Las funciones obtener_nombre, obtener_poblacion, y obtener_superficie se utilizan específicamente como funciones clave para el ordenamiento. 

b. Condicionales (if/elif/else) 

Las condicionales permiten que el programa tome decisiones y ejecute diferentes bloques de código basados en el cumplimiento de ciertas condiciones. 

Validación de entrada: Se usan (obtener_entrada_no_vacia, obtener_entrada_numerica) para asegurar que el usuario ingrese datos válidos. 

Flujo del programa: La función main() utiliza una cadena de if/elif para ejecutar la acción correspondiente a la opción del menú seleccionada por el usuario. 

Validación de datos y existencia: En cargar_datos, se usa if para verificar la existencia del archivo, el número de columnas y el tipo de dato. 




c. Archivos CSV (Manejo de Datos) 

Un archivo CSV es un formato de texto simple utilizado para almacenar datos tabulares. 

Persistencia: La función cargar_datos lee el archivo paises.csv línea por línea para inicializar la lista de países, permitiendo que los datos persistan entre ejecuciones del programa, cada línea del archivo se separa en sus componentes (nombre, población, superficie, continente) usando el método split(','). 


Funciones del equipo 

Actividad  

Emiliano Fiscina 

Lucas Catanzaro 

Formulacion del proyecto 

si 

si 

Recopilacion de informacion  

si  

si  

Armado de archivo 

si 

control 

Generacion de codigo 

Testeo  

Inicio del programa 

Definicion de funciones 

Testeo  

Definicion de pasos 

Finalizacion de programa 

Testo y simulacion de Usuario 

Finalizacion de programa 

Modificaciones  

Analisis de funcionamiento y actualizaciones 

Analisis de funcionamiento y actualizaciones 


