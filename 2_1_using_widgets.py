import streamlit as st

st.header(":green[Using Widgets]")
def capture():
    st.subheader(":violet[click a selfie]")
    Image = st.camera_input("click to capture",label_visibility="hidden")
st.subheader("An example to click picture and show")
st.button("Show",on_click=capture)


# Examples of user input
st.header("Different user input types")

st.subheader("1. Taking numeric input")
userinput = st.number_input(":orange[Enter a] number")
st.caption(f"You have entered {userinput}")

userinput = st.slider("Enter value by sliding",
                      min_value=1,max_value=100,value=50)
st.caption(f"you have selected {userinput}")

if not st.checkbox("go to next item",key=1):
    st.stop()



st.subheader("2. Text")
userinput = st.text_input("Enter some text")
st.markdown(f"You have entered --> :orange[{userinput}] <--")
userinput = st.text_area("Enter a paragraph",height=50)

if not st.checkbox("go to next item",key=2):
    st.stop()

st.subheader("3. Enter your birthday")
userinput = st.date_input("some date",label_visibility='hidden')
st.markdown(f"""your birthday comes on  {userinput.strftime("%B %d")}""")



if not st.checkbox("go to next item",key=3):
    st.stop()



st.subheader("4. Checkbox and radio buttons")

# Checkbox
userinput = st.checkbox("Check or uncheck this")
st.caption(f"user input is '{userinput}'")
st.divider()

# single choice with all option visible
useroptions = ['Option 1','Option 2', 'Option 3']
userinput = st.radio("single choice selection",
                     options=useroptions,horizontal=True)
st.caption(f"You have selected -> {userinput} <-")
st.divider()


# single choice drop down box
userinput = st.selectbox("Select by sliding ",options=useroptions)
st.caption(f"You have selected -> {userinput} <-")
st.divider()
    

#  single choice with slider
userinput = st.select_slider("select by sliding",options=useroptions)
st.caption(f"You have selected -> {userinput} <-")
st.divider()

# multiple choice
userinput = st.multiselect("a;sldkfj",options=useroptions,
                           label_visibility="hidden")
st.caption(f"You have selected -> {userinput} <-")
st.divider()


# Quick Test
st.subheader(":red[Different ways to enter a phone number and display]")


# buttons
st.header(":green[Buttons]")
st.button('an button who does nothing')

def print_on_click():
    st.markdown(":red[you clicked a button]")
st.button('button that prints upon click',on_click=print_on_click)

