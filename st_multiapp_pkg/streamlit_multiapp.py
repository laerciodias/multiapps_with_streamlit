import streamlit as st
import pandas as pd


class StreamlitMultiApp:
    _instance = None
    apps = None

    def __new__(cls, *args, **kwargs):
        if not isinstance(cls._instance, cls):
            cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self):
        if self.apps is None:
            self.apps = pd.Series(dtype=object)

    def register_app(self, app_name, app_func):
        if app_name not in self.apps.index:
            self.apps[app_name] = app_func

    def run(self):
        selected_app_name = st.sidebar.radio(
            label='Select an app',
            options=self.apps.index
        )

        self.apps[selected_app_name]()

