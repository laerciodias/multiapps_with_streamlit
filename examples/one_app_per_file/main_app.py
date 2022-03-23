from st_multiapp_pkg.streamlit_multiapp import StreamlitMultiApp
import app_foo
import app_bar

multi_app = StreamlitMultiApp()

multi_app.register_app("Foo", app_foo.run)
multi_app.register_app("Bar", app_bar.run)

multi_app.run()
