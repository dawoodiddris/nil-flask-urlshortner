from flask import Flask,render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html", name="Jane Doe")

@app.route('/your-url', methods=['POST','GET'])
def yoururl():
    if request.method == "POST":
       return render_template("yoururl.html", url=request.form['shorturl'])
    else:
        return redirect('/')   
