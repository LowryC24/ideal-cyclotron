import math
import streamlit as st

def calculate_coil_parameters(
    Breq,  # Required magnetic field in Tesla
    gap_mm,  # Pole gap in mm
    I,  # Operating current in A
    cond_side_mm,  # Conductor side length in mm
    cooling_dia_mm,  # Cooling duct diameter in mm
    correction_factor=1,  # Correction factor from excitation curve
    added_turns=10,  # Extra turns added
    num_coils=1,  # Number of coils
    hor_turns=14,  # Horizontal turns (manual selection)
    ver_turns=32  # Vertical turns (manual selection)
):
    # Constants
    mu0 = 1e-6  # H/m (simplified)

    # Convert gap to meters for formula
    gap_m = gap_mm / 1000

    # Conductor area (mm²)
    cond_area = cond_side_mm ** 2 - math.pi * (cooling_dia_mm / 2) ** 2

    # Current density (A/mm²)
    current_density = I / cond_area

    # Ideal number of turns
    turns_required = (Breq * gap_m) / (mu0 * I * correction_factor)

    # Total turns with adjustment
    total_turns = turns_required + added_turns

    # Turns per coil
    turns_per_coil = total_turns / num_coils

    return {
        "Vacuum Permeability (mu0) [H/m]": mu0,
        "Conductor Area [mm^2]": cond_area,
        "Current Density [A/mm^2]": current_density,
        "Ideal Number of Turns": turns_required,
        "Total Turns Used": total_turns,
        "Turns per Coil": turns_per_coil,
        "Horizontal Turns (selected)": hor_turns,
        "Vertical Turns (selected)": ver_turns
    }

# Streamlit app
st.title("90° Double Focus Coil Calculator")

st.sidebar.header("Input Parameters")
Breq = st.sidebar.number_input("Required Magnetic Field Breq (T)", value=0.27)
gap_mm = st.sidebar.number_input("Pole Gap (mm)", value=160)
I = st.sidebar.number_input("Operating Current (A)", value=80)
cond_side_mm = st.sidebar.number_input("Conductor Side Length (mm)", value=8)
cooling_dia_mm = st.sidebar.number_input("Cooling Duct Diameter (mm)", value=5)
correction_factor = st.sidebar.number_input("Correction Factor", value=1.0)
added_turns = st.sidebar.number_input("Added Turns", value=10)
num_coils = st.sidebar.number_input("Number of Coils", value=1)
hor_turns = st.sidebar.number_input("Horizontal Turns (selected)", value=14)
ver_turns = st.sidebar.number_input("Vertical Turns (selected)", value=32)

if st.button("Calculate"):
    results = calculate_coil_parameters(
        Breq, gap_mm, I, cond_side_mm, cooling_dia_mm,
        correction_factor, added_turns, num_coils, hor_turns, ver_turns
    )

    st.subheader("Calculation Results")
    for key, value in results.items():
        st.write(f"**{key}**: {value:.4f}" if isinstance(value, float) else f"**{key}**: {value}")
