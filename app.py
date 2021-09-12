from flask import Flask, request, jsonify, render_template
from profanity_filter import ProfanityFilter
import spacy
import en_core_web_sm
nlp = en_core_web_sm.load()

app = Flask(__name__)

@app.route('/')
def home():
    return '''Safe forum'''

@app.route('/predict/<string:txt>',methods=['GET'])
def predict(txt):
    '''
    For rendering results on HTML GUI
    '''

    # str_features = request.form.values()
    pf = ProfanityFilter()
    # postStr = list(str_features)
    output = pf.censor(txt)

    return jsonify({'txt': output})

if __name__ == "__main__":
    app.run(debug=True)



