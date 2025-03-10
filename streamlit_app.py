import streamlit as st

# Must be the first Streamlit command
st.set_page_config(page_title="Password Strength Meter", page_icon="🔒")

from app import PasswordStrengthMeter

# Add background color and hover effects
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(45deg, #FF1493 0%, #C71585 50%, #DB7093 100%);
    }
    
    /* Style for title */
    h1 {
        color: #1A1A1A !important;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
        font-weight: 700 !important;
        padding: 10px;
        background: rgba(255, 255, 255, 0.1);
        border-radius: 10px;
    }
    
    /* Style for tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 20px;
    }
    
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        padding: 10px 20px;
        background-color: rgba(255, 255, 255, 0.1);
        border-radius: 5px;
        color: white;
        transition: all 0.3s ease;
    }
    
    .stTabs [data-baseweb="tab"]:hover {
        background-color: rgba(75, 0, 130, 0.7);
        color: white;
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }
    
    .stTabs [aria-selected="true"] {
        background-color: rgba(75, 0, 130, 0.9) !important;
        color: white !important;
    }
</style>
""", unsafe_allow_html=True)

def main():
    st.markdown('<h1>Password Strength Meter 🔒</h1>', unsafe_allow_html=True)
    
    meter = PasswordStrengthMeter()
    
    tab1, tab2 = st.tabs(["Check Password", "Generate Password"])
    
    with tab1:
        password = st.text_input("Enter your password:", type="password")
        if password:
            score, feedback, strength = meter.check_password_strength(password)
            
            # Display strength with color
            color = {
                "Strong": "green",
                "Moderate": "orange",
                "Weak": "red",
                "Very Weak": "#8B0000"  # Dark red color
            }[strength]
            
            st.markdown(f"### Strength: <span style='color:{color}'>{strength}</span>", unsafe_allow_html=True)
            st.markdown(f"**Score:** {score:.1f}/4.0")
            
            st.markdown("### Feedback:")
            for msg in feedback:
                st.markdown(f"- {msg}")
    
    with tab2:
        length = st.slider("Password Length", min_value=8, max_value=32, value=12)
        if st.button("Generate Strong Password"):
            password = meter.generate_strong_password(length)
            st.code(password, language=None)
            st.info("Copy this password and keep it safe!")

if __name__ == "__main__":
    main() 