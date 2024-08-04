import streamlit as st
from common import config_page, sidebar_menu


config_page('Others')
sidebar_menu()

st.title("Others📚")
st.subheader("- Teaching Experience")
st.markdown("""
- **Introduction to Python Programming (2021 - Present)**

    The "Introduction to Python Programming" course is offered twice every year 
    at Technische Universität Berlin Winter and Summer School. It is designed 
    for beginners and provides foundational knowledge in Python programming. 
    The course includes a series of live lectures, hands-on exercises with 
    tutorials, and project design activities. The course is tailored for a 
    diverse audience, including university students at the bachelor, master, 
    and PhD levels, as well as working professionals from various fields.
    For more details, you can visit the [course page](https://www.tu.berlin/en/international/summer-school/summer-school/summer-school-online/t2-introduction-to-python-programming).
""")
st.markdown("""
- **Web-Scraping for Beginners (2024)**

    The "Web-Scraping for Beginners Workshop" is a 2-day course provided to the 
    Data-Method-Monitoring Cluster at DeZIM Institute, aimed at quantitative 
    researchers with prior experience in survey data but little to no experience 
    in web scraping. 
""")

st.subheader("- Training Programs")
markdown_table = """
<table>
  <tr>
    <td style="font-style: italic; color: gray">2019</td>
    <td>Lab Course Machine Learning</td>
    <td>Technische Universität Berlin</td>
  </tr>
  <tr>
    <td></td>
    <td style="font-family: Verdana, sans-serif; font-size: 14px;">
      Python, Linux<br>
      • 9 ECTS, grade 1.0<br>
      • <a href="https://drive.google.com/drive/u/0/folders/1vGAO5KiugYWIoOG3o7_lSKohEB19pH1Z">
        course certificate and report sample</a>
    </td>
    <td></td>
  </tr>
  <tr>
    <td style="font-style: italic; color: gray">2020</td>
    <td>Project Machine Learning</td>
    <td>Technische Universität Berlin</td>
  </tr>
  <tr>
    <td></td>
    <td style="font-family: Verdana, sans-serif; font-size: 14px;">
      Python, Linux<br>
      • reproduction of ML projects: (U-Nets) semantic segmentation<br>
      • self-built dataset <a href="https://www.kaggle.com/datasets/cceekkigg/berlin-aoi-dataset/data">CitySegmentation</a>
    </td>
    <td></td>
  </tr>
  <tr>
    <td style="font-style: italic; color: gray">2022</td>
    <td>Simone Training</td>
    <td><a href="https://www.liwacom.com/index.php">LIWACOM</a></td>
  </tr>
  <tr>
    <td></td>
    <td style="font-family: Verdana, sans-serif; font-size: 14px;">
      Simone Software and API<br>
      • A leading pipeline simulation and optimization software<br>
      • participation certificate</a>
    </td>
    <td></td>
  </tr>
</table>
"""
st.markdown(markdown_table, unsafe_allow_html=True)
