from pyscript import display, document
placeholder = {
    "H": ("Hydrogen",1, 1.000),
    "O": ("Oxygen", 8, 15.999),
    "Cl": ("Chlorine", 17, 35.45),
    "Ne": ("Neon", 10, 20.180),
    "Xe": ("Xenon", 54, 131.29),
 # The code recognizes the symbol you type and shows the results in the parentheses, from 0, 1, and 2.
}
def element_checker(e):
    document.getElementById('result').innerHTML = " "
    element1 = document.getElementById('element_name').value.strip().title()
    result = placeholder.get(
        element1, ("Element not found", "-", "-")
 # If theres a symbol typed that isn't found in the dictionary, it gives this result ^
    )
    document.getElementById('result').innerHTML = f"""
    <b>Symbol:</b> {element1}<br>
    <b>Element:</b> {result[0]}<br>
    <b>Atomic Number:</b> {result[1]}<br>
    <b>Atomic Mass:</b> {result[2]}<br>
    """
    # This ^ shows the results of the non-element you type in