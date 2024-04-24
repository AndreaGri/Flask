'''
Realizzare un single page application che permette di avere informazioni sulle regioni italiane.
In un file csv devono essere memorizzate le seguenti informazioni:
-Nome regione
-Nome capoluogo
-Popolazione regione
-Popolazione capoluogo
-Percorso di un immagine relativa alla regione 
-L'applicazione deve permettere all'utente di selezionare da un elenco il nome della regione e deve fornire all'utente 
 tutte le informazioni relative alla regione nonchè il meteo relativo al capoluogo della regione.
Grafica a scelta
'''

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def homepage(): #quetsa rotta restituisce la home page della nostra single page app

 return render_template('homeRegioni.html')

@app.route('/elenco')#elenco regioni
def elenco():
 import pandas as pd
 df=pd.read_csv('/workspace/Flask/data/regioni.csv')
 info= df.nome_regione
 return render_template('json.html', tabella = info.to_json())


@app.route('/info/<nome>')#info regione
def info(nome):
 import pandas as pd
 df=pd.read_csv('/workspace/Flask/data/regioni.csv')
 info=df[df.nome_regione==nome]
 return render_template('json.html', tabella = info.to_json())


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3248, debug=True)