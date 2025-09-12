from layouts.saas_app import (
    AppMainLayout, AppMobileMainLayout, # a page can support multiple layout versions so we'll implement both
    SideBarMenuLayout, AppHeaderMenuLayout,
    HEADER_HEIGHT, MENU_ITEM_HEIGHT, BRAND_WIDTH, APP_MENU_WIDTH
)
from components.sidebar import sidebar
from components.app_header import app_header
from components.dashboard_metrics import dashboard
from pydzn.responsive import responsive_pair # combines layouts and allows client to choose, as an example, between mobile or desktop 


def app_root_page(debug=False):
    desktop = AppMainLayout(
        debug=debug,
        region_dzn={
            "left_sidebar": "border-0 border-r border-slate-300 border-solid",
            "appbar": "border-0 border-b border-slate-300 border-solid",
        }
    ).render(
        left_sidebar=sidebar(debug=debug, logo_height=HEADER_HEIGHT, nav_item_height=MENU_ITEM_HEIGHT),
        appbar=app_header(debug=debug, brand_width=BRAND_WIDTH, app_menu_width=APP_MENU_WIDTH),
        content=dashboard(debug=debug),
    )

    mobile = AppMobileMainLayout(
        debug=debug,
        region_dzn={
            "appbar": "border-0 border-b border-slate-300 border-solid",
        }
    ).render(
        appbar=app_header(debug=debug, brand_width=BRAND_WIDTH, app_menu_width=APP_MENU_WIDTH),
        content=dashboard(debug=debug),
    )

    # responsive pair formats the output so that the rendered result is chosen by the client (desktop or mobile)
    return responsive_pair(desktop_html=desktop, mobile_html=mobile)
