from flask import Flask, request, jsonify, render_template
from profanity_filter import ProfanityFilter

# import en_core_web_sm
# nlp = en_core_web_sm.load()

app = Flask(__name__)

@app.route('/')
def home():
    return '''Safe forum'''

@app.route('/predict/',methods=['GET']) #<string:txt>
def predict():
    '''
    For rendering results on HTML GUI
    '''
    txt = "Fuck"
    # str_features = request.form.values()
    pf = ProfanityFilter()
    # postStr = list(str_features)
    output = pf.censor(txt)

    return jsonify({'txt': output})

if __name__ == "__main__":
    app.run(debug=True)



