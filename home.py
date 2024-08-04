import streamlit as st
from common import config_page, sidebar_menu


config_page('Career Dashboard')
sidebar_menu()

# CSS
st.markdown("""
    <style>
    .title {
        font-size: 36px;
        font-weight: bold;
        color: #4CAF50;
    }
    .subtitle {
        font-size: 24px;
        font-weight: bold;
        color: #333;
    }
    .normal-text {
        font-size: 16px;
        color: #333;
    }
    .highlight {
        font-size: 16px;
        font-weight: bold;
        color: #FF5733;
    }
    a {
        color: #1E90FF;
        text-decoration: none;
        font-style: italic;
    }
    a:hover {
        text-decoration: underline;
        color: #FF5733;
    }
    </style>
    """, unsafe_allow_html=True)

# body

st.markdown('<div class="title">Welcome to My Career Dashboard!</div>',
            unsafe_allow_html=True)
st.markdown('<div class="normal-text">This dashboard serves as a comprehensive '
            'overview of my professional journey, showcasing key projects, '
            'research endeavors, tools I\'ve developed, and my teaching '
            'experiences. Explore each section to gain insights into my work '
            'and contributions.</div>', unsafe_allow_html=True)

st.markdown('<div class="subtitle">About Me</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="normal-text">'
    ' <strong>Name</strong>: <span class="highlight">Dongrui Jiang</span><br>'
    ' <strong>Birth Year</strong>: <span class="highlight">1994</span><br>'
    ' <strong>Current Title</strong>:'
    '  <a href="https://www.tu.berlin/er/ueber-uns/team/dongrui-jiang" '
    '     target="_blank">Research Associate at TU Berlin</a><br>'
    ' <strong>Contact</strong>: '
    '  <a href="mailto:jiang@er.tu-berlin.de" '
    '     target="_blank">jiang@er.tu-berlin.de</a><br>'
    '</div>',
    unsafe_allow_html=True)

st.markdown(
    '<div class="normal-text">'
    'I have been studying and working in the field of gas network since 2018, '
    'focusing on optimizing workable flow patterns in complex natural gas '
    'networks. My work aims to meet various energy targets in natural gas and '
    'hydrogen scenarios, considering elements such as trading flows, storage, '
    'and demand sectors including industry, heating, transportation, and '
    'important gas network facilities like compressor stations. I am dedicated '
    'to developing a powerful and intelligent tool to create a reliable energy '
    'network that combines gas, electricity, and other energy sources for future'
    ' energy scenarios.'
    '</div>',
    unsafe_allow_html=True)

st.markdown('<div class="subtitle">Dashboard Sections</div>',
            unsafe_allow_html=True)
st.markdown(
    '<div class="normal-text"><ul>'
    '<li><strong>Projects 📁</strong>: A collection of significant projects '
    'I have worked on.</li>'
    '<li><strong>Research 🔬</strong>: Including published papers, ongoing '
    'studies, and collaborative efforts.</li>'
    '<li><strong>Tools 🛠️</strong>: An array of tools and applications I have '
    'developed or contributed to.</li>'
    '<li><strong>Teaching 👩‍🏫</strong>: An overview of my teaching experiences.</li>'
    '</ul></div>',
    unsafe_allow_html=True)

# contact info
st.markdown("""
    <hr style="border:1px solid lightgray; margin-top:15px; margin-bottom:10px">
    Feel free to contact the author via email
    <a href="mailto:jdr_maggiea@hotmail.com">jdr_maggiea@hotmail.com</a>
    :)""",
    unsafe_allow_html=True)
