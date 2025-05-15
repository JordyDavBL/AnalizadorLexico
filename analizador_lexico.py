import re

# Definición de tokens (simplificada)
tokens = {
    'PALABRA_RESERVADA': r'\b(inicio|fin|imprimir|leer|si|sino|mientras)\b',
    'IDENTIFICADOR': r'\b[a-zA-Z_][a-zA-Z0-9_]*\b',
    'NUMERO': r'\b\d+\b',
    'ASIGNACION': r'=',
    'OPERADOR': r'[+\-*/]',
    'PUNTOYCOMA': r';',
    'PARENTESIS_ABRE': r'\(',
    'PARENTESIS_CIERRA': r'\)',
    'LLAVE_ABRE': r'\{',
    'LLAVE_CIERRA': r'\}',
    'ESPACIO': r'\s+',
}

# Compilamos todos los patrones en uno solo
token_regex = '|'.join(f'(?P<{nombre}>{patron})' for nombre, patron in tokens.items())

def analizar_codigo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            codigo = archivo.read()

        print(f"\nAnalizando archivo: {nombre_archivo}\n")

        for match in re.finditer(token_regex, codigo):
            tipo = match.lastgroup
            valor = match.group(tipo)

            if tipo != 'ESPACIO':
                print(f"✔ Token reconocido: {valor} -> {tipo}")

        print("\n✅ Análisis léxico completado con éxito.")

    except FileNotFoundError:
        print(f"❌ Error: El archivo '{nombre_archivo}' no existe.")

if __name__ == "__main__":
    analizar_codigo("src/programa.txt")
