# ⚡ AI-Based Transformer Health Monitoring & Failure Prediction

A machine-learning system that predicts the **failure risk of distribution transformers** from their operating conditions, with an interactive **Streamlit dashboard** for monitoring transformers district by district. Built with smart-grid and rural power infrastructure in mind.

## ✨ Features
- **Failure prediction** from five operating parameters: load (kW), temperature (°C), voltage, oil level and age
- **Model comparison**: Logistic Regression vs. Random Forest (scikit-learn); the better model is saved and used for prediction
- **Interactive dashboard** (Streamlit + Plotly):
  - Select a district and transformer ID from the control panel
  - Failure-risk gauge (green / yellow / red zones)
  - High-risk alert with a simulated protective disconnect and restore
  - District-wise summary of high-risk transformers
- **Data API** (Flask): a small server that receives and serves live readings as JSON

## 🛠️ Tech Stack
Python · pandas · NumPy · scikit-learn · Streamlit · Plotly · Flask

## 📁 Project Structure
| File | Purpose |
|---|---|
| `generate_data.py` | Generates a synthetic dataset of 3,000 transformers (`transformer_data.csv`) |
| `train_model.py` | Trains Logistic Regression and Random Forest models and saves the best one to `model.pkl` |
| `app.py` | Streamlit dashboard for monitoring and prediction |
| `server.py` | Flask API to receive (`POST /data`) and read (`GET /get`) live sensor data |
| `transformer.pdf` | Project report |

## 🚀 How to Run
```bash
pip install pandas numpy scikit-learn streamlit plotly flask
python generate_data.py     # create the dataset
python train_model.py       # train and save the model
streamlit run app.py        # launch the dashboard
```

## 📊 How It Works
1. Transformer readings (load, temperature, voltage, oil level, age) are fed to the trained classifier.
2. The model outputs a failure probability, shown on the risk gauge.
3. Transformers above the risk threshold trigger an alert and a simulated disconnection for protection.

## 🔮 Future Scope
- Connect real sensors (e.g., via a microcontroller) to the Flask API for live monitoring
- Train on real field data from utilities
- SMS / email alerts for maintenance teams

## 👩‍💻 Author
**Nandini Madugula** — B.Tech Electrical & Computer Engineering, Amrita Vishwa Vidyapeetham, Coimbatore
[LinkedIn](https://www.linkedin.com/in/madugula-nandini)
