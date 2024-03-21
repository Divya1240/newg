import streamlit as st

def main():
    st.title("Patient Registration Platform")

    # Sidebar with user registration
    with st.sidebar:
        st.header("User Registration")
        username = st.text_input("Username")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        confirm_password = st.text_input("Confirm Password", type="password")
        if st.button("Register"):
            if password == confirm_password:
                # Process registration logic here (e.g., save to database)
                st.success("Registration successful!")
            else:
                st.error("Passwords do not match!")

    # Main content for patient registration
    st.subheader("Patient Registration")
    patient_name = st.text_input("Patient Name")
    patient_age = st.number_input("Patient Age", min_value=0, max_value=150, value=0)
    patient_gender = st.radio("Gender", options=["Male", "Female", "Other"])
    patient_notes = st.text_area("Additional Notes")

    # Submit button
    if st.button("Register Patient"):
        # Process patient registration logic here (e.g., save to database)
        st.success("Patient registered successfully!")

    # Gamification section
    st.header("Gamification")
    st.markdown("### Points: 100")
    st.markdown("### Badges: 🏅🎉")

    # Leaderboard
    st.header("Leaderboard")
    st.write("""
    | Rank | Username | Points |
    |------|----------|--------|
    | 1    | John     | 500    |
    | 2    | Emily    | 450    |
    | 3    | David    | 400    |
    """)

if __name__ == "__main__":
    main()
