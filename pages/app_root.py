from layouts.saas_app import AppMainLayout, SideBarMenuLayout, AppHeaderMenuLayout
from pydzn.components import Text
from components.sidebar import sidebar
from components.app_header import app_header


def app_root_page(debug=False):
    """
    This the landing page of the app when users first log in
    """
    
    return AppMainLayout(
        debug=debug,
        region_dzn={
            "left_sidebar": "border-0 border-r border-slate-300 border-solid",
            "appbar": "border-0 border-b border-slate-300 border-solid"
        }
    ).render(
        left_sidebar=sidebar(debug=debug),
        appbar=app_header(debug=debug),
        content=Text(text="C").render(),
    )
