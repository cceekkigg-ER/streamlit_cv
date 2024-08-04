import streamlit as st
from common import sidebar_menu, config_page

config_page('Project')
sidebar_menu()

st.title("Projects📁")
st.markdown("""
    This page lists the main projects I've contributed to since 2019. All these projects focus on discovering and 
    validating natural gas or hydrogen networks for Germany and the EU to meet various future gas supply and demand 
    targets. Explore the details below to learn more about each project.
""")

tab1, tab2, tab3 = st.tabs(["Langfristszenarien", "TransHyDE", "GHVR"])
with tab1:
    st.header("Langfristszenarien")
    st.markdown("""
        The [Langfristszenarien(LFS)](https://langfristszenarien.de/enertile-explorer-de/index.php) project, 
        commissioned by the German Federal Ministry for Economic Affairs and Climate  Action, covers the entire energy 
        system of Germany. This includes the generation of electricity, heat, and  hydrogen, as well as energy demand 
        in the industry, transport, building, and appliances sectors. The goal is to achieve the country's energy and 
        climate policy objectives.

        The focus of the analysis is not on developing a single "lead scenario" but on investigating different scenario 
        worlds to understand the advantages and disadvantages of various paths for transforming the energy system 
        through comparative analyses.

        My team and I concentrate on the [gas grid](https://langfristszenarien.de/enertile-explorer-en/scenario-explorer/gas-networks.php#anchor_03aa7654_Gas-grids) 
        within the energy system. Using our enhanced models, we are exploring how Germany can achieve greenhouse gas 
        neutrality by 2045, aligning with current political goals.
    """)
    col_x1, col_y1 = st.columns([1, 1])
    with col_x1:
        st.image("source/lfs_1.png", width=625)
    with col_y1:
        st.image("source/lfs_2.png", width=650)
with tab2:
    st.header("TransHyDE")
    st.markdown("""
        The [TransHyDe](https://www.wasserstoff-leitprojekte.de/leitprojekte/transhyde) project is funded by the 
        Bundesministerium für Bildung und Forschung (BMBF) and investigates suitable options for transport 
        infrastructure in a European hydrogen economy. The goal of the project is to identify and evaluate possible 
        topologies and transport pathways for hydrogen using model-based infrastructure analysis. The findings of all 
        TransHyDE projects will lead to recommendations for the national hydrogen infrastructure. To this end, 
        overarching regulatory framework conditions, standards, and certification options will be analyzed, and 
        gaps identified.
    """)
    st.image("source/transhyde.png", width=800)
with tab3:
    st.header("Gas Supply Security - GHVR")
    st.markdown("""
        **Gasversorgungssicherheit vor dem Hintergrund unterbrochener Versorgung aus Russland** project is funded by 
        [National Academy of Science and Engineering of Germany (Acatech)](https://en.acatech.de/) to analyze the
        security of Europe's gas supply from a network engineering perspective. It conducts a performance balance 
        examination of gas flows for the years 2022 to 2026 and 2030, assuming a complete interruption of gas supplies 
        from Russia. The resulting gas transports are validated through detailed flow modeling for the year 2026 across 
        five major European transport networks.
        More details: Ragwitz, M., Müller-Kirchenbauer, J., Klaaßen, B., Graf, M., Herrmann, U., Nolden, C., Evers, M., 
        Akça, O., Jiang, D., Hurtig, K. (2022): [Europäische Gasversorgungssicherheit aus technischer und 
        wirtschaftlicher Perspektive vor dem Hintergrund unterbrochener Versorgung aus Russland, Studie im 
        Auftrag des Akademienprojektes Energiesysteme der Zukunft“ (ESYS)], Förderkennzeichen 03EDZ2016, 
        Fraunhofer IEG & SCAI, TU Berlin, Berlin.
    """)
    col_x2, col_y2 = st.columns([1, 1])
    with col_x2:
        st.image("source/acatech_2.jpg", width=650)
    with col_y2:
        st.image("source/acatech_1.png", width=650)

