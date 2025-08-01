import joblib
from flask import Flask, render_template, request
import numpy as np 
from config.path_config import MODEL_OUTPUT_PATH


app = Flask(__name__)

loaded_model = joblib.load(MODEL_OUTPUT_PATH)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get input values from the form
        lead_time = int(request.form["lead_time"])
        no_of_special_requests = int(request.form["no_of_special_requests"])
        avg_price_per_room = float(request.form["avg_price_per_room"])
        arrival_month = int(request.form["arrival_month"])
        arrival_date = int(request.form["arrival_date"])
        market_segment_type = int(request.form["market_segment_type"])
        no_of_week_nights = int(request.form["no_of_week_nights"])
        no_of_weekend_nights = int(request.form["no_of_weekend_nights"])
        type_of_meal_plan = int(request.form["type_of_meal_plan"])
        room_type_reserved = int(request.form["room_type_reserved"])

        # Prepare the input array for the model
        input_features = np.array([[lead_time, no_of_special_requests, avg_price_per_room,
                                    arrival_month, arrival_date, market_segment_type,
                                    no_of_week_nights, no_of_weekend_nights,
                                    type_of_meal_plan, room_type_reserved]])

        # Make prediction
        prediction = loaded_model.predict(input_features)[0]

        # Render result
        return render_template("index.html", prediction=prediction)

    return render_template("index.html", prediction=None)


if __name__=="__main__":
    app.run(host="0.0.0.0", port=8080)