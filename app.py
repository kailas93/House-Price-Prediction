from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np

# Initialize Flask app
app = Flask(__name__)

# Load trained model
try:
    with open("best_linear_regression.pkl", "rb") as model_file:
        model = pickle.load(model_file)
    print("✅ Model loaded successfully!")
except Exception as e:
    print(f"❌ Error loading model: {e}")
    model = None

# Home route - Shows input form
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        try:
            # Get user input from form
            features = [float(request.form[key]) for key in 
                        ["MedInc", "HouseAge", "AveRooms", "AveBedrms", "Population", "AveOccup", "Latitude", "Longitude"]]
            
            # Convert to numpy array and reshape for prediction
            features = np.array(features).reshape(1, -1)
            
            # Predict house price
            if model is not None:
                prediction = model.predict(features)[0]
                predicted_price = round(prediction, 2)  # Round result
                return render_template("index.html", prediction=f"Predicted Price: ${predicted_price}")
            else:
                return render_template("index.html", prediction="Model not loaded. Please check the server logs.")
        except Exception as e:
            return render_template("index.html", prediction=f"Error: {str(e)}")

    return render_template("index.html", prediction=None)

# **API Endpoint for JSON Input**
@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Ensure JSON input is received
        data = request.get_json()
        if data is None:
            return jsonify({"error": "Invalid JSON format"}), 400
        
        # Required fields
        required_fields = ["MedInc", "HouseAge", "AveRooms", "AveBedrms", "Population", "AveOccup", "Latitude", "Longitude"]
        
        # Check if all required fields are present
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return jsonify({"error": "Missing required fields", "missing_fields": missing_fields}), 400

        # Convert to NumPy array
        features = np.array([data[field] for field in required_fields]).reshape(1, -1)

        # Predict house price
        if model is not None:
            prediction = model.predict(features)[0]
            return jsonify({"prediction": round(prediction, 2)})
        else:
            return jsonify({"error": "Model not loaded. Please check the server logs."}), 500

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Handle GET requests to /predict (Avoid 405 errors)
@app.route("/predict", methods=["GET"])
def predict_get():
    return jsonify({"message": "Use POST method with JSON data to get predictions"}), 405

# Run Flask app
if __name__ == "__main__":
    print("🚀 Flask app running at: http://127.0.0.1:8080/")
    app.run(debug=True, port=8080)