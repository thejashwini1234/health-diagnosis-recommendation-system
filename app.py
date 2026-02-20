from flask import Flask, render_template
from symptom_checker import symptom_checker
from home_remedies import home_remedies
from hospital_recommendation import hospital_recommendation

app = Flask(__name__)

# Register blueprints
app.register_blueprint(symptom_checker, url_prefix="/symptom_checker")
app.register_blueprint(home_remedies, url_prefix="/home_remedies")
app.register_blueprint(hospital_recommendation, url_prefix="/hospital_recommendation")

@app.route("/")
def home():
    return render_template("index.html")
@app.route('/kn')
def home_kn():
    return render_template('index_kn.html')


if __name__ == "__main__":
    app.run(debug=True)
