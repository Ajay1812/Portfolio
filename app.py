from PIL import Image
import streamlit as st
import requests
from streamlit_lottie import st_lottie


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title = 'Portfolio', page_icon = ':tada:', layout = 'wide' )

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# --- Use Local CSS --- #
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css('style/style.css')

# ----- LOAD ASSETS ---- #
lottie_coding = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_tfb3estd.json")
lottie_profile = load_lottieurl('https://assets1.lottiefiles.com/datafiles/i1uFIojbGt3KRN2/data.json')
img_WhatsApp_Chat = Image.open('./images/WhatsApp chat Analyzer.webp')
img_PowerBi_Sales = Image.open('./images/power-BI.webp')
img_titanic = Image.open('./images/Titanic Dataset Analysis.png')
img_posenet = Image.open('./images/Posenet.png')
img_chatGPT = Image.open('./images/openai-featured.jpg')
img_scrapy = Image.open('./images/scrapy.png')
img_CO2 = Image.open('./images/CO2 Emission and Climate Change.png')
movie_app = Image.open('./images/movie_app.png')
Youtube_app = Image.open('./images/Youtube_1.png')


#---- lOAD RESUME PDF---#
Resume_pdf = './assets/Ajay Kumar_Resume.pdf'



# ------ HEADER SECTION ----- #
with st.container():
    Hi, img_profile = st.columns((2,1))
    with Hi:
        st.subheader('Hi, I am Ajay :wave:')
        st.title('Data Analyst')
        st.write("I am a recent B.Tech graduate with a passion for data analysis. I have developed skills in statistical analysis, data visualization, and machine learning, and have experience using tools such as Python, SQL, and PowerBI. As a data analyst, I am highly skilled in data analysis and visualization, and am committed to continuing to learn and grow in my career.")

    with img_profile:
        st_lottie(lottie_profile, height= 300, key='profile')
        # with st.container():

with st.container():
    one, two, three, four = st.columns(4)
    with four:
        with open(Resume_pdf, 'rb') as pdf_file:
                    PDFbytes = pdf_file.read()
                    st.download_button(
                        label=" 📄 Download Resume",
                        data=PDFbytes,
                        file_name= Resume_pdf,
                        mime="application/octet-stream",
                    )
        st.write("📫 a.kumar01c@gmail.com")

# ------ WHAT I DO ------ # 
with st.container():
    st.write('---')
    left_column, right_column = st.columns(2)
    with left_column:
        st.header('What I do')
        st.write("I have been learning about machine learning and artificial intelligence, and I am actively seeking opportunities to further develop my skills in these areas. I have also completed several projects in these fields to apply my knowledge and gain practical experience.")
    with right_column:
            st_lottie(lottie_coding, height= 400, key='coding')

# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn, Pandas), SQL, Streamlit
- 📊 Data Visulization: PowerBi, MS Excel
- 📚 Development: HTML, CSS, JavaScript, React JS, Streamlit
- 🗄️ Databases: MySQL
"""
)




# ---- PROJECTS ---- #
with st.container():
    st.write('---')
    st.header('PROJECTS')
    st.write('##')
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_WhatsApp_Chat)
        st.image(img_PowerBi_Sales)
        st.image(img_titanic)
        st.image(img_posenet)
        st.image(img_CO2)


        with text_column:
            # WhatsApp Chat Analyzer
            st.subheader('WhatsApp Chat Analyzer')
            st.write('A WhatsApp chat analyzer is a tool that allows you to analyze the messages in a WhatsApp chat and extract various statistics and insights from the data. This can be useful for understanding how a group of people communicate with each other.')
            st.markdown("[Source Code 🔗](https://github.com/Ajay1812/WhatsApp_Chat_Analysis)")

            # Sales Analysis using PowerBi
            st.subheader('Sales Analysis using PowerBi')
            st.write('The purpose of the project was to better understand the customer base and identify trends in sales revenue. Sales data was collected from a company database covering a three-year period. Power BI was used to create visualizations, including bar charts, scatter plots, and maps, to analyze the data.')
            st.markdown("[Source Code 🔗](https://github.com/Ajay1812/Machine_Learning_Projects/tree/main/PowerBi%20Dashboard)")
            st.write('#')

            # Titanic Dataset Analysis
            st.subheader('Titanic Dataset Analysis')
            st.write('This repo presents my approach for the solution of the classical and most famous Titanic Dataset. This project marked the beginning of my Data science Journey and helped in Learning a lot.  EDA, Feature Generation and Modelling of Tabular Data                      ')
            st.markdown("[Source Code 🔗](https://github.com/Ajay1812/Machine_Learning_Projects/tree/main/Titanic%20Dataset%20Analysis)")
            st.write('#')
            
            # PoseNet - Posture Dection by Posenet
            st.subheader('Posture Dection by Posenet')
            st.write('Posenet can be used for posture detection by tracking the key points on a person body and estimating the pose based on the relative positions of these points. The model can detect a wide range of postures, including standing, sitting, walking, running, and more.')
            st.markdown("[Source Code 🔗](https://github.com/Ajay1812/Machine_Learning_Projects/tree/main/PoseNet)")

            
            st.write('#')
            # CO2 Emisson And Climate Change Dashboard
            st.subheader('CO2 Emisson And Climate Change Dashboard')
            st.write('The CO2 Emission and Climate Change Dashboard is a Python-based application that utilizes the power of Panel and HvPlot libraries to visualize and analyze data related to CO2 emissions and climate change. It provides a user-friendly interface that allows users to explore and understand the impact of CO2 emissions on the environment.')
            st.markdown("[Source Code 🔗](https://github.com/Ajay1812/Machine_Learning_Projects/tree/main/Co2%20Dashboard)")


st.write('#')

# ---- CONTACT ---- #
with st.container():
    st.write('---')
    st.header('Get In Touch With Me!')


#----- SOCIAL LINKS-----#
LinkedIn = 'https://www.linkedin.com/in/ajay-kumar-691a52208'
GitHub = 'https://github.com/Ajay1812'


# cols = st.columns(len(Social_media))
# for index, (platform, link) in enumerate(Social_media.items()):
#     cols[index].write(f'[{platform}]({link})')

with st.container():
    one, two, three, four = st.columns(4)
    with one:
        st.markdown('[LinkedIn](https://www.linkedin.com/in/ajay-kumar-691a52208)')
    with two:
        st.markdown('[GitHub](https://github.com/Ajay1812)')


    # Documention: 
    contact_form = """
    <form action="https://formsubmit.co/a.kumar01c@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
