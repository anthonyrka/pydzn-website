from layouts.saas_app import AppHeaderMenuLayout, AppHeaderMobileMenuLayout
from pydzn.components import NavItem, Text
from pydzn.responsive import responsive_pair


def app_header(debug, brand_width=264, app_menu_width=124):
    nav_variant="simple-item"
   
    brand = (
        NavItem(
            variant=nav_variant,
            children=Text("Acme Widget Co").render()
            )
        .render()
    )

    tasks = (
        NavItem(variant=nav_variant, children=Text("Tasks").render())
        .center() # x+y+text centering
        .render()
    )

    customers = (
        NavItem(variant=nav_variant, children=Text("Customers").render())
        .center()
        .render()
    )

    orders = (
        NavItem(
            variant=nav_variant,
            children=Text("Orders").render(),
            dzn="no-underline text-[inherit]"   # kill underline + inherit color
            )
            .as_link("/widget-billing")
        .center()
        .render()
    )

    notifications = (
        NavItem(variant=nav_variant, children=Text("Notifications").render())
        .center()
        .render()
    )

    user_profile = (
        NavItem(variant=nav_variant, children=Text("Profile").render())
        .center()
        .render()
    )

    desktop_html = AppHeaderMenuLayout(
        debug=debug
    ).render(
        brand=brand,
        tasks=tasks,
        customers=customers,
        orders=orders,
        notifications=notifications,
        user_profile=user_profile,
    )

    mobile_html = AppHeaderMobileMenuLayout(
        debug=debug
    ).render(
        brand=brand,
        hamburger_menu=Text(text="Menu").render()
    )
    return responsive_pair(desktop_html=desktop_html, mobile_html=mobile_html)

