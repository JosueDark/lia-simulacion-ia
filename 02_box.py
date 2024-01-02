import speech_recognition as sr
import pyttsx3

# Instanciando Objetos
reconocedor = sr.Recognizer()
motor_convertidor = pyttsx3.init()

# Modificacion de la voz y la velocidad del motor de Pyttsx3

# Obtener una lista de voces disponibles
voices = motor_convertidor.getProperty('voices')
# Seleccionar una voz específica (puedes cambiar el índice según tus necesidades)
selected_voice = voices[0]
motor_convertidor.setProperty('voice', selected_voice.id)
# Configurar la velocidad (opcional)
motor_convertidor.setProperty('rate', 150)  # Ajusta la velocidad según tus preferencias

# Ver si ya esta escuchando
motor_convertidor.say('Hola, Jeferson, Como estas, en que puedo ayudarte hoy.')
motor_convertidor.runAndWait()

# Variables
conversacion_vigente = True # Si usuario dice Finaliza con Adios, Chapi... esto cambiara a false

# Funcion que ejecuta las tareas que indiquemos
def tareas(tarea):

    tareas_disponibles = ['saludar', 'abre excel'] # Lista de 10 Tareas disponibles
    
    if tarea == 'saludar':
        motor_convertidor.say(f'Ejecutando {tarea}')
        motor_convertidor.say('Hola Jeferson Como estas.')

    
    motor_convertidor.runAndWait()

# Funcion para escuchar...
def escuchar():

    with sr.Microphone() as source:

        print('Esperando Instruccion...')

        # Para la adaptacion del ruido ambiental
        reconocedor.adjust_for_ambient_noise(source)

        # Para Escuchar
        audio = reconocedor.listen(source)

    # Errores que puedan ocurrrir
    try:
        tarea = reconocedor.recognize_google(audio, language='es-ES').casefold()
        print(f'Instruccion dada: {tarea}')
        tareas(tarea)

    except sr.UnknownValueError:
        print('No se pudo entender el comando')

    except sr.RequestError as e:
        print(f'Error al realizar la solicitud: {e}')

while True:
    escuchar()
# Activar la asistente de voz
