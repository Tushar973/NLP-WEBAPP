from flask import Flask,render_template,request,redirect,session
from db import Database
import api
from textblob import TextBlob 
from api import document_qa
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

app.secret_key = "123456789"


dbo = Database()

UPLOAD_FOLDER = "uploads"
ALLOWED_EXTENSIONS = {"pdf", "txt", "docx"}

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/perform_registration',methods=['post'])
def perform_registration():
    name = request.form.get('user_ka_name')
    email = request.form.get('user_ka_email')
    password = request.form.get('user_ka_password')

    response = dbo.insert(name, email, password)

    if response:
        return render_template('login.html',message="Registration Successful. Kindly login to proceed")
    else:
        return render_template('register.html',message="Email already exists")

@app.route('/perform_login',methods=['post'])
def perform_login():
    email = request.form.get('user_ka_email')
    password = request.form.get('user_ka_password')

    response = dbo.search(email, password)

    if response:
        session['logged_in'] = 1
        return redirect('/profile')
    else:
        return render_template('login.html',message='incorrect email/password')

@app.route('/profile')
def profile():
    if session:
        return render_template('profile.html')
    else:
        return redirect('/')

@app.route('/ner')
def ner():
    if session:
        return render_template('ner.html')
    else:
        return redirect('/')

@app.route('/perform_ner',methods=['post'])
def perform_ner():
    if session:
        text = request.form.get('ner_text')
        response = api.ner(text)
        print(response)


        return render_template('ner.html',response=response)
    else:
        return redirect('/')
@app.route('/sentiment')
def sentiment_page():
    if session:
        return render_template('sentiment.html')
    else:
        return redirect('/')


@app.route('/perform_sentiment', methods=['post'])
def perform_sentiment():
    if session:
        text = request.form.get('sent_text')
        result = api.sentiment(text)
        return render_template('sentiment.html', result=result)
    else:
        return redirect('/')


@app.route('/abuse')
def abuse_page():
    if session:
        return render_template('abuse.html')
    else:
        return redirect('/')


@app.route('/perform_abuse', methods=['post'])
def perform_abuse():
    if session:
        text = request.form.get('abuse_text')
        result = api.abuse_detection(text)
        return render_template('abuse.html', result=result)
    else:
        return redirect('/')
    
@app.route('/document_qa')
def document_qa_page():
    if session:
        return render_template('document-qa.html')
    else:
        return redirect('/')

@app.route('/perform_document_qa', methods=['post'])
def perform_document_qa():
    if session:
        file = request.files.get('document')
        question = request.form.get('question')

        if not file or file.filename == '':
            return render_template(
                'document-qa.html',
                error="Please upload a document"
            )

        if not allowed_file(file.filename):
            return render_template(
                'document-qa.html',
                error="Unsupported file type"
            )

        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        file_type = filename.rsplit('.', 1)[1].lower()
        result = document_qa(file_path, file_type, question)

        os.remove(file_path)

        return render_template(
            'document-qa.html',
            answer=result.get('answer'),
            confidence=result.get('confidence')
        )
    else:
        return redirect('/')



app.run(debug=True)


##ADDED HASHING FEATURE