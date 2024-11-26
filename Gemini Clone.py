import streamlit as st
import google.generativeai as genai

# Gemini ka Code
keyVar="AIzaSyDhTd3CtspolCWgfme0b85ZJ95vDjokyuE"
genai.configure(api_key=keyVar)
model = genai.GenerativeModel("gemini-1.5-flash")

data= '''
Administration:- 
Principal: Reverend Father Vivian Fernandez
Vice Principal: Reverend Sister ta
Teachers:-
Shakun Saxena : Computer teacher
Arun Rajput : Maths teacher
Ravi Srivastav : Computer teacher
Akash : Physical education teacher
Manju Sharma : Computer for junior classes
Harpreet Kaur : Computer science teacher
Purnima Mani Tripathi : Biology teacher
Renu Arora : Maths teacher
Vaishali Tandon : Physics teacher
Nishi Popli : Chemistry teacher
Devendra : Physical education teacher
Rita Bernard : Hindi teacher
Helen Gabriel : English teacher
Ivan D'Souza : Social Science teacher
Viji Alex : English teacher
Ranjeet Kaur : Hindi teacher
Poonam Rastogi : Hindi teacher
Rupanjali Kamboj : Science teacher
Ashwini Catherine : Dance teacher
Gulafsha : Social Science teacher
Amit Kumar : Maths teacher
Hemlata Gangwar : Hindi teacher
Meenakshi Rawat : Maths teacher
Shivani Soni : Maths teacher
Nidhi Verma : English teacher
Vandana Chauhan : English teacher
Richa Rawat : Biology teacher
Bharti Singh : Social Science teacher
Sutapa Bhattacharya :Business Studies Teacher
Sonal Agarwal :Business Studies Teacher
Deepti Arora :Social Science Teacher
Jyoti Verma :Social Science Teacher
Arti Verma :Social Science Teacher
Priyanka Chaturvedi :Science Teacher



Information about school or Principal's Word:
Maria Assumpta Convent Sr. Secondary School is a minority Institution (Constitution of India Act, 30). It is a recoganized but un aided English Medium School, established and administered by Roman Catholic Diocese of Bareilly, a charitable Society (Registered Society) It was registered in Bareilly on 13.4.1989 under the Societies registration Act XXI of 1860.

This Institution is situated in the out skirts of Kashipur. It's imposing building is equipped with electric lights and fans, with it’s hall, well stocked library, Science laboratories, Reading Room, spacious room and large play ground.

Maria Assumpta Convent Sr. Sec. School, Kashipur is a Co-Educational English medium Institution run by the Catholic Minority. It is affiliated to the Central Board of Secondary Education, New Delhi.
Our aim is to help students to realize their potential. Instead of wasting time worrying about what they don't have or what they can't do, spend time in working at things they can do.
Our educational philosophy is centered on praise, encouragement, enthusiasm, and affection, rather than criticism, fear, and punishment. We constantly work to develop a sense of discipline and good moral character, where all students are expected to confirm to high disciplinary standards and to develop values of tolerance, fair play, compassion, integrity and fortitude.
We are trying to provide our students with an atmosphere of multifaceted development, where children are encouraged to channelize their potential in the pursuit of excellence. This can only be possible in a holistic and student-centric environment. The talents, skills, and abilities of each student need to be identified, nurtured, and encouraged so that he/she is able to reach greater heights. We are providing our Students a platform to think, express, and exhibit their skills. It is necessary to empower them to negotiate several issues that confront them, with the teacher being a facilitator.
'''
# Streamlit Code
st.title("MACS Clone")
st.write("MACS Clone stimulates real life conversation and answers to your prompts in a real life conversative manner. Our bot uses a combination of artificial intelligence (AI) and natural language processing (NLP) techniques to understand and respond to user queries. ")
st.write("All rights reserved to @AS.Developer")
st.divider()
# Result Function
def replyFunc(userPrompt:str):   
    response = model.generate_content(f"Reply to the prompt of '{userPrompt}' in accordance from {data}. ")
    return response.text

st.chat_message("assistant").markdown("Hello, what is in your mind?")
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("assistant"):
        response= replyFunc(prompt)
        st.markdown(response)
        
    st.session_state.messages.append({"role": "assistant", "content": response})        
