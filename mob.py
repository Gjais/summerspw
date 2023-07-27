import streamlit as st
st.header("provide your ph no")
# uinput=st.text_input(label='Enter your mob number')
# st.subheader("2. Text")
userinput = st.text_input("Enter number")
userinput=list(userinput)
status=True
if(len(userinput)!=10):
    status=False

# st.write(userinput)
for i in range(6):
     if(userinput[0]==f"{i}"):
         status=False
if status==True:
        st.markdown(f"You have entered --> :orange[{userinput}] <--")
else:
        st.markdown(f"You have entered --> wrong number <--")           