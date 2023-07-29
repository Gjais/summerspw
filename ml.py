import streamlit as st

# Function to display the "My Profile" page
def show_my_profile():
    st.title("My Profile")
    st.write("Please fill in your details below:")

    # Use st.form to create a form for the user to fill in their details
    with st.form(key='profile_form'):
        name = st.text_input("Name:")
        email = st.text_input("Email:")
        address = st.text_area("Address:")
        submit_button = st.form_submit_button(label='Submit')

        # Process the form data after submission
        if submit_button:
            # Do something with the user's details, e.g., store in a database
            # For now, we'll just display a success message
            st.success("Profile details submitted successfully!")

# Main function
def main():
    # Create a sidebar with some options
    st.sidebar.title("Sidebar")
    menu_selection = st.sidebar.radio("Menu:", ["Home", "My Profile"])

    if menu_selection == "Home":
        st.title("Welcome to My Website")
        st.write("This is the home page.")
    elif menu_selection == "My Profile":
        # Show the "My Profile" page when the user clicks on "My Profile" in the sidebar
        show_my_profile()

if __name__ == "__main__":
    main()
