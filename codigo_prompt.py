# 1. Inicia la interacción con el usuario
print("¡Bienvenido a la creación de tarjetas de cumpleaños! Por favor, responde estas preguntas para personalizar tu diseño.")

# 2. Recopila las variables del usuario
formato = input("¿Prefieres un diseño vertical u horizontal? (Opciones: Vertical, Horizontal): ")
colores = input("¿Qué colores deseas para el diseño? (Ejemplo: pastel azul y rosa, tonos vivos, monocromáticos): ")
elementos = input("¿Qué elementos quieres incluir? (Ejemplo: pastel con velas, globos, flores, confeti): ")
estilo = input("¿Qué estilo prefieres? (Opciones: Moderno, Elegante, Infantil, Vintage, Festivo): ")
texto_principal = input("¿Qué mensaje principal deseas? (Ejemplo: '¡Feliz Cumpleaños!', 'Happy Birthday'): ")
espacio_nombre = input("¿Quieres incluir un espacio para personalizar con el nombre del destinatario? (Sí/No): ")
destinatario = input("¿Para quién está dirigida? (Opciones: Niños, Adultos, General): ")
decoraciones = input("¿Qué decoraciones adicionales prefieres? (Ejemplo: marcos dorados, patrones abstractos, confeti): ")
resolucion = input("¿Qué resolución deseas? (Opciones: Alta, Media, Baja): ")

# 3. Define las proporciones en función del formato
if formato.lower() == "vertical":
    proporciones = "10x15 cm, proporción vertical"
else:
    proporciones = "15x10 cm, proporción horizontal"

# 4. Ajusta la resolución
if resolucion.lower() == "alta":
    resolucion_pixels = "1024x1792"
elif resolucion.lower() == "media":
    resolucion_pixels = "512x896"
else:
    resolucion_pixels = "256x448"

# 5. Genera el prompt dinámico
prompt = f"""
A {formato.lower()} birthday card design with a {colores} background and {decoraciones}.
At the center, {elementos}. 
At the top, the text '{texto_principal}' is written in a {estilo.lower()} style. 
{('Below the text, a blank space framed with gold for the recipient\'s name.' if espacio_nombre.lower() == 'sí' else '')}
The card is suitable for {destinatario.lower()} and proportioned to {proporciones}. 
Resolution: {resolucion_pixels} pixels.
"""

# 6. Muestra el prompt generado
print("Tu prompt generado para DALL·E es:")
print(prompt)
