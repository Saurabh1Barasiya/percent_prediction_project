from flask import Flask,render_template,redirect,url_for,request
import joblib
import math
import numpy as np 
import pyttsx3

app = Flask(__name__)
model  = joblib.load('Stundts_mark_predictor_model.pkl') 
# model = joblib.load(open("model.pkl",'rb')) 

def speak(word):
    word = math.floor(word)
    word = str(word)
    engine = pyttsx3.init()
    engine.say(f"Number of percent should be {word}")
    engine.runAndWait() 
    return

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict',methods = ["POST"])
def predict():
    try:
      int_features = [float(x) for x in request.form.values()]
      final_features = [np.array(int_features)]
    except:
        return render_template('index.html',predition_text = "Please enter numbers only")

    predition = model.predict(final_features)

    output = np.round(predition[0],2)
    output_str = output.copy()
    speak(output_str)
    return render_template('index.html',predition_text = "Number of percent should be {}".format(math.floor(output)))

if __name__ == "__main__":
    app.run()
