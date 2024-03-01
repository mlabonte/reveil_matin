import threading
from flask import Flask, render_template, request
from ecran import get_ecran
from reveil_matin import get_reveil_matin

app = Flask(__name__)

def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

@app.route('/', methods=['POST', 'GET'])
def index():
    name = "Toto"
    if request.method == 'POST':
        name = request.form.get('action', "no action")
        get_ecran().afficher_text(name)
        if name == "Play":
            get_reveil_matin().play()
        elif name == "Stop":
            get_reveil_matin().stop()
        elif name == "Vol+":
            get_reveil_matin().monte_le_son()
        elif name == "Vol-":
            get_reveil_matin().baisse_le_son()
        elif name == "Parler":
            get_reveil_matin().parle(
                request.form.get('paroles', "kouakoubé")
            )
        elif name == "kill":
            shutdown_server()
    return render_template('index.html', name=name)

def lancer_serveur():
    app.run(debug=False, host='0.0.0.0', port=5000, use_reloader=False)

if __name__ == '__main__':
    lancer_serveur()
    
