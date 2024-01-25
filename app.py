from dotenv import load_dotenv
from streamlit_modal import Modal
from PIL import Image
import streamlit as st
import os
import google.generativeai as genai
import random
st.set_page_config(page_title="Celebrity.AI",page_icon="👦🏽",layout='centered',menu_items={'Get Help': 'https://www.extremelycoolapp.com/help',
'Report a bug': "https://www.extremelycoolapp.com/bug",
'About': "# This is a header. This is an *extremely* cool app!"})
# loading enviroinmental variables
load_dotenv()
api_lst=[]
msg_query=[]

api_lst.append(os.environ.get('GOOGLE_API_KEY_1'))

genai.configure(api_key=str(api_lst[0]))

modal = Modal(key="Demo Key",title=["test"])

# loading model
model=genai.GenerativeModel('gemini-pro')

# chat variables store all chat history

chat = model.start_chat(history=[])

def main_page():
    
    st.caption("🛠️use dark theme for better user experience 😎")

    title_text = '<p style="font-family:Impact; color:rgb(255, 161, 39);; font-size: 50px;">CELEBRITY AI</p>'
    st.markdown(title_text, unsafe_allow_html=True)
    st.write("-"*50)
    
    
    st.header(" 🚀Chat with Fomous personalities 🙎🏼 Anytime ⏲️, Anywhere!!! 📌")
    st.write("\n")
    st.write("\n")
    st.image("black-img-trans-resized.png")
    # 
    st.write("\n")
    st.write("\n")
    st.write("\n")
    
    user_input = st.text_input(' *Enter Celebrity name 🧔🏽‍♂️👩🏽:')
    # original_title = '<p style="font-family:Impact; color:rgb(255, 161, 39);; font-size: 50px;">Original image</p>'
    # st.markdown(original_title, unsafe_allow_html=True)
    
    st.write("\n")
    st.write("\n")
    col1,col2=st.columns([6,6])
    with col1:
        
        # 🛠️✨🎯📌🚀🔥🙎🏼🙎🏼🧔🏽‍♂️👩🏽🔥
        con_type=st.selectbox(
            " *how you want your conversation to be ?",
            ['Friendly 😊','Casual 😎','Formal 🙂','Inspirational 🥺',"Serious 😨","Funny 🤣",'Informative 🧐','Professional 🤓','Sarcastic 😆','Respectful 🫡','Motivational 🤯']
        )
    
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    with col2:
        
        con_length=st.selectbox(
            " *choose preffered chat length",
            ['Crisp (5 - 50 words)','Short (50 - 100 words)','Medium (100 - 200 words)','Long (200 - 350 words)']
        )
    
    
    st.write("\n")
   
    next=st.button('Next')
    st.caption("Click next to continue..")
    st.write("-"*50)
    st.subheader("Help us improve📝")
    st.write("Share your Valuable feedback: https://shorturl.at/itEM2")
    st.write("-"*50)
    st.subheader("Contact Me!! 📱")
    # st.subheader("Made by Vasan R ❤️")
    
    st.write("Email Me! 📧 contact.vasanml@gmail.com")
    st.write("My github 🐈‍⬛ https://github.com/vasan-rj")
    st.write("My LinkedIn 🔗 https://www.linkedin.com/in/vasan-r/")
    st.caption("Made by Vasan R ❤️")
    if next :
        if con_length and con_type and user_input:  
            # Save user input to session state
            st.session_state.user_input = user_input
            st.session_state.con_type=con_type
            st.session_state.con_length=con_length
            
            # Navigate to the "side" page
            st.experimental_set_query_params(page='side')
        else:            
            with modal.container():
                st.markdown('" :red[ENTER THE CELEBRITY NAME..... ]"')
               
            
            
def side_page():
    # st.write(st.session_state['user_input'])
    st.caption("🛠️use dark theme for better user experience 😎")
    title_text = '<p style="font-family:Impact; color:rgb(255, 161, 39);; font-size: 50px;">CELEBRITY AI</p>'
    st.markdown(title_text, unsafe_allow_html=True)
    st.subheader('🔥Talk to famous personality like Shah Rukh Khan Ghandhi ji Hitler ,Andrew Tate RDJ Etc....✨')
    
    st.write("-"*20)
    # Retrieve user data from session state
    if 'user_input' and 'con_type' and 'con_length' in st.session_state:
        user_input = st.session_state.user_input
        con_type=st.session_state.con_type
        con_length=st.session_state.con_length
        
    else:
        st.write("⚠️⚠️⚠️ERROR: Go back to Main Page and type celebrity name and try again....⚠️⚠️⚠️")
        
        
    def respone_from_gemini(query):
        try:
            res_ponse_x=model.generate_content(query)
            res_ponse_x=res_ponse_x.text
            
        except:
            res_ponse_x="Soory error occured try again please ..."
            
        return res_ponse_x
     
    x=""
    # st.image("black-img-trans.png")
    initial_prompt= f''' 
    user : hey you are a celebrity chatbot which gives reply like {user_input} ,
    Your role is to respond authentically, reflecting the unique mannerisms, vocabulary, and style of {user_input}
    And i want you to give response to the asked question in the {con_type} manner, and your response should be {con_length}, 
    make sure that you give correct and human readable answers ,Embrace their personas and interact naturally, providing users with an
    immersive experience akin to chatting with their idols, make sure you add emojis to your response.
    
    ai : hey i am {user_input} bot !!  
    
    '''
    x+=initial_prompt
    # st.write(x)
# d={}
    if 'chat-history' not in st.session_state:
        st.session_state['chat-history'] =[]
        
    with st.chat_message("ai"):
        st.markdown(f"hey i'm {user_input} bot!!")    
        
    # st.write(x)
    for role,res in st.session_state['chat-history']:
        with st.chat_message(role):
            st.markdown(res)
     
    if input := st.chat_input("Talk to celebrity!!"):
        with st.chat_message("user"):
            st.markdown(input)
    
        st.session_state['chat-history'].append(("user",input)) 
      
        for user,text in st.session_state['chat-history']:
            x+=(f"{user} : {text}")
            x+="\n"*2
            
        response=respone_from_gemini(x)
        
        
        st.subheader("Your response is")
        with st.chat_message("ai"):
            st.markdown(response)
        st.session_state['chat-history'].append(("ai",response)) 
        
    reset=st.button('Reset The bot')
    if reset:
        x=" "
        st.session_state['chat-history'] =[]
    st.caption("📝⚠️ if you want to talk to another personality click 'reset the bot' button and go back to the main page and type the new celebeirty name !! ⚠️")
    
    st.write(" "*10)
    st.write("-"*50)
    st.subheader("Help us improve📝")
    st.write("Share your Valuable feedback: https://shorturl.at/itEM2")
    st.write("-"*50)
    st.caption("Made by Vasan R ❤️")

   
# /////////////////////////////////

def main():
    # st.set_page_config(page_title="Celebrity-bot",page_icon="👦🏽",layout='wide')
    
    page = st.experimental_get_query_params().get("page", ["main"])[0]
    # page = st.query_params().get("page", ["main"])[0]

    
    if page == "main":
        main_page()
    elif page == "side":
        side_page()

if __name__ == "__main__":
    main()



