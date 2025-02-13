import joblib
import gradio as gr

# Load pre-trained models
naive_bayes_model = joblib.load('/content/gender_naive_bayes_model.joblib')
random_forest_model = joblib.load('/content/gender_random_forest_model.joblib')
logistic_regression_model = joblib.load('/content/gender_logistic_regression_model.joblib')

def predict_gender(name, model_choice):
    """
    Predicts the gender for a given name using the selected model.
    
    Parameters:
        name (str): The input name.
        model_choice (str): The model to use ("Naive Bayes", "Random Forest", "Logistic Regression").
    
    Returns:
        tuple: Predicted gender and the confidence level.
    """
    if model_choice == "Naive Bayes":
        predicted_gender = naive_bayes_model.predict([name])[0]
        probabilities = naive_bayes_model.predict_proba([name])[0]
        confidence = max(probabilities)
    elif model_choice == "Random Forest":
        predicted_gender = random_forest_model.predict([name])[0]
        probabilities = random_forest_model.predict_proba([name])[0]
        confidence = max(probabilities)
    elif model_choice == "Logistic Regression":
        predicted_gender = logistic_regression_model.predict([name])[0]
        probabilities = logistic_regression_model.predict_proba([name])[0]
        confidence = max(probabilities)
    else:
        return "Invalid model choice", 0.0

    return predicted_gender, confidence

# Footer HTML for displaying developer information and social links
footer_html = """
<footer style="text-align: center; margin-top: 20px; font-family: Arial, sans-serif;">
  <p>Developed ❤️ with Gradio by DINESH S.</p>
  <div style="display: inline-flex; align-items: center; justify-content: center; gap: 10px; margin-top: 10px;">
    <h3>Connect with me:</h3>
    <a href="https://www.linkedin.com/in/dinesh-x/" target="_blank">
      <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" alt="LinkedIn" style="width:32px;">
    </a>
    <a href="https://github.com/itzdineshx/Data_Play_Fellowship" target="_blank">
      <img src="https://upload.wikimedia.org/wikipedia/commons/9/91/Octicons-mark-github.svg" alt="GitHub" style="width:32px;">
    </a>
  </div>
  <script>console.log("Footer HTML loaded successfully.");</script>
</footer>
"""

# Create the Gradio interface
iface = gr.Interface(
    fn=predict_gender,
    inputs=[
        gr.Textbox(lines=1, placeholder="Enter a name here...", label="Name"),
        gr.Radio(["Naive Bayes", "Random Forest", "Logistic Regression"], label="Choose a Model")
    ],
    outputs=[
        gr.Textbox(label="Predicted Gender"),
        gr.Number(label="Confidence")
    ],
    title="Gender Prediction👫",
    description="Predict the gender based on a given name using different Machine Learning models.",
    article=footer_html 
)

# Launch the app
iface.launch()
