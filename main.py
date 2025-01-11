# Import
from flask import Flask, render_template, request




app = Flask(__name__)

def result_calculate(size, lights, device):
    # Variabili che consentono di calcolare il consumo energetico degli apparecchi
    home_coef = 100
    light_coef = 0.04
    devices_coef = 5   
    return size * home_coef + lights * light_coef + device * devices_coef 

# La prima pagina
@app.route('/')
def index():
    return render_template('index.html')
# La seconda pagina
@app.route('/<size>')
def lights(size):
    return render_template(
                            'lights.html', 
                            size=size
                           )

# La terza pagina
@app.route('/<size>/<lights>')
def electronics(size, lights):
    return render_template(
                            'electronics.html',                           
                            size = size, 
                            lights = lights                           
                           )

# Calcolo
@app.route('/<size>/<lights>/<device>')
def end(size, lights, device):
    return render_template('end.html', 
                            result=result_calculate(int(size),
                                                    int(lights), 
                                                    int(device)
                                                    )
                        )
# Il modulo
@app.route('/form')
def form():
    return render_template('form.html')


#I risultati del modulo
@app.route('/submit', methods=['POST'])
def submit_form():
    # Dichiarare le variabili per la raccolta dei dati
    name = request.form['name']
    address = request.form["address"]
    email = request.form["email"]
    date = request.form["date"]
    # È possibile salvare i dati o inviarli via e-mail
    with open('/Users/davidebaroncelli/Documents/corso python/progetti web/calculator_itl-main/form.txt', 'a',) as form:
        form.write(name + '\n')
        form.write(address + '\n')
        form.write(email + '\n')
        form.write(date + '\n\n')
   
    return render_template('form_result.html', 
                           # Inserire le variabili qui
                           name=name,
                           address=address,
                           email=email,
                           date=date,
                           )



app.run(debug=True)

