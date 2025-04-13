import streamlit as st
from PIL import Image
import requests
from io import BytesIO

# Set page configuration
st.set_page_config(
    page_title="Sahir Ali",
    page_icon="👨‍💻",
    layout="wide"
)

# Load profile picture from URL
def load_image(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    return img

profile_pic = load_image("https://drive.google.com/file/d/1FVLn2RbagKS7u7x_Zw42k5n8eGq9s08P/view?usp=sharing")

# Custom CSS for dark theme
st.markdown(
    """
    <style>
    /* Main app background */
    .stApp {
        background: linear-gradient(45deg, #1e3c72, #2a5298);
        color: white !important;
    }

    /* Sidebar background */
    .css-1d391kg {
        background: linear-gradient(45deg, #1e3c72, #2a5298) !important;
    }

    /* Sidebar text color */
    .css-1d391kg h1, .css-1d391kg h2, .css-1d391kg h3, .css-1d391kg h4, .css-1d391kg h5, .css-1d391kg h6, .css-1d391kg p, .css-1d391kg label {
        color: white !important;
    }

    /* Main content text color */
    .stMarkdown, .stMarkdown p, .stMarkdown h1, .stMarkdown h2, .stMarkdown h3, .stMarkdown h4, .stMarkdown h5, .stMarkdown h6 {
        color: white !important;
    }

    /* Button styling */
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 5px;
        padding: 10px 20px;
        font-size: 16px;
    }

    /* Input field styling */
    .stTextInput>div>div>input {
        background-color: transparent;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "About Me", "Projects", "Contact"])

# Home Page
if page == "Home":
    st.title("Welcome to My Portfolio!")
    
    # Create two columns for image and text
    col1, col2 = st.columns([1, 2])  # Adjust the ratio as needed
    
    with col1:
        # Display the profile picture with a larger size
        st.image(profile_pic, width=300, caption="Sahir Ali")  # Adjust the width as needed
    
    with col2:
        # Display the text on the right side of the image
        st.write("""
        Hi, I’m **Sahir Ali**! I’m studying Electrical and Electronics Engineering and learning about things like semiconductors and how to make eco-friendly designs. 
        I love working on ideas that can help improve technology and make it useful for everyone. I’ve also taken courses in E-commerce and IT to build my skills. 
        I’m excited to keep learning and growing in this field.
        """)

    # Additional paragraphs
    st.write("""
    ### My Journey in Engineering
    From a young age, I’ve been fascinated by how things work. This curiosity led me to pursue a degree in **Electrical and Electronics Engineering**, where I’ve been able to dive deep into subjects like semiconductor technology, renewable energy systems, and embedded systems. My goal is to contribute to the development of sustainable and efficient technologies that can make a positive impact on the world.
    """)

    st.write("""
    ### Passion for Innovation
    I’m particularly passionate about **AI, Metaverse, and Web 3.0**. These technologies are reshaping the future, and I’m excited to be part of this transformation. Through my studies and projects, I’ve gained hands-on experience in building decentralized applications, working with blockchain technology, and exploring virtual and augmented reality. I believe these technologies have the potential to solve real-world problems and create new opportunities for everyone.
    """)

    st.write("""
    ### Continuous Learning
    Learning is a lifelong journey for me. I’ve completed courses in **E-commerce** and **Information Technology (CIT)**, which have given me a strong foundation in digital business operations, programming, and troubleshooting. I’m always eager to expand my knowledge and take on new challenges. Whether it’s through online courses, hands-on projects, or collaborating with others, I’m committed to growing both personally and professionally.
    """)

# About Me Page
elif page == "About Me":
    st.title("About Me")
    st.write("""
    ### Bio
    Hi, I’m **Sahir Ali**! I’m studying Electrical and Electronics Engineering and learning about things like semiconductors and how to make eco-friendly designs. 
    I love working on ideas that can help improve technology and make it useful for everyone. I’ve also taken courses in E-commerce and IT to build my skills. 
    I’m excited to keep learning and growing in this field.
    """)
    
    st.write("### Skills")
    st.write("""
    #### AI, Metaverse, and Web 3.0
    - **Artificial Intelligence**: Proficient in machine learning algorithms, neural networks, and AI model development.
    - **Blockchain Technology**: Experience in building decentralized applications (DApps) and smart contracts.
    - **Virtual and Augmented Reality**: Skilled in creating immersive VR/AR experiences using tools like Unity and Unreal Engine.
    - **Web 3.0**: Knowledge of decentralized web technologies and protocols.
    """)

    st.write("""
    #### E-Commerce
    - **Digital Marketing**: Expertise in SEO, social media marketing, and online advertising.
    - **E-Commerce Platforms**: Hands-on experience with platforms like Shopify, WooCommerce, and Magento.
    - **Online Business Operations**: Proficient in managing online stores, inventory, and customer relationships.
    """)

    st.write("""
    #### Information Technology (CIT)
    - **Programming**: Proficient in Python, JavaScript, and C++.
    - **Troubleshooting**: Skilled in diagnosing and resolving hardware and software issues.
    - **Computer Applications**: Experience with Microsoft Office Suite, database management, and network administration.
    """)

    st.write("""
    #### English Language
    - **Communication**: Strong written and verbal communication skills.
    - **Proficiency**: Completed an Anglophone course to enhance English language skills.
    """)

# Projects Page
elif page == "Projects":
    st.title("My Projects")
    st.write("Here are some of the projects I’ve worked on:")

    # Streamlit Projects
    st.write("### Streamlit Projects")
    st.write("""
    #### 1. Password Strength Meter
    **Description**:  
    The Password Strength Meter is a tool designed to evaluate the strength of user passwords. It checks for factors such as length, complexity, and the presence of special characters.  
    **Technologies Used**: Python, Streamlit.  
    **Key Features**:  
    - Real-time password strength feedback.  
    - Visual indicators for weak, medium, and strong passwords.  
    """)

    st.write("""
    #### 2. Personal Library Manager
    **Description**:  
    The Personal Library Manager is a web application that helps users organize their book collections. Users can add, delete, and search for books in their library.  
    **Technologies Used**: Python, Streamlit, SQLite.  
    **Key Features**:  
    - Add and remove books from the library.  
    - Search functionality to find books quickly.  
    - Simple and intuitive user interface.  
    """)

    st.write("""
    #### 3. Unit Converter
    **Description**:  
    The Unit Converter is a versatile tool that allows users to convert between different units of measurement, such as length, weight, and temperature.  
    **Technologies Used**: Python, Streamlit.  
    **Key Features**:  
    - Supports multiple unit categories.  
    - Easy-to-use dropdown menus for unit selection.  
    - Instant conversion results.  
    """)

    st.write("""
    #### 4. Growth Mindset Document Web
    **Description**:  
    This web app provides resources and documents related to the growth mindset, helping users develop a positive attitude toward learning and self-improvement.  
    **Technologies Used**: Python, Streamlit.  
    **Key Features**:  
    - Access to curated growth mindset resources.  
    - User-friendly interface for easy navigation.  
    - Regularly updated content.  
    """)

    # Robotics Projects
    st.write("### Robotics Projects")
    st.write("""
    #### 1. LFR (Line Following Robot)
    **Description**:  
    The Line Following Robot is designed to autonomously follow a predefined path using sensors. It demonstrates the principles of robotics and automation.  
    **Technologies Used**: Arduino, IR sensors, Motors.  
    **Key Features**:  
    - Accurate line detection and tracking.  
    - Adjustable speed and sensitivity.  
    - Compact and efficient design.  
    """)

    st.write("""
    #### 2. Soccer Robot
    **Description**:  
    The Soccer Robot is a remote-controlled robot designed to play soccer. It showcases skills in robotics, control systems, and teamwork.  
    **Technologies Used**: Arduino, Bluetooth module, Motors.  
    **Key Features**:  
    - Remote control via Bluetooth.  
    - Precision movement and ball handling.  
    - Durable and lightweight design.  
    """)

    st.write("""
    #### 3. Lightweight War Bot
    **Description**:  
    The Lightweight War Bot is a combat robot designed for competitions. It features a robust design and powerful motors for agility and strength.  
    **Technologies Used**: Arduino, Motors, Weapon mechanisms.  
    **Key Features**:  
    - High-speed movement and maneuverability.  
    - Effective weapon systems for combat.  
    - Lightweight yet durable construction.  
    """)

    # Electronics Projects
    st.write("### Electronics Projects")
    st.write("""
    #### Variable Power Supply
    **Description**:  
    The Variable Power Supply is a versatile tool that provides adjustable voltage and current outputs. It was one of my early projects in electronics engineering.  
    **Technologies Used**: Basic electronic components (resistors, capacitors, transformers).  
    **Key Features**:  
    - Adjustable voltage and current.  
    - Stable and reliable output.  
    - Compact and portable design.  
    """)

# Contact Page
elif page == "Contact":
    st.title("Contact Me")
    st.write("""
    I’m always excited to connect with like-minded individuals, collaborate on innovative projects, or discuss new opportunities. 
    Whether you have a question about my work, want to share ideas, or simply want to say hello, feel free to reach out! 
    You can contact me via email at **sahirali9205@gmail.com** or connect with me on [LinkedIn](https://www.linkedin.com/in/sahir-ali-65380a33a/). 
    I’m open to discussions about technology, engineering, AI, and more. Looking forward to hearing from you!
    """)
    
    # Contact Details
    st.write("### Contact Details")
    st.write("📞 **Phone**: +92 3213574864")
    st.write("📧 **Email**: sahirali9205@gmail.com")
    st.write("🔗 **LinkedIn**: [Sahir Ali](https://www.linkedin.com/in/sahir-ali-65380a33a/)")
