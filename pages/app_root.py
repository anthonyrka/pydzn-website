from layouts.saas_app import WCAppMainLayout
from pydzn.components import Text


def app_root_page(debug=False):
    """
    This the landing page of the app when users first log in
    """
    
    return WCAppMainLayout(
        debug=debug,
        region_dzn={
            "left_sidebar": "border-0 border-r border-slate-300 border-solid",
            "appbar": "border-0 border-b border-slate-300 border-solid"
        }
    ).render(
        left_sidebar=Text(text="A").render(),
        appbar=Text(text="B").render(),
        content=Text(text="C").render(),
    )
