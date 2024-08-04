import base64
import streamlit as st
from common import sidebar_menu, config_page

config_page('Publication')
sidebar_menu()

st.title("Publication📝")


def load_image(path):
    with open(path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()


image_paths = [f"source/psig ({i}).png" for i in range(1, 12)]

scrollable_container = """
<style>
.scrollable-container {
    max-height: 600px;  /* Adjust the max height as needed */
    overflow-y: auto;
}
.scrollable-container img {
    display: block;
    margin: 10px auto;  /* Center images and add some margin */
    max-width: 100%;  /* Ensure the images fit within the container */
}
</style>
<div class="scrollable-container">
"""

for image_path in image_paths:
    image_base64 = load_image(image_path)
    scrollable_container += f'<img src="data:image/png;base64,{image_base64}">'
scrollable_container += "</div>"

col1, col2 = st.columns([1, 1])
with col1:
    st.subheader("Sample Scientific Paper")
    st.markdown(f"[Jiang, D., Hotopp, S., Wacker, M., & Muller-Kirchenbauer, J. (2020, May). Load Flow Calculations of "
                f"Large Transmission Gas Networks based on Public Data. In PSIG Annual Meeting (pp. PSIG-2005). PSIG.]"
                f"(https://onepetro.org/PSIGAM/proceedings-abstract/PSIG20/All-PSIG20/447849)", unsafe_allow_html=True)
    st.markdown(scrollable_container, unsafe_allow_html=True)
with col2:
    st.subheader("Cooperative Works and Ongoing Study")

    papers = [
        {"title": f"""Müller‐Kirchenbauer, J., Evers, M., Hollnagel, J., Kuzyaka, B., Jiang, D., Akça, O., 
                ... & Verwiebe, P. A. (2024). Germany's Way from Russian Natural Gas to Green Hydrogen: Network Data, 
                Procedures, and Topologies for Feasible Transition Paths to a Green Hydrogen Transport Infrastructure 
                in Germany, GreenHyDE [gri: n'haɪ̯də]–. Energy Technology, 2300976.""",
         "link": "https://www.researchgate.net/publication/380790496_Germany's_Way_from_Russian_Natural_Gas_to_Green_Hydrogen_Network_Data_Procedures_and_Topologies_for_Feasible_Transition_Paths_to_a_Green_Hydrogen_Transport_Infrastructure_in_Germany_GreenHyDE_grin'haI"},
        {"title": f"""Ragwitz, M., Müller-Kirchenbauer, J., Klaaßen, B., Graf, M., Herrmann, U., Nolden, C., 
                Evers, M., Akça, O., Jiang, D., Hurtig, K. (2022): Europäische Gasversorgungssicherheit aus 
                technischer und wirtschaftlicher Perspektive vor dem Hintergrund unterbrochener Versorgung aus 
                Russland, Studie im Auftrag des Akademienprojektes Energiesysteme der Zukunft“ (ESYS), 
                Förderkennzeichen 03EDZ2016, Fraunhofer IEG & SCAI, TU Berlin, Berlin.""",
         "link": "https://www.er.tu-berlin.de/fileadmin/a38331300/Report_Acatech_Fraunhofer_TU_Berlin.pdf"},
    ]
    for paper in papers:
        st.markdown(f'- [{paper["title"]}]({paper["link"]})')
    st.markdown("---")
    st.markdown("""
                #### Ongoing Research:

                **Simulation-Based Assessment of Hydrogen Storage Requirements for the Transition 
                from Natural Gas to Hydrogen in Germany** 
                _Dongrui Jiang, Jeremias Hollnagel, Nesma Aboshanab, Berkan Kuzyaka, Bekir Okan Akca, 
                Joachim Müller-Kirchenbauer_

                (draft version completed)
                """, unsafe_allow_html=True)

