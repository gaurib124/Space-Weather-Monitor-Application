

import streamlit as st
import tools
from config import app_styles
from modules import current_conditions
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
  
    st.set_page_config(page_title='space', page_icon=':rocket:',
                       initial_sidebar_state='expanded')

    #############################################################
    # HTML Styles
    app_styles.apply(st)

  
    st.sidebar.title('Space Weather Monitor Application 🚀')
    tool_name = st.sidebar.selectbox('Choose a Tool from the list', list(tools.TOOLS.keys()), 0)
    tool = tools.TOOLS[tool_name][0]

    if tool_name == '—':
        st.write('# Welcome to Space Weather Monitor Application!')
    else:
        st.markdown('# %s' % tool_name)
        description = tools.TOOLS[tool_name][1]
        if description:
            st.write(description)
        # Clear everything from the intro page.
        # We only have 4 elements in the page so this is intentional overkill.
        for i in range(90):
            st.empty()

    tool()

    current_conditions(st)


if __name__ == '__main__':
    run()
