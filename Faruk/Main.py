from flask import Flask, render_template
import random
import speech

app = Flask(__name__)



@app.route("/")
def hello_world():
    return render_template('index.html')


@app.route("/rastgele_mizah")
def rasgele():
    liste = ["rüzgar muz yiyo Emir elmayedi Rüzgar muzunu düşürdü Emir BRUH","aaaaa","sen naaptın?","bi adam varmış ama varamamış"]

    x = random.choice(liste)

    return render_template('rasgele.html',x=x)

@app.route("/rastgele_gercek")
def rasgele1():
    liste = ["eğer bir sayının sonundaki sayı çiftsayıysa 2 ye kalansız bölünür","eğer bir sayının rakamları toplamı 3 veya 3ün katıysa 3 e bölünür","en zengin insan ELON MUSK'tur","2022 yılında galatasaray süperlig'de şampiyon oldu"]

    x = random.choice(liste)

    return render_template('rasgele.html',x=x)

@app.route("/aciklama")
def info():
    return render_template('aciklama.html')
@app.route("/gorsel solen")
def hee():
    return render_template('gorsel solen.html')

@app.route("/oyun1")
def oyun1():
    return render_template('oyun1.html')

@app.route("/oyun2")
def oyun2():
    return render_template('oyun1 copy.html')

@app.route("/oyun3")
def oyun3():
    return render_template('oyun1 copy 2.html')

@app.route("/oyun4")
def hee1():
    return render_template('oyun1 copy 3.html')

@app.route("/oyun5")
def oyun11():
    return render_template('oyun1 copy 4.html')

@app.route("/oyun6")
def oyun21():
    return render_template('oyun1 copy 5.html')

@app.route("/oyun7")
def oyun31():
    return render_template('oyun1 copy 6.html')

@app.route("/oyun8")
def oyun32():
    return render_template('oyun1 copy 7.html')

@app.route("/oyun9")
def oyun34():
    return render_template('oyun1 copy 8.html')

@app.route("/oyun10")
def oyun35():
    return render_template('oyun1 copy 9.html')

@app.route("/oyun11")
def oyun36():
    return render_template('oyun1 copy 10.html')

@app.route("/oyun12")
def oyun37():
    return render_template('oyun1 copy 11.html')

@app.route("/oyun13")
def oyun38():
    return render_template('oyun1 copy 12.html')

@app.route("/oyun14")
def oyun39():
    return render_template('oyun1 copy 13.html')

@app.route("/oyun15")
def oyun30():
    return render_template('oyun1 copy 14.html')

@app.route("/oyun16")
def oyun312():
    return render_template('oyun1 copy 15.html')

@app.route("/oyun17")
def oyun313():
    
    return render_template('oyun1 copy 16.html')
    

@app.route("/oyun18")
def oyun311():
    return render_template('oyun1 copy 17.html')

@app.route("/oyun19",methods=["POST"])
def oyun315():
    a = speech.speech_tr()
    print (a)
    return render_template('oyun1 copy 18.html',a = a.lower())

@app.route("/oyun20")
def oyun317():
    return render_template('oyun1 copy 19.html')


app.run(debug=True)