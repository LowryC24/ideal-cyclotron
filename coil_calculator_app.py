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
    ver_turns=32,  # Vertical turns (manual selection)
    power_per_coil=100,  # Dissipated power per coil in Watts
    num_large_units=1,  # Number of large cooling units
    num_small_units=1,  # Number of small cooling units
    delta_T=20,  # Allowed temperature change in °C
    h2o_pressure=2.0  # Available H2O pressure in bar
):
    # Constants
    mu0 = 1e-6  # H/m (simplified)
    specific_heat = 4.186  # J/g°C for water

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

    # Cooling Calculations
    power_large = power_per_coil / num_large_units
    power_small = power_per_coil / num_small_units

    Q_large = power_large / (specific_heat * delta_T)  # grams/sec
    Q_small = power_small / (specific_heat * delta_T)  # grams/sec

    # Convert flow to liters per minute (approx.)
    Q_large_lpm = Q_large / 1000 * 60
    Q_small_lpm = Q_small / 1000 * 60

    # Estimate pressure drop (placeholder, not calculated here)
    dp_large = h2o_pressure * 0.6  # e.g., 60% pressure drop assumption
    dp_small = h2o_pressure * 0.4  # 40% drop for smaller unit

    return {
        "Vacuum Permeability (mu0) [H/m]": mu0,
        "Conductor Area [mm^2]": cond_area,
        "Current Density [A/mm^2]": current_density,
        "Ideal Number of Turns": turns_required,
        "Total Turns Used": total_turns,
        "Turns per Coil": turns_per_coil,
        "Horizontal Turns (selected)": hor_turns,
        "Vertical Turns (selected)": ver_turns,
        "Power per Large Cooling Unit [W]": power_large,
        "Power per Small Cooling Unit [W]": power_small,
        "Flow in Large Unit [L/min]": Q_large_lpm,
        "Flow in Small Unit [L/min]": Q_small_lpm,
        "Pressure Drop in Large Unit [bar]": dp_large,
        "Pressure Drop in Small Unit [bar]": dp_small
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
power_per_coil = st.sidebar.number_input("Dissipated Power per Coil (W)", value=100)
num_large_units = st.sidebar.number_input("Number of Large Cooling Units", value=1)
num_small_units = st.sidebar.number_input("Number of Small Cooling Units", value=1)
delta_T = st.sidebar.number_input("Allowed Temperature Rise ΔT (°C)", value=20)
h2o_pressure = st.sidebar.number_input("Available Water Pressure (bar)", value=2.0)

if st.button("Calculate"):
    results = calculate_coil_parameters(
        Breq, gap_mm, I, cond_side_mm, cooling_dia_mm,
        correction_factor, added_turns, num_coils,
        hor_turns, ver_turns,
        power_per_coil, num_large_units, num_small_units,
        delta_T, h2o_pressure
    )

    st.subheader("Calculation Results")
    for key, value in results.items():
        st.write(f"**{key}**: {value:.4f}" if isinstance(value, float) else f"**{key}**: {value}")
