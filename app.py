import streamlit as st
import pandas as pd
import pickle
import plotly.express as px
import plotly.graph_objects as go
import time

st.set_page_config(page_title="Transformer Monitoring System", layout="wide")

# -------------------------
# LOAD MODEL & DATA
# -------------------------

with open("model.pkl","rb") as f:
    model = pickle.load(f)

data = pd.read_csv("transformer_data.csv")

st.title("🇮🇳 AI-Based Transformer Health Monitoring & Failure Prediction System")

# -------------------------
# SIDEBAR - DISTRICT & TRANSFORMER
# -------------------------

st.sidebar.header("Control Panel")

district_list = sorted(data["District"].unique())
selected_district = st.sidebar.selectbox("Select District", district_list)

district_data = data[data["District"] == selected_district]

transformer_list = district_data["Transformer_ID"].values
selected_transformer = st.sidebar.selectbox("Select Transformer ID", transformer_list)

selected_row = district_data[district_data["Transformer_ID"] == selected_transformer]

# -------------------------
# SHOW TRANSFORMER DETAILS
# -------------------------

st.subheader("📋 Selected Transformer Details")
st.dataframe(selected_row)

# -------------------------
# PREDICTION SECTION
# -------------------------

input_data = selected_row[["Load_kW","Temp_C","Voltage","Oil_Level","Age_Years"]]

if st.sidebar.button("Predict Transformer Health"):

    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]

    st.subheader("🔎 Prediction Result")

    # -------------------------
    # RISK GAUGE
    # -------------------------

    st.subheader("⚡ Risk Meter")

    fig_gauge = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = probability * 100,
        title = {'text': "Failure Risk (%)"},
        gauge = {
            'axis': {'range': [0, 100]},
            'bar': {'color': "red"},
            'steps': [
                {'range': [0, 40], 'color': "green"},
                {'range': [40, 70], 'color': "yellow"},
                {'range': [70, 100], 'color': "red"}
            ],
        }
    ))

    st.plotly_chart(fig_gauge)

    # -------------------------
    # ALERT LOGIC
    # -------------------------

    if prediction == 1:
        st.error(f"⚠ HIGH RISK! Failure Probability: {probability*100:.2f}%")

        st.warning("🚨 Transformer Disconnected for Protection")

        countdown = st.empty()

        for i in range(5,0,-1):
            countdown.write(f"Restarting in {i} seconds...")
            time.sleep(1)

        st.success("✅ Transformer Restored Successfully!")

    else:
        st.success(f"🟢 Transformer Healthy. Failure Probability: {probability*100:.2f}%")

# -------------------------
# DISTRICT RISK SUMMARY
# -------------------------

st.subheader("📊 District Risk Summary")

district_summary = data.groupby("District")["Failure"].sum().reset_index()

fig_district = px.bar(
    district_summary,
    x="District",
    y="Failure",
    title="Number of High-Risk Transformers per District",
    color="Failure"
)

st.plotly_chart(fig_district)

# -------------------------
# MODEL COMPARISON
# -------------------------

st.subheader("📈 Model Accuracy Comparison")

model_names = ["Logistic Regression", "Random Forest", "XGBoost"]
accuracies = [0.92, 1.0, 1.0]  # Replace with your actual values

fig_comp = px.bar(
    x=model_names,
    y=accuracies,
    labels={'x':'Model','y':'Accuracy'},
    title="Model Accuracy Comparison",
    color=accuracies
)

st.plotly_chart(fig_comp)

# -------------------------
# FOOTER
# -------------------------

st.markdown("---")
st.markdown("Developed for Smart Grid & Rural Power Infrastructure Enhancement 🇮🇳")