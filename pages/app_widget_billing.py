from layouts.saas_app import (
    AppMainLayout,
    SideBarMenuLayout,
    WidgetBillingLayout,
    AppHeaderMenuLayout,
    HEADER_HEIGHT,
    MENU_ITEM_HEIGHT,
    BRAND_WIDTH,
    APP_MENU_WIDTH
)
from pydzn.components import Text
from components.sidebar import sidebar
from components.app_header import app_header


def app_widget_billing_page(debug=False):
    """
    This the client billing page of the app
    """
    
    billing_content = WidgetBillingLayout(
        debug=debug,
        region_dzn={
            "widget_billing": "border-0 border-r border-slate-300 border-solid"
        }
        ).render(
            widget_billing=Text(text="Widget Billing").render(),
            widget_program=Text(text="Widget Attributes").render()
            )

    body = AppMainLayout(
        debug=debug,
        region_dzn={
            "left_sidebar": "border-0 border-r border-slate-300 border-solid",
            "appbar": "border-0 border-b border-slate-300 border-solid"
        }
    ).render(
        left_sidebar=sidebar(debug=debug, logo_height=HEADER_HEIGHT, nav_item_height=MENU_ITEM_HEIGHT),
        appbar=app_header(debug=debug, brand_width=BRAND_WIDTH, app_menu_width=APP_MENU_WIDTH),
        content=billing_content,
    )

    return body
