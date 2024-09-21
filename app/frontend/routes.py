from flask import Blueprint,request,jsonify,render_template

frontend = Blueprint('Frontend', __name__, url_prefix='/',template_folder='./templates',static_folder="./statics")



@frontend.get("/")
def index():
    return render_template("index.html")

