from layouts.app import (
    AppHeaderMenuLayout, 
    AppHeaderMobileMenuLayout,
    AppHeaderMobileMenuDropDownLayout
)
from pydzn.components import NavItem, Text, HamburgerMenu
from pydzn.responsive import responsive_pair


def app_header(debug, brand_width=264, app_menu_width=124):
    nav_variant="simple-item"
   
    brand = (
        NavItem(
            variant=nav_variant,
            children=Text("Acme Widget Co").render(),
            )
        .center()
        .as_link("/dashboard")
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

    # tasks = NavItem(variant="simple-item", children=Text("Tasks").render()).render()
    # customers = NavItem(variant="simple-item", children=Text("Tasks").render()).render()
    # orders = NavItem(variant="simple-item", children=Text("Tasks").render()).render()
    # notifications = NavItem(variant="simple-item", children=Text("Tasks").render()).render()
    # user_profile_mobile = NavItem(variant="simple-item", children=Text("Tasks").render()).render()

    dashboard_mobile = (
        NavItem(
            variant=nav_variant,
            children=Text("Dashboard").render(),
            )
        .center()
        .as_link("/dashboard")
        .render()
    )
    drop_down_mobile = AppHeaderMobileMenuDropDownLayout(
        debug=debug
    ).render(
        dashboard=dashboard_mobile,
        tasks=tasks,
        customers=customers,
        orders=orders,
        notifications=notifications,
        user_profile=user_profile
    )

    # Right-side full-height drawer
    menu_btn = HamburgerMenu(
        mode="right",
        drawer_width=320,
        show_backdrop=True,
        children=drop_down_mobile,
        dzn="bg-[white]",   # forwarded to the panel automatically
        panel_dzn="p-[24px]" # this is how you set the semantic css classes for the drawer (panel)
    ).render()


    mobile_html = AppHeaderMobileMenuLayout(
        debug=debug,
        region_dzn = {
            "brand": "flex justify-center items-center",
            "hamburger_menu": "flex justify-center items-center"
        }
    ).render(
        brand=brand,
        hamburger_menu=menu_btn
    )
    return responsive_pair(desktop_html=desktop_html, mobile_html=mobile_html)

