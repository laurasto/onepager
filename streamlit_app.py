# An GitHub "compatible" mini cv

import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

with st.sidebar:
    st.write("*Contact Info*")
    st.image("https://raw.githubusercontent.com/laurasto/onepager/master/images/accenture.aug.2017-072.jpg", width=200)
    st.write("Laura Astola")
    st.write("AI/ML Computational Science Associate Manager")
    st.write("📱 +31 622 098 982")
    st.write("📧 laura.astola@accenture.com")

tab1, tab2, tab3 = st.tabs(["Work Experience", "Education & Languages", "Certificates"],width="stretch")

with tab1:
    # stlite cannot read external data, so data is hardcoded here until I create a typescript version
    wdf = pd.DataFrame(columns=['Start', 'Finish', 'Client/Employer', 'Sector', 'Functional', 'Technical'])
    start = ['2025-09-01','2024-09-01','2019-01-01','2018-06-15','2017-10-15','2017-08-17','2014-01-01','2011-01-01','2010-02-01','2006-02-01']
    finish = ['2026-05-13','2025-09-20','2025-8-30','2018-10-15','2018-05-15','2017-10-15','2016-12-30','2013-12-30','2010-12-30','2010-01-23']
    wdf['Start'] = pd.to_datetime(start).strftime('%b-%Y')
    wdf['Finish'] = pd.to_datetime(finish).strftime('%b-%Y')
    wdf['Client/Employer'] = ['DSM-Firmenich/Accenture','Fokker/Accenture','Rabobank/Accenture','DHL/Accenture','AXA/Accenture',\
                              'Vodafone/Accenture','TU Eindhoven','Wageningen University',\
                              'ASML/TU Eindhoven','TU Eindhoven']
    wdf['Sector'] = ['Bio Tech','Aviation','Financial','Transport','Insurance','Telecom','Higher Education',
                     'Higher Education','Semiconductor','Higher Education']
    wdf['Functional'] = ['Build prototype central application where lab personnel can easily query\n internal information from database, clean and organize historical data to database',
            'Deliver an interactive view on all contracts, users, their status and location etc. as python Plotly dashboard',
            'Data Quality monitoring, building dashboards and reports for proactive measures, building scripts to retrieve, and validate external data sources for data quality improvements',
            'Build and validate ML models, using various customer data to predict parcel weights and dimensions',
            'Build application to extract, validate and display information from images of handwritten forms, using ML and Computer Vision',
            'Train deep neural networks to recognize modem status from images',
            'Design and lecture bachelor courses on medical image analysis and processing',
            'Research on mathematical modeling of metabolic and genetic networks of tomatoes for cost efficient trait improvement',
            'Research on alternative geometric modeling of diffraction gratings',
            'PhD project on geometric modeling of diffusion tensor images to capture axonal connectivities in brain']
    wdf['Technical'] = ['Databricks, Python, Streamlit, GitHub  Actions, Bitbucket, AzureML, Spotfire, Jira',
                        'Python, AzureDevOps, Plotly, Infinity, SQL',
                        'Informatica, Python, Power BI, Databricks, AzureDevOps, Git, SQL, OracleDB, IBM DB, DBVisualiser, SQLDeveloper, Mainframe',
                        'Python, Sk-Learn, XGBoost, SQL',
                        'Python,  Open CV, Azure cognitive services, Fuzzy matching, Javascript',
                        'Python, Keras,  Open CV, Javascript',
                        'Python, Matlab, Mathematica',
                        'R, Matlab, Mathematica',
                        'Matlab, Mathematica',
                        'Matlab, Mathematica']

    st.dataframe(wdf, hide_index=True, column_config={'Start':st.column_config.TextColumn(width=25,
                                                                    help="Project starting month"),
                                                      'Finish':st.column_config.TextColumn(width=25,
                                                                   help="Projectst finishing month"),
                                                      'Client/Employer':st.column_config.TextColumn(width=110),
                                                      'Sector':st.column_config.TextColumn(width=85),
                                'Functional':st.column_config.TextColumn(help="Double-click a cell for wrapped text"),
                                'Technical': st.column_config.TextColumn(help="Double-click a cell for wrapped text")})

