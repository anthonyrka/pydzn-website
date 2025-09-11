from layouts.saas_app import AppHeaderMenuLayout
from pydzn.components import NavItem, Text


def app_header(debug, brand_width=264, app_menu_width=124):
    nav_variant="dropdown-item"
   
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

    return AppHeaderMenuLayout(
        debug=debug
    ).render(
        brand=brand,
        tasks=tasks,
        customers=customers,
        orders=orders,
        notifications=notifications,
        user_profile=user_profile,
    )
