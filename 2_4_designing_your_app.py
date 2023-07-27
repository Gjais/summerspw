import streamlit as st

page_choice = st.radio("Select an option",
                       options=['design brief',
                                'using tabs',
                                'using sidebar'
                                ])

if page_choice == 'design brief':
    
    
    st.header(":green[Overview of streamlit page design]")

    
    # Sidebars
    st.sidebar.header("This is sidebar")

    with st.sidebar:
        st.markdown("Everythign is same")
        st.checkbox(" a checkbox in sidebar")
        name_from_sidebar = st.text_input("Enter name in sidebar")


    


    # Multiple columns
    st.subheader(":green[Multiple columns]")
    col1,col2,col3 = st.columns(3)

    col1.header("Column 1")
    col2.header(":green[Column 2]")
    col3.header(":violet[Column 3]")

    myname = col1.text_input("Enter Name")
    if myname.strip():
        col2.markdown(f" Hare Krishna {myname}")
        col3.caption(f"Your name have {len(myname)} characters")
    
    # variables from sidebar are accessible here also
    col3.markdown(name_from_sidebar)



    # Tabs
    st.divider()
    st.subheader(":green[Tabs]")
    col1,col2,col3 = st.tabs(["Tab 1","Tab 2","Tab 3"])

    col1.number_input("Enter your age")
    col2.write("Works similar as column")


    # Expander 
    st.header(":green[Expandable area]")
    with st.expander("Expandable area",expanded=False):
        st.header("This is expandable area")
        st.text("which can close to acquire less space")

elif page_choice == 'using tabs':
    
    st.header("An example of designing geeting using tabs")
    t1,t2,t3,t4,t5 = st.tabs(['what we want',
                           'Naive way to do',
                           'with 1 button',
                           'with 2 buttons',
                           'final'
                           ])
    # what we wan
    with t1:
        username = st.text_input("Enter your name")
        if username.strip():
            st.markdown(f"Hare Krishna :orange[{username}]")
    
    # Naive way to do
    with t2:
        def naive(name):
            if name.strip():
                st.markdown(f"Hare Krishna :orange[{name}]")
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
        

elif page_choice == 'using sidebar':
    st.error("please implement this ")

    st.text_input("Enter your department",value="Mathematics",
                  disabled=True)
    
    st.write({
         '22B2434':["Akash Joshi",'22B2434','Meta',['MM225','MM777']],
         '22B243d':["Akash Joshi",'22B2434','Meta',['MM225','MM777']]
         })
