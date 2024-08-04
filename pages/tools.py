import time
import streamlit as st
from common import config_page, sidebar_menu

config_page('Tool')
sidebar_menu()

button_css = """
<style>
    .button {
        display: inline-block;
        padding: 10px 20px;
        font-size: 16px;
        cursor: pointer;
        text-align: center;
        text-decoration: none;
        outline: none;
        color: #fff;
        background-color: #4CAF50;
        border: none;
        border-radius: 15px;
        box-shadow: 0 9px #999;
        width: 200px;  /* Adjust button width */
    }

    .button:hover {background-color: #3e8e41}

    .button:active {
        background-color: #3e8e41;
        box-shadow: 0 5px #666;
        transform: translateY(4px);
    }

    .button-container {
        display: flex;
        flex-direction: column;
        gap: 10px;
    }
</style>
"""

st.title("Tools🛠️")
st.write("""
    Welcome to the Tools Page! This page showcases all the tools I've created or collaborated on for gas network 
    simulation. These tools cover the entire simulation process, from network generation and scenario data definition 
    to network assignment, compressor configuration, and simulator connection via API. They also include 
    functionalities for collecting simulation results for post-processing and analysis.

    On the left, you will find a list of tools for different processes. On the right, you can see some sample 
    results from these tools.
""")

st.divider()
col1, col2 = st.columns([2, 3])

button_html = """
<div class="button-container">
    <button class="button" onclick="document.getElementById('tool1').click();">Tool 1</button>
    <button class="button" onclick="document.getElementById('tool2').click();">Tool 2</button>
    <button class="button" onclick="document.getElementById('tool3').click();">Tool 3</button>
    <button class="button" onclick="document.getElementById('tool4').click();">Tool 4</button>
</div>
"""
st.markdown(button_css, unsafe_allow_html=True)
if 'selected_tool' not in st.session_state:
    st.session_state['selected_tool'] = "Tool 1"

with col1:
    if st.button("Network Generation", key='tool1', help="",
                 use_container_width=True):
        st.session_state['selected_tool'] = "Tool 1"
        st.markdown("""
        Network Generation tool focus on network topology generation, aiming to create a new gas network (natural 
        gas or hydrogen) based on the latest Germany natural gas network. The tools perform the following tasks:

        **Convert Topology Data**:
        - Converts topology data among different formats including CSV/Excel tables, MongoDB databases, 
        SQL databases, Python DataFrames, and simulator APIs.

        **Generate New Network**:
        - Generates a new connected natural gas or hydrogen network based on targeted gas suppliers, 
        demand locations, and pipeline lists.

        **Visualize Generated Network**:
        - Visualizes the generated network for verification and analysis, ensuring it meets the necessary 
        criteria and configurations.
        """)
    if st.button("Scenario Definition", key='tool2', help="",
                 use_container_width=True):
        st.session_state['selected_tool'] = "Tool 2"
        st.markdown("""
        The Scenario Definition tool allocates defined supply and demand flows into the nodes of a generated network. 
        It also allows for pre-checking of the flow allocation within the network before proceeding with simulation.
        """)
    if st.button("Simulation Toolchain", key='tool3', help="",
                 use_container_width=True):
        st.session_state['selected_tool'] = "Tool 3"
        st.markdown("""
        The Simulation Execution tool automatically delivers network and scenario data into the simulator for execution.
        Additionally, it helps set configurations for compressors and other active elements in the network to ensure a 
        successful flow that meets the required supply and demand settings.
        """)

    if st.button("Results Validation", key='tool4', help="",
                 use_container_width=True):
        st.markdown("""
        After obtaining results from the simulator, the Results Visualization tool enables post-processing to convert 
        these results into preferred visual formats. This includes generating figures, interactive HTML pages, or 
        table data tailored for specific purposes.
        """)
        st.session_state['selected_tool'] = "Tool 4"

with col2:
    if st.session_state['selected_tool'] == 'Tool 1':
        col2.image("source/topo_tool.png", use_column_width=True)
        # col2.image("source/topo_tool_2.png", use_column_width=True)
    elif st.session_state['selected_tool'] == 'Tool 2':
        col_x, col_y = st.columns([1, 2])
        with col_x:
            option = st.selectbox(
                "Select a sample scenario to check allocated flows for view",
                ("max imports", "max load", "min imports"),
            )
            if option == "max imports":
                col_y.image("source/max_imports_3199_44675_2045.png", use_column_width=0)
            if option == 'max load':
                col_y.image("source/max_load_8167_44675_2045.png", use_column_width=0)
            if option == 'min imports':
                col_y.image("source/min_imports_7623_44675_2045.png", use_column_width=0)
    elif st.session_state['selected_tool'] == 'Tool 3':
        fig_container = st.empty()
        figures = ['source/simu_tool.PNG', 'source/simu_tool_2.PNG', 'source/simu_tool_3.PNG']
        fig_captions = ["Figure 1: One Compressor Configuration",
                        "Figure 2: Active Elements Configuration on the Whole Network",
                        "Figure 3: Execution of the Simulation via API"]
        while True:
            for fig, caption in zip(figures, fig_captions):
                fig_container.image(fig, caption=caption)
                time.sleep(3)
    elif st.session_state['selected_tool'] == 'Tool 4':
        st.video("source/scenario_tool.mp4")
