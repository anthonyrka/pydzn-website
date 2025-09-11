from pydzn.grid_builder import layout_builder


# ----- Main App Layout ----#
# the content section accepts various layouts

LEFT_SIDEBAR_WIDTH=128 # the width of the sidebar
MAIN_SHARE="1fr" # remaining share of the space
HEADER_HEIGHT=108
MENU_ITEM_HEIGHT=HEADER_HEIGHT
BRAND_WIDTH=264
APP_MENU_WIDTH=124


AppMainLayout = (
    layout_builder()
    .fill_height("100vh", property="height") # sets up the page to restrict height to view height
    .columns(left_sidebar=LEFT_SIDEBAR_WIDTH, main="1fr") # split the main layout into two columns: sidebar and main
    .rows(header=HEADER_HEIGHT, content="1fr") # add 2 rows: a header section and a content section stacked 
    .region("left_sidebar", col="left_sidebar", row="header", row_span=2) # place the sidebar into the left_sidebar column in the first row and span both rows
    .region("appbar", col="main", row="header", col_span=1) # Add the appbar to the right of sidebar in the main section and span the last row
    .region("content", col="main", row="content") # declar the empty content section which is the last row in main
    .build(name="AppMainLayout")
)

# ---- This is the sidebar menu slots ---#
SideBarMenuLayout = (
    layout_builder()
    .fill_height("100vh", property="height")
    .columns(menu="1fr")
    .rows(logo=HEADER_HEIGHT, dashboard=MENU_ITEM_HEIGHT, widgets=MENU_ITEM_HEIGHT, orders=MENU_ITEM_HEIGHT, reserved_space="3fr", settings=MENU_ITEM_HEIGHT) # Header Height for logo, menu height for items in case we need more room for more items
    .region("logo", col="menu", row="logo")
    .region("dashboard", col="menu", row="dashboard")
    .region("widgets", col="menu", row="widgets")
    .region("orders", col="menu", row="orders")
    .region("reserved_space", col="menu", row="reserved_space")
    .region("settings", col="menu", row="settings")
    .build(name="SideBarMenuLayout")
)

# ----- Appheader menu slots -----#
AppHeaderMenuLayout = (
    layout_builder()
    # make the inner grid fill the parent (the appbar row), not the viewport
    .fill_height("100%", property="height")     # was min-height:100vh (implicit default)
    .columns(brand=BRAND_WIDTH, spacer="1fr", tasks=APP_MENU_WIDTH, customers=APP_MENU_WIDTH, orders=APP_MENU_WIDTH, notifications=APP_MENU_WIDTH, user_profile=APP_MENU_WIDTH)
    .rows(app_header_main=f"minmax({HEADER_HEIGHT}px, auto)") # these items don't take up the full height of the app header unless you set it here
    .region("brand", col="brand", row="app_header_main")
    .region("spacer", col="spacer", row="app_header_main") # empty; pushes the rest right
    .region("tasks", col="tasks", row="app_header_main")
    .region("customers", col="customers", row="app_header_main")
    .region("orders", col="orders", row="app_header_main")
    .region("notifications", col="notifications", row="app_header_main")
    .region("user_profile", col="user_profile", row="app_header_main")
    .build(name="AppHeaderMenuLayout")
)

# ----- Billing Page Layout ----#
WidgetBillingLayout = (
    layout_builder()
    .fill_height("100%", property="height", apply_to="both") # both refers to the section and it's wrapper so that the page height is restricted to view height
    .columns(left_section="1fr", right_section="1fr")
    .rows(row1="1fr")
    .region("widget_billing", col="left_section", row="row1")
    .region("widget_program", col="right_section", row="row1")
    .build(name="WidgetBillingLayout")
)
