# PysingScan

App de ciberseguridad en segundo plano que detecta contenido peligroso en tiempo real usando inteligencia artificial.

Detecta si hay texto copiado al portapapeles o capturado con OCR. Procesa el texto con técnicas de IA y PNL.

Lanza alertas al usuario si detecta contenido sensible, fraudulento o riesgoso (ej: datos sensible,  condiciones abusivas en contratos o phishing encubierto).

---

Detección de palabras/frases clave: “compartimos datos”, “sin derecho a eliminar”, “cesión permanente”, etc. 

Modelos de clasificación: entrenar uno que identifique párrafos problemáticos. 
Resumen automático: usar sumy, transformadores, etc., para extraer lo más importante. 

| Necesidad                  | Herramienta 
| ---                        | --- 
| Analizar lenguaje          | spaCy, transformadores, nltk 
| Backend API                | FastAPI, Flask 
| Interfaz gráfica (Windows) | tkinter, PyQt, customtkinter 
| Leer texto de pantalla     | pytesseract (OCR), pyperclip (portapapeles) 
| Extensión navegador        | JavaScript + Python backend

---

## Puesta en marcha

```bash
# Crear el entorno virtual
python -m venv .venv

# Activar el entorno virtual
source .venv/bin/activate

# Instalar requerimientos

pip install -r requirements.txt

```