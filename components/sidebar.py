from layouts.saas_app import SideBarMenuLayout
from pydzn.components import NavItem, Text


def sidebar(debug, logo_height=108, nav_item_height=108):
    nav_variant="sidebar-quiet"

    logo = (
        NavItem(
            variant=nav_variant, 
            children=Text("LOGO").render(),
            dzn="no-underline text-[inherit]"   # kill underline + inherit color
            )
        .as_link("/dashboard")
        .center()                           # x+y+text centering
        .height(logo_height)                         # fixed height
        .full_width()                       # fill sidebar width
        # .bottom_divider("subtle")           # single line below
        # .hover(bg="rgba(37,99,235,.06)", text="#2563eb", underline="blue-500")
        # .focus(bg="rgba(37,99,235,.10)")    # optional focus wash
        .render()
    )

    dashboard = (
        NavItem(
            variant=nav_variant, 
            children=Text("Dashboard").render(),
            dzn="no-underline text-[inherit]"   # kill underline + inherit color
            )
        .as_link("/dashboard")
        .center()                           # x+y+text centering
        .height(nav_item_height)                         # fixed height
        .full_width()                       # fill sidebar width
        # .bottom_divider("subtle")           # single line below
        # .hover(bg="rgba(37,99,235,.06)", text="#2563eb", underline="blue-500")
        # .focus(bg="rgba(37,99,235,.10)")    # optional focus wash
        .render()
    )

    widgets = (
        NavItem(
            variant=nav_variant, 
            children=Text("Widgets").render(),
            dzn="no-underline text-[inherit]"   # kill underline + inherit color
        )
        .center()                           # x+y+text centering
        .height(nav_item_height)                         # fixed height
        .full_width()                       # fill sidebar width
        # .bottom_divider("subtle")           # single line below
        # .hover(bg="rgba(37,99,235,.06)", text="#2563eb", underline="blue-500")
        # .focus(bg="rgba(37,99,235,.10)")    # optional focus wash
        .render()
    )

    orders = (
        NavItem(
            variant=nav_variant,
            children=Text("Orders").render(),
            dzn="no-underline text-[inherit]"   # kill underline + inherit color
            )
        .as_link("/widget-billing")
        .center().height(nav_item_height).full_width()
        .render()
    )


    settings = (
        NavItem(
            variant=nav_variant,
            children=Text("Settings").render(),
            dzn="no-underline text-[inherit]"   # kill underline + inherit color
            )
        .center()                           # x+y+text centering
        .height(nav_item_height)                         # fixed height
        .full_width()                       # fill sidebar width
        # .bottom_divider("subtle")           # single line below
        # .hover(bg="rgba(37,99,235,.06)", text="#2563eb", underline="blue-500")
        # .focus(bg="rgba(37,99,235,.10)")    # optional focus wash
        .render()
    )

    return SideBarMenuLayout(
        debug=debug
    ).render(
        logo=logo,
        dashboard=dashboard,
        widgets=widgets,
        orders=orders,
        settings=settings,
    )
