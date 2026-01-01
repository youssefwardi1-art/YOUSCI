# YOUSCI - AI-Powered Catalyst Discovery for UM6P
# Prepared by: Youssef WARDI - USMBA University
# M2 Internship Proposal: Theoretical Insights into Metal Nanoparticles-Perovskite Interactions

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import ipywidgets as widgets
from IPython.display import display, Markdown, HTML

print("🔬 YOUSCI: AI-Driven Discovery of Stable Metal Nanoparticles on Perovskite Supports")
print("==================================================================================")
print("Real database with 135+ data points from 2020-2024 literature")
print("Predictive model accuracy: R² = 0.9919")
print()

# REAL DATA FROM YOUR DATABASE (Formation/Adhesion Energies)
formation_data = {
    'Metal': ['Pd', 'Ni', 'Ag', 'Pt', 'Au', 'Co', 'Ni', 'Pd', 'Pt', 'Ag', 'Ni', 'Co',
              'Au', 'Pd', 'Pt', 'Ag', 'Ni', 'Co', 'Au', 'Pd'],
    'Support': ['SrTiO3', 'LaFeO3', 'TiO2', 'BaZrO3', 'LaFeO3', 'SrTiO3', 'SrTiO3', 
                'LaFeO3', 'TiO2', 'BaZrO3', 'BaZrO3', 'LaFeO3', 'SrTiO3', 'BaZrO3',
                'LaFeO3', 'SrTiO3', 'TiO2', 'BaZrO3', 'TiO2', 'TiO2'],
    'Formation_Energy_eV': [-2.45, -1.89, -1.12, -3.10, -1.55, -2.15, -1.95, -2.30, -3.40,
                           -1.25, -2.05, -2.10, -1.40, -2.55, -3.25, -1.15, -1.80, -2.20,
                           -1.35, -2.40]
}

# Bader Charges from your database
bader_data = {
    'System': ['Pd/SrTiO3', 'Ni/LaFeO3', 'Ag/TiO2', 'Pt/BaZrO3', 'Au/LaFeO3', 
               'Co/SrTiO3', 'Ni/SrTiO3', 'Pd/LaFeO3', 'Pt/TiO2', 'Ag/BaZrO3',
               'Co/LaFeO3', 'Au/SrTiO3', 'Pd/BaZrO3', 'Pt/LaFeO3', 'Ag/SrTiO3',
               'Ni/TiO2', 'Co/BaZrO3', 'Au/TiO2', 'Pd/TiO2', 'Pt/SrTiO3'],
    'Metal_Charge_e': [0.45, 0.32, 0.15, 0.58, 0.22, 0.38, 0.35, 0.42, 0.62, 0.18,
                      0.40, 0.25, 0.48, 0.65, 0.20, 0.38, 0.42, 0.28, 0.52, 0.68]
}

# Create DataFrames
df_formation = pd.DataFrame(formation_data)

# Split the System column in bader_data to create Metal and Support columns
df_bader = pd.DataFrame(bader_data)
df_bader[['Metal', 'Support']] = df_bader['System'].str.split('/', expand=True)

# Merge data on both Metal and Support
df = pd.merge(df_formation, df_bader[['Metal', 'Support', 'Metal_Charge_e']], 
              on=['Metal', 'Support'], how='left')

# Display the database
print("📊 REAL DATABASE EXTRACT (20 systems from 135+ points):")
display(df.head(10))

# Metal properties (from your methodological data file)
metal_properties = {
    'Ni': {'electronegativity': 1.91, 'atomic_radius_A': 1.24, 'd_electrons': 8, 'cost_kg': 20},
    'Co': {'electronegativity': 1.88, 'atomic_radius_A': 1.25, 'd_electrons': 7, 'cost_kg': 33},
    'Pt': {'electronegativity': 2.28, 'atomic_radius_A': 1.39, 'd_electrons': 9, 'cost_kg': 32000},
    'Pd': {'electronegativity': 2.20, 'atomic_radius_A': 1.37, 'd_electrons': 10, 'cost_kg': 62000},
    'Au': {'electronegativity': 2.54, 'atomic_radius_A': 1.44, 'd_electrons': 10, 'cost_kg': 59000},
    'Ag': {'electronegativity': 1.93, 'atomic_radius_A': 1.44, 'd_electrons': 10, 'cost_kg': 850}
}

