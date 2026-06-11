# An interactive format of our beloved OnePager


import streamlit as st
import pandas as pd

# hardcoded workaround for stlite
css = """/* Button 1 */
.st-key-color1 a {
    background-color: aquamarine;
    color: #191970;
    border-radius: 8px;
}/* Button 2 */
.st-key-color2 a {
    background-color: #E6E6FA;
    color: #191970;
    border-radius: 8px;;
}/* Button 3 */
.st-key-color3 a {
    background-color: #87CEFA;
    color: #191970;
    border-radius: 8px;
}/* Button 4 */
.st-key-color4 a {
    background-color: #E0FFFF;
    color: #191970;
    border-radius: 8px;
}/* Button 5 */
.st-key-color5 a {
    background-color: #FFF0F5;
    color: #191970;
    border-radius: 8px;
}/* Button 6 */
.st-key-color6 a {
    background-color: #F5FFFA;
    color: #191970;
    border-radius: 8px;
}/* Button 7 */
.st-key-color7 a {
    background-color: #FFE4E1;
    color: #191970;
    border-radius: 8px;
}/* Button 8 */
.st-key-color8 a {
    background-color: #FFE4E1;
    color: #191970;
    border-radius: 8px;
}
"""
st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

st.set_page_config(layout="wide")

with st.sidebar:
    st.write("*Contact Info*")
    st.image('images/accenture.aug.2017-072.jpg',width=200)
    st.write("Laura Astola")
    st.write("AI/ML Computational Science Associate Manager")
    st.write("📱 +31 622 098 982")
    st.write("📧 laura.astola@accenture.com")

tab1, tab2, tab3 = st.tabs(["Work Experience", "Education & Languages", "Certificates"],width="stretch")

with tab1:
    wdf= pd.read_excel('./data/work_experience.xlsx')
    st.dataframe(wdf, hide_index=True, column_config={'Start':st.column_config.TextColumn(width=25,
                                                                    help="Project starting month"),
                                                      'Finish':st.column_config.TextColumn(width=25,
                                                                   help="Projectst finishing month"),
                                                      'Client/Employer':st.column_config.TextColumn(width=110),
                                                      'Sector':st.column_config.TextColumn(width=85),
                                'Functional':st.column_config.TextColumn(help="Double-click a cell for wrapped text"),
                                'Technical': st.column_config.TextColumn(help="Double-click a cell for wrapped text")})

with tab2:
    st.image('images/Eindhoven_University_of_Technology_logo.png', width=150)
    st.write("PhD Applied Mathematics, 2010")
    st.link_button("Thesis in Google Scholar", 'https://scholar.google.com/citations?view_op=view_citation&hl=en&user=ZJZIls8AAAAJ&cstart=20&pagesize=80&citation_for_view=ZJZIls8AAAAJ:WF5omc3nYNoC')
    st.image('images/Helsinki_University_of_Technology_logo.png', width=150)
    st.write('Helsinki University of Technology')
    st.write('Licenciate\'s Degree in Mathematics, 2009')
    st.link_button("Thesis", 'https://alexandria.tue.nl/openaccess/Metis226803.pdf')
    st.write('Master\'s Degree in Mathematics, 2000')

with tab3:
    col1, col2, col3, col4,col5,col6,col7,col8, col9 = st.columns(9, gap="xsmall")
    with col1:
        st.link_button("GitHub Actions",'https://www.udacity.com/certificate/e/01dd1d86-79b2-11f0-b061-2b2f4f747398', key="color1")
        st.link_button("Machine Learning with PySpark: Data Analysis using SQL",
                       'https://www.coursera.org/account/accomplishments/verify/GL2Y2XL73XLR?utm_source=link&utm_medium=certificate&utm_content=cert_image&utm_campaign=sharing_cta&utm_product=project',
                       key="color4")
        st.link_button("Apache Spark (TM) SQL for Data Analysts",
                       'https://www.coursera.org/account/accomplishments/verify/D6NXQUMG5XZ9',
                       key="color7", width="stretch")
    with col2:
        st.link_button("FastAPI",'https://www.udacity.com/certificate/e/bab5e9a8-6eab-11f0-bb2a-5ffcb77ac1ac', key="color2")
        st.link_button("Deep Learning Speciali-zation", 'https://www.coursera.org/account/accomplishments/specialization/7SYBZGUEQCX9',
                       key="color5")
    with col3:
        st.link_button("Generative AI and Large Language Models", 'https://www.coursera.org/account/accomplishments/verify/EBZMCLUA6A2N?utm_source=link&utm_medium=certificate&utm_content=cert_image&utm_campaign=sharing_cta&utm_product=course',
                       key="color3", width="stretch")
        st.link_button("Developing AI Applications on Azure",
                       'https://www.coursera.org/account/accomplishments/verify/MXJBBXUXWSS5',
                       key="color6", width="stretch")


