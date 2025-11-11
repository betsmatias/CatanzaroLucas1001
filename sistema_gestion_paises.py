
import os  # Necesario para verificar si el archivo existe y limpiar pantalla
import unicodedata

# Constante para el nombre del archivo
NOMBRE_ARCHIVO_CSV = 'paises.csv'

# --- Funciones de Carga y Limpieza ---

def limpiar_pantalla():
    """
    Limpia la pantalla de la consola.
    Funciona tanto en Windows ('cls') como en Linux/macOS ('clear').
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def cargar_datos(nombre_archivo):
    """
    Carga los datos desde un archivo CSV.
    Valida la existencia del archivo, el formato de las líneas y
    que los datos numéricos sean correctos.
    """
    lista_paises = []
    
    # 1. Validación: Verificar si el archivo existe
    if not os.path.exists(nombre_archivo):
        print(f"Error: El archivo '{nombre_archivo}' no se encuentra.")
        print("Asegúrate de que esté en la misma carpeta que el script.")
        # Hacemos una pausa para que el usuario lea el error
        input("\nPresione Enter para intentar de nuevo...") 
        return lista_paises  # Retorna lista vacía

    # Si existe, lo abrimos
    archivo = open(nombre_archivo, 'r', encoding='utf-8')
    
    # Omitir la cabecera (header)
    next(archivo, None)
    
    print("Cargando datos...")
    
    # Procesar cada línea
    for linea in archivo:
        linea = linea.strip()  # Quitar espacios/saltos de línea

        if not linea: continue # Ignorar líneas vacías

        partes = linea.split(',')
        
        # 2. Validación: Verificar formato (cantidad de columnas)
        if len(partes) != 4:
            print(f"Error de formato: La línea '{linea}' no tiene 4 columnas. Se omite.")
            continue
            
        nombre, pob_str, sup_str, continente = partes
        
        # 3. Validación: Campos vacíos
        if not nombre or not pob_str or not sup_str or not continente:
            print(f"Error de datos: La línea '{linea}' tiene campos vacíos. Se omite.")
            continue
        
        # 4. Validación: Datos numéricos
        if not pob_str.isdigit() or not sup_str.isdigit():
            print(f"Error de tipo: La línea '{linea}' tiene datos no numéricos. Se omite.")
            continue

        # Si todas las validaciones pasan, creamos el diccionario
        pais = {
            'nombre': nombre,
            'poblacion': int(pob_str),
            'superficie': int(sup_str),
            'continente': continente
        }
        lista_paises.append(pais)

    archivo.close()
    if lista_paises:
        print("¡Datos cargados exitosamente!")
    else:
        print("No se cargaron datos, el archivo podría estar vacío o todas las líneas tenían errores.")
        
    # Pausa después de la carga inicial
    input("\nPresione Enter para continuar...")
    return lista_paises

# --- Funciones de entrada segura ---

def obtener_entrada_no_vacia(mensaje):
    """Pide al usuario una entrada y valida que no esté vacía."""
    entrada = input(mensaje).strip()
    while not entrada:
        print("Error: Este campo no puede estar vacío.")
        entrada = input(mensaje).strip()
    return entrada

def obtener_entrada_numerica(mensaje):
    """Pide al usuario un número y valida que sea un entero positivo."""
    entrada = input(mensaje).strip()
    while not entrada.isdigit():
        print("Error: Debe ingresar un número entero y positivo.")
        entrada = input(mensaje).strip()
    return int(entrada)

# --- Funciones auxiliares para ordenamiento  ---

def obtener_nombre(pais_dict):
    """Devuelve el nombre de un diccionario de país."""
    return pais_dict['nombre']

def obtener_poblacion(pais_dict):
    """Devuelve la población de un diccionario de país."""
    return pais_dict['poblacion']

def obtener_superficie(pais_dict):
    """Devuelve la superficie de un diccionario de país."""
    return pais_dict['superficie']

# --- Funciones del Menú ---

def mostrar_paises(lista):
    """
    Muestra una lista de países en formato de "bloque" vertical,
    uno debajo del otro, para mejor legibilidad.
    """
    if not lista:
        print("No hay países para mostrar o que cumplan el criterio.")
        return
        
    print(f"\n--- {len(lista)} Países Encontrados ---")
    
    for pais in lista:
        print("-" * 30)  # Separador
        print(f"  Nombre:     {pais['nombre']}")
        # : , agrega comas como separadores de miles
        print(f"  Población:  {pais['poblacion']:,}")
        print(f"  Superficie: {pais['superficie']:,} km²")
        print(f"  Continente: {pais['continente']}")
    
    print("-" * 30)

def agregar_pais(paises):
    """Agrega un nuevo país a la lista global."""
    print("--- Agregar Nuevo País ---")
    nombre = obtener_entrada_no_vacia("Nombre: ")
    poblacion = obtener_entrada_numerica("Población: ")
    superficie = obtener_entrada_numerica("Superficie (km²): ")
    continente = obtener_entrada_no_vacia("Continente: ")
    
    nuevo_pais = {
        'nombre': nombre,
        'poblacion': poblacion,
        'superficie': superficie,
        'continente': continente
    }
    paises.append(nuevo_pais)
    print(f"¡País '{nombre}' agregado exitosamente!")

def actualizar_pais(paises):
    """Actualiza la población y superficie de un país existente."""
    print("--- Actualizar País ---")
    nombre_buscar = obtener_entrada_no_vacia("Ingrese el nombre exacto del país a actualizar: ")
    
    pais_encontrado = None
    for pais in paises:
        if pais['nombre'].lower() == nombre_buscar.lower():
            pais_encontrado = pais
            break
            
    if pais_encontrado is None:
        print(f"Error: No se encontró ningún país con el nombre '{nombre_buscar}'.")
        return

    print(f"Actualizando datos de: {pais_encontrado['nombre']}")
    nueva_poblacion = obtener_entrada_numerica(f"Nueva población (actual: {pais_encontrado['poblacion']:,}): ")
    nueva_superficie = obtener_entrada_numerica(f"Nueva superficie (actual: {pais_encontrado['superficie']:,} km²): ")
    
    pais_encontrado['poblacion'] = nueva_poblacion
    pais_encontrado['superficie'] = nueva_superficie
    
    print(f"¡Datos de '{pais_encontrado['nombre']}' actualizados!")

def buscar_pais(paises):
    """Busca países por coincidencia parcial o exacta."""
    print("--- Buscar País por Nombre ---")
    termino = obtener_entrada_no_vacia("Ingrese el nombre (o parte) del país a buscar: ").lower()
    
    resultados = []
    for pais in paises:
        if termino in pais['nombre'].lower():
            resultados.append(pais)
            
    if not resultados:
        print(f"No se encontraron países que coincidan con '{termino}'.")
    else:
        mostrar_paises(resultados)

def filtrar_paises(paises):
    """Muestra un submenú para filtrar por continente o rangos."""
    
    def normalizar_texto(s):
        """Función interna para quitar acentos y convertir a minúsculas."""
        s = ''.join(c for c in unicodedata.normalize('NFD', s)
                    if unicodedata.category(c) != 'Mn')
        return s.lower()

    print("--- Filtrar Países ---")
    print("1. Filtrar por Continente")
    print("2. Filtrar por Rango de Población")
    print("3. Filtrar por Rango de Superficie")
    opcion = obtener_entrada_no_vacia("Seleccione una opción de filtro: ")

    resultados = []
    
    if opcion == '1':
        # Pedimos al usuario el término de búsqueda
        termino_continente = obtener_entrada_no_vacia("Ingrese el nombre del continente: ")
        
        # Normalizamos la entrada del usuario (ej: "america")
        termino_normalizado = normalizar_texto(termino_continente)
        
        for pais in paises:
            # Normalizamos el dato del diccionario (ej: "america (caribe)")
            continente_dato_normalizado = normalizar_texto(pais['continente'])
            
            # Comparamos si la entrada del usuario ESTÁ CONTENIDA en el dato
            # (ej: "america" in "america (caribe)")
            if termino_normalizado in continente_dato_normalizado:
                resultados.append(pais)
                
    elif opcion == '2':
        pob_min = obtener_entrada_numerica("Población mínima: ")
        pob_max = obtener_entrada_numerica("Población máxima: ")
        for pais in paises:
            if pob_min <= pais['poblacion'] <= pob_max:
                resultados.append(pais)

    elif opcion == '3':
        sup_min = obtener_entrada_numerica("Superficie mínima: ")
        sup_max = obtener_entrada_numerica("Superficie máxima: ")
        for pais in paises:
            if sup_min <= pais['superficie'] <= sup_max:
                resultados.append(pais)
    else:
        print("Opción de filtro no válida.")
        return 
        
    if not resultados:
        print("No se encontraron países que cumplan con el filtro.")
    else:
        mostrar_paises(resultados)

def ordenar_paises(paises):
    """
    Ordena la lista de países por el criterio y orden elegidos.
    Usa funciones auxiliares (ej: obtener_nombre).
    """
    print("--- Ordenar Países ---")
    print("Criterio de orden:")
    print("1. Nombre")
    print("2. Población")
    print("3. Superficie")
    criterio = obtener_entrada_no_vacia("Seleccione un criterio: ")
    
    print("Orden:")
    print("1. Ascendente (A-Z, Menor a Mayor)")
    print("2. Descendente (Z-A, Mayor a Menor)")
    orden = obtener_entrada_no_vacia("Seleccione un orden: ")
    
    es_descendente = (orden == '2')
    
    lista_ordenada = []
    if criterio == '1':
        # p: p['nombre']
        lista_ordenada = sorted(paises, key=obtener_nombre, reverse=es_descendente)
    elif criterio == '2':
        #  p: p['poblacion']
        lista_ordenada = sorted(paises, key=obtener_poblacion, reverse=es_descendente)
    elif criterio == '3':
        #  p: p['superficie']
        lista_ordenada = sorted(paises, key=obtener_superficie, reverse=es_descendente)
    else:
        print("Criterio de orden no válido.")
        return

    print("--- Países Ordenados ---")
    mostrar_paises(lista_ordenada)

def mostrar_estadisticas(paises):
    """
    Calcula y muestra estadísticas clave sobre los datos.
    Usa un bucle 'for'.
    """
    print("--- Estadísticas de Países ---")
    
    if not paises:
        print("No hay datos cargados para calcular estadísticas.")
        return

    # 1. País con mayor y menor población 
    
    
    # Inicializamos las variables con el primer país de la lista
    mayor_pob = paises[0]
    menor_pob = paises[0]
    
    total_poblacion = 0
    total_superficie = 0
    conteo_continentes = {}
    
    # Usamos un solo bucle para calcular todo
    for pais_actual in paises:
        
        # --- Cálculo de Min/Max ---
        # Comparamos para encontrar el mayor
        if pais_actual['poblacion'] > mayor_pob['poblacion']:
            mayor_pob = pais_actual
            
        # Comparamos para encontrar el menor
        if pais_actual['poblacion'] < menor_pob['poblacion']:
            menor_pob = pais_actual
            
        # --- Cálculo de Promedios ---
        total_poblacion += pais_actual['poblacion']
        total_superficie += pais_actual['superficie']
        
        # --- Conteo por Continente ---
        continente = pais_actual['continente']
        conteo_continentes[continente] = conteo_continentes.get(continente, 0) + 1

    # --- Mostrar resultados de Min/Max ---
    print(f"País con mayor población: {mayor_pob['nombre']} ({mayor_pob['poblacion']:,})")
    print(f"País con menor población: {menor_pob['nombre']} ({menor_pob['poblacion']:,})")
    
    # --- Mostrar resultados de Promedios ---
    cantidad_paises = len(paises)
    prom_poblacion = total_poblacion / cantidad_paises
    prom_superficie = total_superficie / cantidad_paises
    
    print(f"Población promedio: {prom_poblacion:,.2f}")
    print(f"Superficie promedio: {prom_superficie:,.2f} km²")
    
    # --- Mostrar resultados de Conteo ---
    print("\nCantidad de países por continente:")
    for continente, cantidad in conteo_continentes.items():
        print(f"- {continente}: {cantidad}")

def mostrar_menu():
    """Imprime el menú principal en la consola."""
    print("===== Gestión de Datos de Países =====")
    print("1. Agregar un país")
    print("2. Actualizar datos de un país")
    print("3. Buscar un país por nombre")
    print("4. Filtrar países")
    print("5. Ordenar países")
    print("6. Mostrar estadísticas")
    print("7. Mostrar todos los países")
    print("8. Salir")
    print("========================================")

def main():
    """Función principal que ejecuta el programa."""
    
    lista_paises = cargar_datos(NOMBRE_ARCHIVO_CSV)
    
    while True:
        limpiar_pantalla() 
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if not opcion.isdigit():
            print("Error: Opción inválida. Debe ingresar un número del 1 al 8.")
            input("\nPresione Enter para reintentar...")
            continue 
            
        op = int(opcion)
        
        limpiar_pantalla()

        if op == 1:
            agregar_pais(lista_paises)
        elif op == 2:
            actualizar_pais(lista_paises)
        elif op == 3:
            buscar_pais(lista_paises)
        elif op == 4:
            filtrar_paises(lista_paises)
        elif op == 5:
            ordenar_paises(lista_paises)
        elif op == 6:
            mostrar_estadisticas(lista_paises)
        elif op == 7:
            mostrar_paises(lista_paises)
        elif op == 8:
            print("¡Gracias por usar el programa! Adiós.")
            break 
        else:
            print("Error: Opción no válida. Intente de nuevo.")

        # Pausa para ver los resultados
        print("\n" * 2) 
        input("Presione Enter para volver al menú...")

# --- Punto de entrada del script ---
if __name__ == "__main__":
    main()