import streamlit as st

# -----------------------------------
# Page Configuration
# -----------------------------------
st.set_page_config(
    page_title="Simple Calculator",
    page_icon="🧮",
    layout="centered"
)

st.title("🧮 Simple Calculator")
st.write("Enter a mathematical expression below.")

# -----------------------------------
# User Input
# -----------------------------------

expression = st.text_input(
    "Enter Expression",
    placeholder="Example: 2+2"
)

# -----------------------------------
# Calculate
# -----------------------------------

if st.button("Calculate"):

    if expression.strip() == "":
        st.warning("Please enter an expression.")

    else:
        try:
            result = eval(expression)
            st.success(f"Result: {result}")

        except ZeroDivisionError:
            st.error("Error: Division by zero is not allowed.")

        except Exception:
            st.error("Invalid mathematical expression.")