with tab2:
    st.image("https://raw.githubusercontent.com/laurasto/onepager/master/images/Eindhoven_University_of_Technology_logo.png", width=150)
    st.write("PhD Applied Mathematics, 2010")
    st.link_button("Thesis in Google Scholar", 'https://scholar.google.com/citations?view_op=view_citation&hl=en&user=ZJZIls8AAAAJ&cstart=20&pagesize=80&citation_for_view=ZJZIls8AAAAJ:WF5omc3nYNoC')
    st.image("https://raw.githubusercontent.com/laurasto/onepager/master/images/Helsinki_University_of_Technology_logo.png", width=150)
    st.write('Helsinki University of Technology')
    st.write('Licenciate\'s Degree in Mathematics, 2009')
    st.link_button("Thesis", 'https://alexandria.tue.nl/openaccess/Metis226803.pdf')
    st.image("https://raw.githubusercontent.com/laurasto/onepager/master/images/Helsinki_University_logo.jpg", width=150)
    st.write('Master\'s Degree in Mathematics, 2000')

with tab3:
    col1, col2, col3, col4,col5,col6,col7,col8, col9 = st.columns(9, gap="small")
    with col1:
        # Inject CSS for styling since stlite does not allow reading from folder
        st.markdown("""<style>.custom-link-button {
            background-color: aquamarine; 
            color: #191970 !important;
            border-radius: 8px;}</style>
        """, unsafe_allow_html=True)
        st.markdown('<a href="https://www.udacity.com/certificate/e/01dd1d86-79b2-11f0-b061-2b2f4f747398" target="_blank" '
            'class="custom-link-button">GitHub Actions</a>',
            unsafe_allow_html=True)
        st.markdown("""<style>.custom-link-button {
            background-color: #FFF0F5; 
            color: #191970 !important;
            border-radius: 8px;}</style>
        """, unsafe_allow_html=True)
        st.markdown('<a href="https://www.udacity.com/certificate/e/bab5e9a8-6eab-11f0-bb2a-5ffcb77ac1ac" target="_blank" '
            'class="custom-link-button">Fast API</a>',
            unsafe_allow_html=True)
        st.markdown("""<style>.custom-link-button {
                    background-color: #F0FFF0; 
                    color: #191970 !important;
                    border-radius: 8px;}</style>
                """, unsafe_allow_html=True)
        st.markdown(
            '<a href="https://www.coursera.org/account/accomplishments/verify/MXJBBXUXWSS5" target="_blank" '
            'class="custom-link-button">Developing AI Applications on Azure</a>',
            unsafe_allow_html=True)

    with col2:
        st.markdown("""<style>.custom-link-button {
            background-color: #FFE4E1; 
            color: #191970 !important;
            border-radius: 8px;}</style>
        """, unsafe_allow_html=True)
        st.markdown('<a href="https://www.coursera.org/account/accomplishments/verify/D6NXQUMG5XZ9" target="_blank" '
            'class="custom-link-button">Apache Spark (TM) SQL for Data Analysts</a>',
            unsafe_allow_html=True)
        st.markdown("""<style>.custom-link-button {
                    background-color: #F5FFFA; 
                    color: #191970 !important;
                    border-radius: 8px;}</style>
                """, unsafe_allow_html=True)
        st.markdown('<a href="https://www.coursera.org/account/accomplishments/specialization/7SYBZGUEQCX9" target="_blank" '
                    'class="custom-link-button">Deep Learning Specialization</a>',
                    unsafe_allow_html=True)

    with col3:
        st.markdown("""<style>.custom-link-button {
            background-color: #E0FFFF; 
            color: #191970 !important;
            border-radius: 8px;}</style>
        """, unsafe_allow_html=True)
        st.markdown('<a href="https://www.coursera.org/account/accomplishments/verify/GL2Y2XL73XLR?utm_source=link&utm_medium=certificate&utm_content=cert_image&utm_campaign=sharing_cta&utm_product=project" target="_blank" '
            'class="custom-link-button">Machine Learning with PySpark: Data Analysis using SQL</a>',
            unsafe_allow_html=True)
        st.markdown("""<style>.custom-link-button {
                    background-color: #F0FFFF; 
                    color: #191970 !important;
                    border-radius: 8px;}</style>
                """, unsafe_allow_html=True)
        st.markdown(
            '<a href="https://www.coursera.org/account/accomplishments/verify/EBZMCLUA6A2N?utm_source=link&utm_medium=certificate&utm_content=cert_image&utm_campaign=sharing_cta&utm_product=course" target="_blank" '
            'class="custom-link-button">Generative AI and Large Language Models</a>',
            unsafe_allow_html=True)






