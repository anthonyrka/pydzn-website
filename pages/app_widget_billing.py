from layouts.app import (
    AppMainLayout,
    AppMainMobileLayout,
    SideBarMenuLayout,
    WidgetBillingLayout,
    WidgetBillingMobileLayout,
    AppHeaderMenuLayout,
    HEADER_HEIGHT,
    HEADER_HEIGHT_MOBILE,
    MENU_ITEM_HEIGHT,
    BRAND_WIDTH,
    APP_MENU_WIDTH
)
from pydzn.components import Text
from components.sidebar import sidebar
from components.app_header import app_header
from pydzn.responsive import responsive_pair


def app_widget_billing_page(debug=False):
    """
    This the client billing page of the app
    """
    
    desktop_billing_content = WidgetBillingLayout(
        debug=debug,
        region_dzn={
            "widget_billing": "border-0 border-r border-slate-300 border-solid"
        }
        ).render(
            widget_billing=Text(text="Widget Billing").render(),
            widget_program=Text(text="Widget Attributes").render()
            )

    mobile_billing_content = WidgetBillingMobileLayout(
        debug=debug,
        region_dzn = {},
    ).render(
        widget_billing=Text(text="Widget Billing").render(),
        widget_program=Text(text="Widget Attributes").render()
    )

    desktop = AppMainLayout(
        debug=debug,
        region_dzn={
            "left_sidebar": "border-0 border-r border-slate-300 border-solid",
            "appbar": "border-0 border-b border-slate-300 border-solid"
        }
    ).render(
        left_sidebar=sidebar(debug=debug, logo_height=HEADER_HEIGHT, nav_item_height=MENU_ITEM_HEIGHT),
        appbar=app_header(debug=debug, brand_width=BRAND_WIDTH, app_menu_width=APP_MENU_WIDTH),
        content=desktop_billing_content,
    )

    mobile = AppMainMobileLayout(
        debug=debug,
        region_dzn={"appbar": "sticky top-0"}
    ).render(
        left_sidebar=sidebar(debug=debug, logo_height=HEADER_HEIGHT, nav_item_height=MENU_ITEM_HEIGHT),
        appbar=app_header(debug=debug, brand_width=BRAND_WIDTH, app_menu_width=APP_MENU_WIDTH),
        content=mobile_billing_content,
    )

    return responsive_pair(desktop_html=desktop, mobile_html=mobile)
