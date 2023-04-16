import streamlit as st
import streamlit.components.v1 as components
from PIL import Image

st.set_page_config(layout="wide",initial_sidebar_state="expanded")
col1,col2 = st.columns((2))
st.sidebar.title('Sophie')
st.sidebar.text("Hi There! My Name is Sophie.")
st.sidebar.text(" I am your Virtual Retail Assistant ,\n designed to assist you with any \n questions or concerns you may have.")
st.sidebar.text(" Whether you're looking for \n information about our products \n or services, or need help with \n an issue you're experiencing, \n I'm here to provide quick and \n efficient support. ")
st.sidebar.text("Please feel free to ask me anything \n and I'll do my best to assist you.\n Type In 'Hello' followed by your \n Question and I will solve it \n for you right away!")




with col1:

    st.subheader('Not sure how to start? \n Use the scenarios below to interact with Sophie')

    st.title('Scenarios')
    st.subheader('Faulty Return')
    st.markdown('You recently purchased a summer item from our store and after trying it on at home, you realized that the seam is coming off. Unfortunately, you have already removed the tag and thrown away the receipt. Now you have found a similar item that you would like to exchange, but you are unsure if this is possible. Reach out to Sophie to gain more information about this.')
    st.subheader('Recycling')
    st.markdown("You may be interested in our recycling incentive program, which allows customers to bring in their old clothes,eletrical etc for recycling.If you're interested in finding out more about the program, or how to participate, just ask Sophie and she'll be happy to assist you.")
    st.subheader('Primark Careers')
    st.markdown("Are you looking for a job that fits your skills and experience? Perhaps you've heard that Primark is hiring and you'd like to apply, but you're not sure where to start. No problem, just ask Sophie! She's here to help you with everything you need to know, from the latest job openings and application deadlines to the skills and qualifications that we're looking for. With Sophie's guidance, you can boost your chances of getting your dream job at Primark. So, what are you waiting for? Let's get started!")
with col2:
    components.html(
    """
            <iframe width="400" height="700" allow="microphone;" src="https://console.dialogflow.com/api-client/demo/embedded/d94eb81d-1d83-4539-a638-92b3d6f09af1"></iframe>
""",
                 height=720,
                 width=450

)