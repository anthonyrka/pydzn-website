from layouts.saas_app import (
    AppMainLayout,
    SideBarMenuLayout,
    AppHeaderMenuLayout,
    AppDashboardLayout,
    HEADER_HEIGHT,
    MENU_ITEM_HEIGHT,
    BRAND_WIDTH,
    APP_MENU_WIDTH
)
from pydzn.components import Text
from components.sidebar import sidebar
from components.app_header import app_header
from components.dashboard_metrics import dashboard


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
        left_sidebar=sidebar(debug=debug, logo_height=HEADER_HEIGHT, nav_item_height=MENU_ITEM_HEIGHT),
        appbar=app_header(debug=debug, brand_width=BRAND_WIDTH, app_menu_width=APP_MENU_WIDTH),
        content=dashboard(debug=debug),
    )
