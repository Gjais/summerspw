import streamlit as st
import pandas as pd

st.header(":green[Using Markdown]")

with st.echo():
    st.markdown("# Hearing1")
    st.markdown("## Hearing2")
    st.markdown("### Hearing3")
    st.markdown("#### Hearing4")
    st.markdown("##### Hearing5")

st.divider()
st.markdown("## :red[text with red font] :violet[violet color]")

with st.echo():
    st.markdown("[visible text](web.whatsapp.com)")




# Displaying dataframe
st.header(":green[Data frames]")
df = pd.DataFrame(
                   [
                        ['Sanjeet Kumar','MAT','Hare Krishna'],
                        ['Akash J','META','Hari Bol'],
                        ['Vikram','Civil','Gaur Hari'],
                        ['Dheeraj','Civil','Gaur Premanande'],
                        ['Vishnu','Civil','Nitai Gaur'],
                        ['Gaurav','Civil','Hari Hari Bol']
                    ],
                   columns=['Name','Branch','greeting']
                   )


st.dataframe(df)

# left,right = st.columns(2)
# left.markdown("#### :orange[Editable view]")
# left.markdown("")
# left.markdown("")
# left.markdown("")
# right.markdown("#### :orange[Returned data]")

# edited_data = left.data_editor(df)
# if right.checkbox("Show returned data"):
#     right.dataframe(edited_data)


# Media elements
st.header(":green[Media Elements]")
# Image
# st.image("https://books.bvks.com/uploads/cache/thumbnail_ZikM9R-yUVw1_1000x.jpg")

# Video
url = st.text_input("Enter the URL of youtube")
if url:
    try :
        st.video(url)
    except :
        st.error("invalid file")

# Audio
url = st.text_input("Enter the URL of audio file")
if url:
    try :
        st.audio(url)
    except :
        st.error("invalid file")