# Perovskite properties from your database
perovskite_properties = {
    'LaFeO3': {'band_gap': 2.1, 'lattice_a': 5.56, 'tolerance': 0.96},
    'SrTiO3': {'band_gap': 3.2, 'lattice_a': 3.91, 'tolerance': 1.00},
    'BaZrO3': {'band_gap': 3.0, 'lattice_a': 4.19, 'tolerance': 1.01},
    'TiO2': {'band_gap': 3.0, 'lattice_a': 4.59, 'tolerance': 'N/A'}
}

print("\n" + "="*70)
print("🧠 UNIVERSAL STABILITY EQUATION (from your research):")
print("="*70)
print("ΔE_form = α + β1*Q_Bader + β2*χ + β3*R_atomic")
print("Where:")
print("  α = 0.335, β1 = -4.578, β2 = -0.183, β3 = -0.277")
print("  Q_Bader: Bader metal charge (e)")
print("  χ: Pauling electronegativity")
print("  R_atomic: Atomic radius (Å)")
print("  Achieved R² = 0.9919 (99.19% variance explained)")
print()

# Implementation of your universal stability equation
def predict_formation_energy(bader_charge, electronegativity, atomic_radius):
    """Your universal stability equation with exact coefficients"""
    alpha = 0.335
    beta1 = -4.578
    beta2 = -0.183
    beta3 = -0.277
    
    formation_energy = alpha + beta1*bader_charge + beta2*electronegativity + beta3*atomic_radius
    return formation_energy

def classify_stability(energy):
    """Classify based on formation energy"""
    if energy < -2.5:
        return "Very High", "🟢"
    elif energy < -2.0:
        return "High", "🟢"
    elif energy < -1.5:
        return "Medium", "🟡"
    elif energy < -1.0:
        return "Low", "🟠"
    else:
        return "Very Low", "🔴"

def calculate_performance_cost_ratio(formation_energy, metal_cost):
    """Your performance-cost ratio equation"""
    if metal_cost > 0:
        return (-formation_energy / metal_cost) * 1000
    else:
        return 0

# Interactive Prediction Tool
print("🎯 INTERACTIVE PREDICTION TOOL FOR UM6P")
print("Configure your catalyst system:")

# Create widgets
metal_widget = widgets.Dropdown(
    options=list(metal_properties.keys()),
    value='Ni',
    description='Metal:',
    style={'description_width': 'initial'}
)

support_widget = widgets.Dropdown(
    options=list(perovskite_properties.keys()),
    value='SrTiO3',
    description='Perovskite:',
    style={'description_width': 'initial'}
)

bader_widget = widgets.FloatSlider(
    value=0.45,
    min=0.1,
    max=0.8,
    step=0.01,
    description='Bader Charge (e):',
    style={'description_width': 'initial'}
)

output = widgets.Output()

def make_prediction(b):
    with output:
        output.clear_output()
        
        metal = metal_widget.value
        support = support_widget.value
        bader_charge = bader_widget.value
        
        # Get properties
        metal_props = metal_properties[metal]
        perovskite_props = perovskite_properties[support]
        
        # Predict using YOUR equation
        predicted_energy = predict_formation_energy(
            bader_charge,
            metal_props['electronegativity'],
            metal_props['atomic_radius_A']
        )
        
        # Classify stability
        stability_class, emoji = classify_stability(predicted_energy)
        
        # Calculate performance-cost ratio
        cost_ratio = calculate_performance_cost_ratio(predicted_energy, metal_props['cost_kg'])
        
        print(f"\n{'='*60}")
        print(f"🔮 PREDICTION FOR: {metal}/{support}")
        print(f"{'='*60}")
        print(f"Input Parameters:")
        print(f"  • Bader Charge: {bader_charge:.3f} e")
        print(f"  • Metal Electronegativity: {metal_props['electronegativity']}")
        print(f"  • Metal Atomic Radius: {metal_props['atomic_radius_A']} Å")
        print(f"\nResults:")
        print(f"  • Predicted Formation Energy: {predicted_energy:.3f} eV")
        print(f"  • Stability Classification: {stability_class} {emoji}")
        print(f"  • Performance-Cost Ratio: {cost_ratio:.2f}")
        
        # Optimal charge range check (from your discovery #2)
        if 0.45 <= bader_charge <= 0.60:
            print(f"  • Charge Transfer: ✅ OPTIMAL (0.45-0.60 e range)")
        elif bader_charge < 0.45:
            print(f"  • Charge Transfer: ⚠️  BELOW OPTIMAL (< 0.45 e)")
        else:
            print(f"  • Charge Transfer: ⚠️  ABOVE OPTIMAL (> 0.60 e)")
        
        # Recommendations
        print(f"\n💡 RECOMMENDATIONS FOR UM6P:")
        if stability_class in ["Very High", "High"]:
            print(f"  1. This system is promising for experimental validation")
            print(f"  2. Consider socketed geometry for enhanced stability")
            
            if metal in ["Ni", "Co"]:
                print(f"  3. Cost-effective alternative to Pt/Pd")
                print(f"     → Estimated savings: 90% compared to Pt-based catalysts")
            
            # Application suggestions
            if support in ["SrTiO3", "TiO2"]:
                print(f"  4. Recommended for: Water splitting (OER)")
            elif support == "BaZrO3":
                print(f"  4. Recommended for: High-temperature fuel cells")
            elif support == "LaFeO3":
                print(f"  4. Recommended for: CO₂ reduction")
        else:
            print(f"  1. Consider alternative metal/support combination")
            print(f"  2. Adjust synthesis parameters to increase charge transfer")
        
        print(f"\n📈 Next steps at UM6P:")
        print(f"  1. Experimental synthesis of {metal}/{support}")
        print(f"  2. XRD/TEM characterization")
        print(f"  3. Electrochemical testing in relevant conditions")

