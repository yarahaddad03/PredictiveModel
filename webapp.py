import streamlit as st
from PIL import Image
from streamlit.components.v1 import html

# Load image
image = Image.open("OSB-ROTATOR-05.png")

# Page 1 - Company Overview
def page_company():
    st.markdown('<h1 style="color: #840132;">Company Overview</h1>', unsafe_allow_html=True)
    st.image(image, use_column_width=True)
    st.write('​​​​​​​​​​​​​​The ​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​American University of Beirut, established in 1866, enjoys a lengthy, distinguished history as one of the worlds foremost universities, a reputation enhanced by the Suliman S. Olayan School of Business. OSB is highly regarded within the international community with rankings consistently placing it as a MENA leader and provider of international caliber vision and opportunity. The school currently enrolls over 1,500 of the most select students in the region within its world-class BBA, MBA/MBA Online​, Executive MBA, and specialized masters degree programs in Human Resources Management, Finance, and Business Analytics. In addition to its extensive activity in providing executive education throughout the region to leading organizations, the school has long been AACSB International-accredited.')

# Page 2 - Tableau Dashboard
def page_dashboard():
    tableau_html = '''
    <div class='tableauPlaceholder' id='viz1683477824302' style='position: relative'><noscript><a href='#'><img alt='Students Attrition Dashboard ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;At&#47;AttritionTableau_16834775703220&#47;StudentsAttritionDashboard&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='AttritionTableau_16834775703220&#47;StudentsAttritionDashboard' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;At&#47;AttritionTableau_16834775703220&#47;StudentsAttritionDashboard&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1683477824302');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='1580px';vizElement.style.height='927px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='1580px';vizElement.style.height='927px';} else { vizElement.style.width='100%';vizElement.style.height='3427px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>
    '''
    # Display the embedded Tableau dashboard
    html(tableau_html, height=1580, width=900)


# Page 3 - Machine Learning Model
def page_ml():
    st.markdown('<h1 style="color: #840132;">Students Performance Predictive Model</h1>', unsafe_allow_html=True)
    st.header('Input students data below')


    #input form
    import pickle
    import numpy as np
    
    def load_model():
        with open('saved_steps.pkl', 'rb') as file:
            data=pickle.load(file)
        return data

    data = load_model()

    rf_loaded = data["model"]
    le_Gender = data["le_Gender"]
    le_Country = data["le_Country"]
    le_Scholarship = data["le_Scholarship"]
    le_Performance = data["le_Performance"]
    le_Governorates = data["le_Governorates"]
    le_Schools = data["le_Schools"]
    le_Diploma = data["le_Diploma"]


    Gender = (
        "M",
        "F"
    )

    Countries = (
        "Lebanon",
        "United Arab Emirates",
        "Saudi Arabia",
        "United States of America",
        "Jordan",
        "Kuwait",
        "Qatar",
        "Syria",
        "United Kingdom",
        "AUB (Development use only)",
        "Canada",
        "France",
        "Cote D'Ivoire",
        "Switzerland",
        "Bahrain",
        "Oman",
        "Tunisia",
        "Australia",
        "Netherlands",
        "Italy",
        "Egypt",
        "Malaysia",
        "Spain",
        "Singapore",
        "AUBMC (Development use only)",
        "Belgium",
        "Romania",
        "Ghana",
        "Germany",
        "Cyprus",
        "Tanzania",
        "Algeria",
        "Turkey",
        "Japan",
        "Greece",
        "Hungary",
        "Hong Kong",
        "Ireland",
        "Morocco",
        "Venezuela",
        "Yemen",
        "Burkina Faso",
    )

    Scholarship = (
        "Yes",
        "No",
    )

    Governorates = (
        "Akkar",
        "Baalbeck-Hermel",
        "Beirut",
        "Bekaa",
        "Mount Lebanon",
        "North Lebanon",
        "South Lebanon",
    )

    School = ('International College, Ras Beirut',
            'GrandLyceeFrancolibanais,bey',
            'Col.Prot.Francais, Beirut',
            'Rawdah H.Sch., Beirut',
            'College Notre Dame de Jamhour',
            'Lycee Abdul-Kader, Beirut',
            'College Louise Wegmann, Beirut',
            'American Comm. Sc /Beirut', 
            'Sagesse High School, Ain Saade', 
            'College Notre Dame de Nazareth', 
            'College MARISTE Champville ,Di', 
            'Hariri High School II, Beirut', 
            'Rafic Hariri High School,Sidon', 
            'St.Joseph Sch.Cornet Shahwan', 
            'GrandLyceeFrancolibanais,bey'
            )

    Diploma = ('Leb Bac II- Basic Life Sci',
            'Leb Bac II-Sociology & Economy',
            'Leb Bac II- General Sci',
            'French Bacc. -Econ.& Sociology',
            'French Bacc. - Mathematics',
            'International Baccalaureate - Science', 
            'Leb Bac II-Humanities & Philo', 
            'French Bacc.  - Literary', 
            'Lebanese Bacc.II Exp.Sci.'
            )

    Age = st.slider("Age at admission", 16, 50 , 18)
    Gender = st.selectbox("Gender", Gender)
    Country = st.selectbox("Country", Countries)
    Scholarship = st.selectbox("Scholarship", Scholarship)
    SAT = st.slider("SAT Score", 500, 1600, 1100)
    Governorates = st.selectbox("Governorates", Governorates)
    School = st.selectbox("School", School)
    Diploma = st.selectbox("Diploma", Diploma)

    predict = st.button("Predict Performance")
    if predict:
        X=np.array([[Age, Gender, Country, Scholarship, SAT, Governorates, School, Diploma]])
        X[:,1] = le_Gender.transform(X[:,1])
        X[:,2] = le_Country.transform(X[:,2])
        X[:,3] = le_Scholarship.transform(X[:,3])
        X[:,5] = le_Governorates.transform(X[:,5])
        X[:,6] = le_Schools.transform(X[:,6])
        X[:,7] = le_Diploma.transform(X[:,7])
        X=X.astype(float)
    
        performance = rf_loaded.predict(X)
        if performance[0] == 0:
            st.subheader("This student will fail")
        else:
            st.subheader("This student will pass")
    
        prediction_proba= rf_loaded.predict_proba(X)
    
        st.subheader('Prediction Probability')
        st.write(prediction_proba)

# App Navigation
def main():
    st.set_page_config(page_title='My Streamlit App', page_icon=':student:', layout='wide')
    st.sidebar.title('Homepage')
    pages = {'Company Overview': page_company, 'Tableau Dashboard': page_dashboard, 'Machine Learning Model': page_ml}
    page = st.sidebar.selectbox('Go to', options=list(pages.keys()))
    pages[page]()

if __name__ == '__main__':
    main()
