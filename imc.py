#realizzzare un sito web che tramite js calcoli l'indice di massa corporea il sito deve essere in italiano e in inglese, utente inserisce peso e altezza e il programma risponde con il calcolo di imc un resposo msotto peso normo... e un immagine adatta
from flask import Flask , render_template
app= Flask(__name__)

@app.route('/')
@app.route('/it')
def italiano():
   return render_template('indeximc.html', titolo= 'Calcola imc', h1='Calcola il tuo imc', testo='Inserire la tua altezza ed il tuo peso per avere il calcolo ed il responso sul tuo imc',peso= 'inserire peso', altezza='inserire altezza', Inizia='Inizia')

@app.route('/en')
def ing():
    return render_template('indeximc.html',titolo= 'Calculate imc', h1='Calculate imc', testo='Give your height and your weight, the iste give you a response', Inizia='Start')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)