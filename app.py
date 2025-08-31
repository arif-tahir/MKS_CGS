import gradio as gr

# Conversion dictionary (base: MKS)
conversions = {
    "Length (m ↔ cm)": {"to_cgs": 100, "to_mks": 1/100},
    "Mass (kg ↔ g)": {"to_cgs": 1000, "to_mks": 1/1000},
    "Force (N ↔ dyne)": {"to_cgs": 1e5, "to_mks": 1/1e5},
    "Energy (J ↔ erg)": {"to_cgs": 1e7, "to_mks": 1/1e7},
}

def convert_units(value, quantity, system):
    try:
        value = float(value)
    except:
        return "❌ Please enter a valid number"
    
    if quantity not in conversions:
        return "❌ Unknown quantity"
    
    factor = conversions[quantity]["to_cgs"] if system == "MKS → CGS" else conversions[quantity]["to_mks"]
    result = value * factor
    
    if quantity == "Length (m ↔ cm)":
        return f"{value} m = {result:.4f} cm" if system == "MKS → CGS" else f"{value} cm = {result:.4f} m"
    elif quantity == "Mass (kg ↔ g)":
        return f"{value} kg = {result:.4f} g" if system == "MKS → CGS" else f"{value} g = {result:.4f} kg"
    elif quantity == "Force (N ↔ dyne)":
        return f"{value} N = {result:.4e} dyne" if system == "MKS → CGS" else f"{value} dyne = {result:.4e} N"
    elif quantity == "Energy (J ↔ erg)":
        return f"{value} J = {result:.4e} erg" if system == "MKS → CGS" else f"{value} erg = {result:.4e} J"

# Gradio interface
demo = gr.Interface(
    fn=convert_units,
    inputs=[
        gr.Textbox(label="Enter Value"),
        gr.Dropdown(list(conversions.keys()), label="Select Quantity"),
        gr.Radio(["MKS → CGS", "CGS → MKS"], label="Conversion Type")
    ],
    outputs="text",
    title="🔄 MKS ↔ CGS Unit Converter",
    description="Convert Length, Mass, Force, and Energy between MKS and CGS systems"
)

if __name__ == "__main__":
    demo.launch()
