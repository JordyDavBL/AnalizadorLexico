import re

# Definición de tokens con prioridad adecuada
tokens = {
    'PALABRA_RESERVADA': r'\b(inicio|fin|imprimir|leer|si|sino|mientras)\b',
    'OPERADOR_RELACIONAL': r'(==|!=|<=|>=|<|>)',
    'NUMERO': r'\b\d+(\.\d+)?\b',
    'IDENTIFICADOR': r'\b[a-zA-Z_][a-zA-Z0-9_]*\b',
    'ASIGNACION': r'=',
    'OPERADOR_ARITMETICO': r'[+\-*/]',
    'PUNTOYCOMA': r';',
    'PARENTESIS_ABRE': r'\(',
    'PARENTESIS_CIERRA': r'\)',
    'LLAVE_ABRE': r'\{',
    'LLAVE_CIERRA': r'\}',
    'ESPACIO': r'\s+',
}

# Compilar expresiones regulares
token_regex = '|'.join(f'(?P<{nombre}>{patron})' for nombre, patron in tokens.items())
token_pattern = re.compile(token_regex)

def analizar_codigo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            codigo = archivo.read()

        print(f"\nAnalizando archivo: {nombre_archivo}\n")

        # Posición del cursor en el texto
        pos = 0
        while pos < len(codigo):
            match = token_pattern.match(codigo, pos)
            if match:
                tipo = match.lastgroup
                valor = match.group(tipo)

                if tipo != 'ESPACIO':  # Ignorar espacios
                    print(f"✔ Token reconocido: {valor} -> {tipo}")

                pos = match.end()
            else:
                # No se reconoció ningún token válido
                print(f"❌ Token no reconocido: {codigo[pos]}")
                pos += 1  # Avanzar un carácter para continuar el análisis

        print("\n✅ Análisis léxico completado.")

    except FileNotFoundError:
        print(f"❌ Error: El archivo '{nombre_archivo}' no existe.")

if __name__ == "__main__":
    analizar_codigo("src/programa2.txt") 