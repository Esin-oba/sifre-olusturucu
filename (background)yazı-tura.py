import random
from flask import Flask
app = Flask(__name__)
@app.route("/random-facts")
def hello_world():
    #soru = str(input("Yazı mı? , Tura  mı? Seçiniz!"))
    #print(soru)
    facts_list = ["YAZI", "TURA"]
    return f'<p>{random.choice(facts_list)}</p>'
@app.route("/")
def randomfacts():
    #return f'<a href="/random-facts">soru</a>'
    return f'<a href="/random-facts">Rastgele bir gerçeği görüntüle!</a>'
app.run(debug=True)
