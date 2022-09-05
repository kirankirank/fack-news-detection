from flask import Flask,render_template, request
import pickle
import nltk
import pandas
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.feature_extraction.text import TfidfVectorizer 
data = pandas.read_csv('C:/Users/kiran/Desktop/projrct_text/all_ok.csv')
lr = pickle.load(open("pred.pkl", "rb"))
tfidf = TfidfVectorizer()
tfidf.fit(data['title'])
from nltk.stem import WordNetLemmatizer
lem = WordNetLemmatizer()
def sen_pre(sen):
    perfect_sen = []
    sent = re.sub("[^A-Za-z" "]+", " ", str(sen)).lower()
    sentence = word_tokenize(sent)
    for a in sentence:
        if len(a) >= 3:
            word = lem.lemmatize(a) 
            perfect_sen.append(word)       
    return perfect_sen  
app = Flask(__name__)
@app.route('/')
def starting():
    return render_template("index_text.html")
@app.route("/pred", methods = ["POST", "GET"])
def predict():
    if request.method == "POST":
        message = request.form["message"]
        message = sen_pre(message)
        tfidf_sen = tfidf.transform(message)
        output = lr.predict(tfidf_sen)
    return render_template("index_text.html", pred = output)    
if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask,render_template, request
import pickle
import nltk
import pandas
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.feature_extraction.text import TfidfVectorizer 
data = pandas.read_csv('C:/Users/kiran/Desktop/projrct_text/all_ok.csv')
lr = pickle.load(open("pred.pkl", "rb"))
tfidf = TfidfVectorizer()
tfidf.fit(data['title'])
from nltk.stem import WordNetLemmatizer
lem = WordNetLemmatizer()
def sen_pre(sen):
    perfect_sen = []
    sent = re.sub("[^A-Za-z" "]+", " ", str(sen)).lower()
    sentence = word_tokenize(sent)
    for a in sentence:
        if len(a) >= 3:
            word = lem.lemmatize(a) 
            perfect_sen.append(word)       
    return perfect_sen  
app = Flask(__name__)
@app.route('/')
def starting():
    return render_template("index_text.html")
@app.route("/pred", methods = ["POST", "GET"])
def predict():
    if request.method == "POST":
        message = request.form["message"]
        message = sen_pre(message)
        tfidf_sen = tfidf.transform(message)
        output = lr.predict(tfidf_sen)
    return render_template("index_text.html", pred = output)    
if __name__ == '__main__':
    app.run()

