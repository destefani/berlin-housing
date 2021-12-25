import joblib
import numpy as np
import pandas as pd
import streamlit as st


st.title("Berlin Rent Price Estimator")

st.write("""
Enter the information you have about the appartment you want to evaluate.
The model will calculate an estimated rent for the property.
""")


with st.form("Information"):
    quarter = st.selectbox(
        "Quarter?",
      (['Neukölln (Neukölln)', 'Wedding (Wedding)',
       'Friedrichshain (Friedrichshain)', 'Kreuzberg (Kreuzberg)',
       'Treptow (Treptow)', 'Mitte (Mitte)',
       'Prenzlauer Berg (Prenzlauer Berg)', 'Lichtenberg (Lichtenberg)',
       'Schöneberg (Schöneberg)', 'Tiergarten (Tiergarten)',
       'Plänterwald (Treptow)']))

    number_rooms = st.number_input("Number of rooms")
    
    private_offer = st.selectbox(
        "Is it a private offer?",
        ("Yes", "No"))
    
    living_space = st.number_input("The area in squared meters m2")
    
    builtin_kitchen = st.selectbox(
        "Does it have a built-in kitchen",
        ("Yes", "No"))
    
    balcony = st.selectbox(
        "Does it have a balcony",
        ("Yes", "No"))
    
    energy_certificate = st.selectbox(
        "Does it have an energy certificate?",
        ("Yes", "No"))
    
    has_new_flag = st.selectbox(
        "Is it listed as a new building?",
        ("Yes", "No"))
    
    garden = st.selectbox(
        "Does it have a garden?",
        ("Yes", "No"))

    submitted = st.form_submit_button("Submit")

if submitted:

    bool_dict = {
        "Yes": True,
        "No": False
    }

    data = {
        "balcony": bool_dict[balcony],
        "builtin_kitchen": bool_dict[builtin_kitchen],
        "energy_certificate": bool_dict[energy_certificate],
        "has_new_glag": bool_dict[has_new_flag],
        "living_space": living_space,
        "number_rooms": number_rooms,
        "private_offer": bool_dict[private_offer],
        "quarter": quarter,
        "garden": bool_dict[garden]
    }


    data_pipeline = joblib.load("data_pipeline.pkl")
    data_array = pd.DataFrame.from_dict([data])
    data_transformed = data_pipeline.transform(data_array)

    clf = joblib.load("housing_model.pkl")
    pred = clf.predict(data_transformed)

    st.markdown(f"## Estimated rent: {int(pred)}€")