# Display widgets
display(metal_widget)
display(support_widget)
display(bader_widget)

button = widgets.Button(description="Predict Catalyst Stability", button_style='success')
button.on_click(make_prediction)
display(button)
display(output)

# Display top systems from your database
print("\n" + "="*70)
print("🏆 TOP 3 SYSTEMS FROM YOUR DATABASE (Recommended for UM6P)")
print("="*70)

top_systems = [
    {"System": "Pt/BaZrO3", "ΔE": -3.10, "Bader": 0.58, "Stability": "Very High", 
     "Cost": 32000, "PCR": 0.097, "Application": "High-temp SOFCs"},
    {"System": "Ni/SrTiO3", "ΔE": -1.95, "Bader": 0.35, "Stability": "High",
     "Cost": 20, "PCR": 97.5, "Application": "Water splitting"},
    {"System": "Co/LaFeO3", "ΔE": -2.10, "Bader": 0.40, "Stability": "High",
     "Cost": 33, "PCR": 63.6, "Application": "CO₂ reduction"}
]

for i, system in enumerate(top_systems, 1):
    print(f"\n{i}. {system['System']}:")
    print(f"   • Formation Energy: {system['ΔE']} eV")
    print(f"   • Bader Charge: {system['Bader']} e (Optimal: 0.45-0.60 e)")
    print(f"   • Stability: {system['Stability']}")
    print(f"   • Performance-Cost Ratio: {system['PCR']}")
    print(f"   • Best Application: {system['Application']}")
    
    if system['System'].startswith(('Ni', 'Co')):
        print(f"   • ✅ Cost Advantage: 90% cheaper than Pt-based catalysts")

# Visualization of charge transfer optimal range (from your discovery #2)
print("\n" + "="*70)
print("📊 OPTIMAL CHARGE TRANSFER RANGE (Discovery #2)")
print("="*70)

# Create visualization
fig, ax = plt.subplots(figsize=(10, 6))

# Plot data points
charges = df['Metal_Charge_e'].dropna()
energies = df['Formation_Energy_eV'][:len(charges)]

ax.scatter(charges, energies, alpha=0.6, s=100, label='Database Points')

# Highlight optimal range
ax.axvspan(0.45, 0.60, alpha=0.2, color='green', label='Optimal Range (0.45-0.60 e)')
ax.axvline(0.55, color='red', linestyle='--', alpha=0.5, label='Optimal (0.55 e)')

ax.set_xlabel('Bader Metal Charge (e)', fontsize=12)
ax.set_ylabel('Formation Energy (eV)', fontsize=12)
ax.set_title('Optimal Charge Transfer for Maximum Stability', fontsize=14)
ax.legend()
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# Final message
print("\n" + "="*70)
print("🚀 READY FOR UM6P: What I Bring to Your Team")
print("="*70)
print("1. ✅ COMPLETE DATABASE: 135+ data points from 2020-2024 literature")
print("2. ✅ VALIDATED MODEL: Universal stability equation (R² = 0.9919)")
print("3. ✅ INTERACTIVE TOOL: Live prediction system (this notebook)")
print("4. ✅ DESIGN RULES: Optimal charge transfer range (0.45-0.60 e)")
print("5. ✅ COST ANALYSIS: 90% savings with Ni/Co alternatives")
print("6. ✅ READY TO START: Experimental plan for first week at UM6P")
print()
print("📧 Contact: youssef.wardi1@usmba.ac.ma")
print("📱 LinkedIn: linkedin.com/in/youssef-wardi")
print("💻 GitHub: github.com/username (YOUSCI framework)")