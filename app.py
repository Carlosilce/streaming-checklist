from flask import Flask, render_template

app = Flask(__name__)

checklist = {
    "Infraestructura y Hardware": [
        {
            "id": "1.1",
            "titulo": "Capturadora Blackmagic",
            "descripcion": "Drivers de audio y video cargados correctamente."
        },
        {
            "id": "1.2",
            "titulo": "Flujo de Video y Audio",
            "descripcion": "Prueba de flujo constante de video y señal de audio."
        },
        {
            "id": "1.3",
            "titulo": "Hardware General",
            "descripcion": "Monitoreo de memoria RAM y CPU."
        },
        {
            "id": "1.4",
            "titulo": "Software vMix",
            "descripcion": "Inicio de aplicación en ambos equipos."
        },
        {
            "id": "1.5",
            "titulo": "Recepción de Señal",
            "descripcion": "Verificación de señal recibida por Audiovisual."
        }
    ],
    "Conectividad y Red": [
        {
            "id": "2.1",
            "titulo": "Cableado físico",
            "descripcion": "Verificación de conexión HDMI entre equipo principal y secundario."
        },
        {
            "id": "2.2",
            "titulo": "Red LAN/Ethernet",
            "descripcion": "Verificación de conexión alámbrica directa."
        },
        {
            "id": "2.3",
            "titulo": "Prueba de Banda Ancha",
            "descripcion": "Speedtest en ambos equipos."
        }
    ],
    "Facebook Meta": [
        {
            "id": "3.1",
            "titulo": "Eliminación Evento Previo",
            "descripcion": "Confirmación con COLNAL de eliminación del evento anterior."
        },
        {
            "id": "3.2",
            "titulo": "Creación Evento Facebook",
            "descripcion": "Creación del nuevo evento en Live Producer, (minimo 2 hrs antes del inicio)."
        },
        {
            "id": "3.3",
            "titulo": "Confirmación de Indexado",
            "descripcion": "Validar visibilidad del evento en el perfil de Facebook."
        }
    ],
    "vMix y Producción": [
        {
            "id": "4.1.1",
            "titulo": "Carga y prueba de fuentes fijas y Gráficos",
            "descripcion": "Plecas, cintillos y anuncios."
        },
        {
            "id": "4.1.2",
            "titulo": "Carga y prueba de Reproductores Multimedia",
            "descripcion": "Videos cortos y largos."
        },
        {
            "id": "4.1.3",
            "titulo": "Salida HDMI",
            "descripcion": "Señal vestida hacia equipo secundario."
        },
        {
            "id": "4.1.4",
            "titulo": "Configuración de encoders RTMP YouTube y X",
            "descripcion": "Configuración de streaming para emisión directa."
        },
        {
            "id": "4.2.1 Equipo Secundario",
            "titulo": "Recepción HDMI",
            "descripcion": "Recepción de señal del equipo principal, ya vestida."
        },
        {
            "id": "4.2.2 Equipo Secundario",
            "titulo": "RTMP Facebook",
            "descripcion": "Configuración de encoder para emisión Facebook Live."
        },
        {
            "id": "4.2.3",
            "titulo": "Cortinilla Contingencia",
            "descripcion": "Carga de banner de emergencia."
        },
        {
            "id": "4.2.4",
            "titulo": "Prueba Auditiva",
            "descripcion": "Validar el audio en Monitoreo con audífonos."
        },
        {
            "id": "4.2.5",
            "titulo": "Apertura Plataformas",
            "descripcion": "YouTube, X y Facebook para inicio de transmisiones."
        }
    ],
    "Crossposting y Monitoreo": [
        {
            "id": "5.1",
            "titulo": "Crossposting",
            "descripcion": "Validar si la transmisión incluye transmisiones cruzadas."
        },
        {
            "id": "5.2",
            "titulo": "Lista de Monitoreo",
            "descripcion": "Envío de captura de imagen a personal de monitoreo -Gil -Liza -Ivan -Carlos."
        },
        {
            "id": "5.3",
            "titulo": "Canal de Alertas",
            "descripcion": "Grupo de comunicación activo Whatsapp etc."
        }
    ],
    "Seguridad y Contingencia": [
        {
            "id": "6.1",
            "titulo": "Datos Emergencia",
            "descripcion": "Datos disponibles a la mano para recreación de eventos."
        },
        {
            "id": "6.2",
            "titulo": "Sin Notificaciones",
            "descripcion": "Validar que Windows Update y notificaciones suspendidas y exclusivo TX."
        },
        {
            "id": "6.3",
            "titulo": "Cámaras y Multistream",
            "descripcion": "Validación de cámaras, encuadre enfoque e ingesta y el envío de Multistream."
        },
        {
            "id": "6.4",
            "titulo": "Seguridad Streaming",
            "descripcion": "Validar la Configuración redundante en ambos equipos."
        }
    ]
}

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/checklist")
def checklist_view():
    return render_template("checklist.html", checklist=checklist, inspection_mode=False)

@app.route("/inspeccion")
def inspeccion():
    return render_template("checklist.html", checklist=checklist, inspection_mode=True)

if __name__ == "__main__":
    app.run(debug=True)