from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/checklist")
def checklist():

    infraestructura = [
        {
            "id": "1.1",
            "titulo": "Capturadora Blackmagic",
            "descripcion": "Drivers de audio y video cargados correctamente."
        },
        {
            "id": "1.2",
            "titulo": "Flujo de Video y Audio",
            "descripcion": "Prueba de flujo constante de video y audio."
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
            "descripcion": "Verificación de señal recibida por audiovisual."
        }
    ]

    conectividad = [
    {
        "id": "2.1",
        "titulo": "Cableado físico",
        "descripcion": "Verificación de conexión HDMI entre ambos equipos."
    },
    {
        "id": "2.2",
        "titulo": "Red LAN/Ethernet",
        "descripcion": "Verificación de conexión alámbrica."
    }
]

    return render_template(
        "checklist.html",
        infraestructura=infraestructura, # Aqui se están enviando las listas de arriba a Jinja
        conectividad=conectividad        # Por seccion y se accede a ellas en el HTML con un for loop
    )

if __name__ == "__main__":
    app.run(debug=True)