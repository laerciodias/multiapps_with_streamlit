import streamlit as st
from st_multiapp_pkg.streamlit_multiapp import StreamlitMultiApp


def app_foo():
    st.markdown("# I am a FOO app")


def app_bar():
    st.markdown("# I am a BAR app")


multi_app = StreamlitMultiApp()

multi_app.register_app("Foo", app_foo)
multi_app.register_app("Bar", app_bar)

multi_app.run()
