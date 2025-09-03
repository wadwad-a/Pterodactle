from flask import Flask, render_template
import pandas as pd
import datetime, random

app = Flask(__name__)

dinoDF = pd.read_csv('data.csv')
dino_names = dinoDF['name'].dropna().tolist()
dinos = dinoDF.to_dict(orient="records")

# Global state
daily_dino = None
last_date = None

def pick_daily_dino():
    return random.choice(dinos)

def get_daily_dino():
    global daily_dino, last_date
    today = datetime.date.today()

    # If we haven't picked yet or the day changed, pick a new one
    if last_date != today:
        daily_dino = pick_daily_dino()
        last_date = today
    return daily_dino

@app.route("/")
def index():
    daily_dino = get_daily_dino()
    return render_template(
        "index.html",
        dino_names=dino_names,
        dinos=dinos,
        daily_dino=daily_dino
    )

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)