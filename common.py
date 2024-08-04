import streamlit as st


def config_page(Page_Title):
    icon_dict = {
        'Career Dashboard': "🧊",
        'Project': '📊',
        'Tool': '🛠️',
        'Publication': '💡',
        'Others': '👩‍🏫',
    }

    st.set_page_config(
        page_title=Page_Title,
        page_icon=icon_dict[Page_Title],
        layout="wide",
        initial_sidebar_state="expanded",
        menu_items={}
    )
    st.markdown("""
        <style>
            .reportview-container {margin-top: -2em;}
            #MainMenu {visibility: hidden;}
            .stDeployButton {display:none;}
            footer {visibility: hidden;}
            #stDecoration {display:none;}
            .block-container {padding-top: 30px;
                              padding-bottom: 30px;
                              padding-left: 80px;
                              padding-right: 80px;}
        </style>
    """, unsafe_allow_html=True)
    return


def sidebar_menu():
    # navigation sidebar
    st.sidebar.page_link('home.py', label='🏠 Home')
    st.sidebar.page_link('pages/projects.py', label='📊 Projects')
    st.sidebar.page_link('pages/tools.py', label='🛠️ Tools')
    st.sidebar.page_link('pages/publication.py', label='💡 Publication')
    st.sidebar.page_link('pages/others.py', label='👩‍🏫 Others')
    return