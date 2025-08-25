from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

dinoDF = pd.read_csv('data.csv')
dino_names = dinoDF['name'].dropna().tolist()

@app.route("/")
def index():
    return render_template("index.html", dino_names=dino_names)

if __name__ == "__main__":
    app.run(debug=True)