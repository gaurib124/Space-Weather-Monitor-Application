def apply(st):
    # Hide the menu and footer
    st.markdown("""
        <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
        </style>
    """, unsafe_allow_html=True)

    # Reduce top padding for a cleaner layout
    st.markdown("""
        <style>
            .block-container {
                padding-top: 1rem;
                padding-bottom: 1rem;
            }
        </style>
    """, unsafe_allow_html=True)

    # Slim horizontal lines
    st.markdown("""
        <style>
            hr {
                margin: 8px 0px;
                border: 0;
                height: 2px;
                background: linear-gradient(to right, #ff6b6b, #f06595);
                border-radius: 2px;
            }
        </style>
    """, unsafe_allow_html=True)

    # Modern button styling
    st.markdown('''
        <style>
            div.stButton > button:first-child {
                display: inline-flex;
                align-items: center;
                justify-content: center;
                min-width: 100%;
                padding: 0.6rem 1.2rem;
                font-weight: 600;
                border-radius: 12px;
                background: linear-gradient(135deg, #ff6b6b, #f06595);
                color: #fff;
                border: none;
                transition: all 0.3s ease;
                box-shadow: 0 4px 8px rgba(240, 101, 149, 0.3);
            }
            div.stButton > button:hover {
                background: linear-gradient(135deg, #f06595, #d6336c);
                transform: scale(1.03);
                box-shadow: 0 6px 12px rgba(240, 101, 149, 0.4);
            }
            div.stButton > button:active {
                transform: scale(0.98);
                background: linear-gradient(135deg, #d6336c, #a61e4d);
            }
        </style>
    ''', unsafe_allow_html=True)

    # Modern download button styling
    st.markdown('''
        <style>
            div.stDownloadButton > button:first-child {
                display: inline-flex;
                align-items: center;
                justify-content: center;
                min-width: 100%;
                padding: 0.6rem 1.2rem;
                font-weight: 600;
                border-radius: 12px;
                background: linear-gradient(135deg, #4dabf7, #339af0);
                color: #fff;
                border: none;
                transition: all 0.3s ease;
                box-shadow: 0 4px 8px rgba(51, 154, 240, 0.3);
            }
            div.stDownloadButton > button:hover {
                background: linear-gradient(135deg, #339af0, #1c7ed6);
                transform: scale(1.03);
                box-shadow: 0 6px 12px rgba(51, 154, 240, 0.4);
            }
            div.stDownloadButton > button:active {
                transform: scale(0.98);
                background: linear-gradient(135deg, #1c7ed6, #1864ab);
            }
        </style>
    ''', unsafe_allow_html=True)
