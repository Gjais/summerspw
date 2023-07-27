import streamlit as st
import pandas as pd
st.header("IIT BOMBAY COURSE REGISTRATION")
page_choice = st.radio("Select an option to fill form",
                       options=['IIT B',
                                'Indian Institute Bombay',
                                'भारतीय प्रौद्योगिकी संस्थान, मुम्बई '
                                ])

if page_choice == 'IIT B':
    st.header(":green[Course Registration]")
    
    
    st.sidebar.header(":violet[My Profile]")

    with st.sidebar:
        st.markdown("ज्ञानं परमं ध्येयम्")
        st.checkbox("This is my profile")
        name_from_sidebar = st.text_input("Enter name in sidebar")
        
    st.subheader(":violet[Enter your details]")
    col1,col2,col3 = st.columns(3)

    col1.header("Name")
    col2.header(":green[Roll no]")
    col3.header(":violet[Department]")
    # col4.header(":red[Courses]")
    cc=0

    myname = col1.text_input("Enter Name")
  
    if not myname:
        st.markdown("please fill your name")
    # for i in range(len(myname)):
        # if(myname[f"{i}"]=='0' or myname[f"{i}"]=='1' or myname[f"{i}"]=='2'or myname[f"{i}"]=='3' or myname[f"{i}"]=='4' or myname[f"{i}"]=='6' or myname[f"{i}"]=='7' or myname[f"{i}"]=='8' or myname[f"{i}"]=='9'):
            # cc=1  
    # if cc==1:
        # str.error(" you entered a number 😅")        
    # myname.capitalize()    
    
    roll=col2.text_input("IITB Roll Number")
    if not roll:
        st.markdown("Please fill the correct roll no")
    elif len(roll)!=8:
        st.error("please fill 8 digit no.")
    elif roll.__contains__(" "):
        st.error("You have a blank space")    
    
    # department=col3.text_input("Department") 
    if(roll[2:5]=='100'):
        a=col3.text_input("Enter your department",value="Computer Science",
                  disabled=True)
    elif(roll[2:5]=='101'):
         a=col3.text_input("Enter your department",value="Civil Engineering",
                  disabled=True)
    elif(roll[2:5]=='111'):
         a=col3.text_input("Enter your department",value="Chemical Engineering",
                  disabled=True)
    elif(roll[2:5]=='112'):
         a=col3.text_input("Enter your department",value="Mechanical Engineering",
                  disabled=True) 
    elif(roll[2:5]=='156'):
         a=col3.text_input("Enter your department",value="BS MATH",
                  disabled=True)              
    elif(roll[2:5]=='168'):
         a=col3.text_input("Enter your department",value="MEMS",
                  disabled=True)
  
    # b=col4.text_input(st.checkbox(" MA 109"))
    
    # x=col4.st.radio("choose your courses" ,options = ['MA 109', 'PH 117', 'CE 103', 'MS 101'])
    # selected_options = st.multiselect('Select options', courses)
    
    # st.write('Selected options:', selected_options)
    # options = ['Option 1', 'Option 2', 'Option 3', 'Option 4']

    # col1, col2 = st.beta_columns(2)

    # with col1:
    #     selected_options = st.multiselect('Select options', options)

    # with col2:
    #     st.write('Selected options:', selected_options)
    st.subheader(":violet[Courses]")
    
    options = ['MA109', 'CH 119', 'PH 117', 'CE 102','MS 101']
    selected_options = []
    # x=col4.text_input("select courses")
    for option in options:
        checkbox = st.checkbox(option)
        if checkbox:
            selected_options.append(option)

    if len(selected_options) == 0:
        st.error('Please select at least one option.')
    else:
        st.write('Selected options:', selected_options)
    
    xo="you successfully submitted"
    st.button("Submit",args=[xo])
#     def greetme(name):
#     st.text(name)
# st.button("Greet",on_click=greetme,args=[userintput])
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
elif page_choice == 'Indian Institute Bombay':
    
    st.header("Course Registration")
    t1,t2,t3,t4,t5 = st.tabs(['Name',
                           'IITB Roll no',
                           'check your department',
                           'Select your courses',
                           'feedback'
                           ])
    # Name
    with t1:
        username = st.text_input("Enter your name")
        if username.strip():
            st.markdown(f"Welcome :orange[{username}] to IIT BOMBAY")
    
    # Roll no
    with t2:
        # def naive(name):
        #     if name.strip():
        #         st.markdown(f"Hare Krishna :orange[{name}]")
        username = st.text_input("Enter your name",key=2)
        st.button("Method 1",on_click=naive,args=[username])
    
    # with 1 button
    with t3:
        def naive(name):
            if name.strip():
                st.session_state.msg = name
        username = st.text_input("Enter your name",key=3)
        st.button("Method 2",on_click=naive,args=[username])
        if 'msg' in st.session_state:
                st.markdown(f"Hare Krishna :orange[{st.session_state.msg}]")

    
    # With 2 buttons
    with t4:
        def naive(name):
            if name.strip():
                st.session_state.msg = name
        username = st.text_input("Enter your name",key=4)
        st.button("Method 3",on_click=naive,args=[username])
        if 'msg' in st.session_state:
                st.markdown(f"## Hare Krishna :orange[{st.session_state.msg}]")

        def erase():
            st.session_state.pop("msg")
        st.button("Erase",on_click=erase)
            
    # final
    with t5:
        def naive(name):
            if name.strip():
                st.session_state.msg = name
        username = st.text_input("Enter your name",key=5)
        st.button("Method 4",on_click=naive,args=[username])
        if 'msg' in st.session_state:
                st.markdown(f"## Hare Krishna :orange[{st.session_state.msg}]")
                st.session_state.pop('msg')
        

elif page_choice == 'भारतीय प्रौद्योगिकी संस्थान, मुम्बई':
    st.error("please implement this ")

    st.text_input("Enter your department",value="Mathematics",
                  disabled=True)
    
    st.write({
         '22B2434':["Akash Joshi",'22B2434','Meta',['MM225','MM777']],
         '22B243d':["Akash Joshi",'22B2434','Meta',['MM225','MM777']]
         })
  
    