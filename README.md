# pydzn-website
A website made with [pydzn](https://github.com/anthonyrka/pydzn)

## What is pydzn
pydzn or "py design" is a lightweight python library that makes it easy to design, build and serve complex websites all in python. It provides an api into CSS-grid for designing layouts and serve as a light-weight website builder with a built-in, and extendable, component library as well as a library for setting CSS semantic classes.

## A website builder for python developers (not front-end developers)
The layout builder contains a debug mode allowing you to visualize the structure of your layout. Each named region is a slot which can be passed a sub-layout or a component in the layout's render function.

<p align="center">
  <img src="docs/website_builder_sortof.gif" alt="mobile" width="640">
</p>

## Responsive is built-in
Build responsive layouts with pydzn

<p align="center">
  <img src="docs/pydzn_responsive.gif" alt="mobile" width="640">
</p>

The above layouts are combined desktop and mobile versions:
```python

from pydzn.grid_builder import layout_builder

# This is the Main App layout structure we've created below for DESKTOP
"""
                    column::left_column    column::main_column
row:header_row      region:left_sidebar    region:appbar
row:content_row     region:left_sidebar    region:content

The layout accepts the following components in render function signature: left_sidebar, appbar, content
"""
AppMainLayout = (
    layout_builder()
    .fill_height("100vh", property="height") # sets up the page to restrict height to view height
    .columns(left_column=LEFT_SIDEBAR_WIDTH, main_column="1fr") # split the main layout into two columns: sidebar and main
    .rows(header_row=HEADER_HEIGHT, content_row="1fr") # add 2 rows: a header section and a content section stacked 
    .region("left_sidebar", col="left_column", row="header_row", row_span=2) # place the sidebar into the left_sidebar column in the first row and span both rows
    .region("appbar", col="main_column", row="header_row", col_span=1) # Add the appbar to the right of sidebar in the main section and span the last row
    .region("content", col="main_column", row="content_row") # declare the empty content section which is the last row in main
    .build(name="AppMainLayout")
)

# This is the Main App layout structure we've created below for MOBILE
"""
                    column::main_column
row:header_row      region:appbar
row:content_row     region:content

The layout accepts the following components in render function signature: appbar, content
"""
AppMainMobileLayout = (
    layout_builder()
    .fill_height("100vh", property="height")
    .columns(main_column="1fr")
    .rows(header_row=HEADER_HEIGHT_MOBILE, content_row="1fr")
    .region("appbar",  col="main_column", row="header_row")
    .region("content", col="main_column", row="content_row")
    .build(name="AppMainMobileLayout")
)

# ----- App header menu slots -----#
AppHeaderMenuLayout = (
    layout_builder()
    # make the inner grid fill the parent (the appbar row), not the viewport
    .fill_height("100%", property="height") # was min-height:100vh (implicit default)
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

# ----- App header mobile menu layout ----#
AppHeaderMobileMenuLayout = (
    layout_builder()
    .fill_height("100%", property="height")
    .columns(brand_col=BRAND_WIDTH, spacer_col="1fr", hamburger_menu_col=100)
    .rows(app_header_mobile_row=f"minmax({HEADER_HEIGHT_MOBILE}px, auto)") # this container holds the app header for mobile layout so height must match
    .region("brand", col="brand_col", row="app_header_mobile_row")
    .region("hamburger_menu", col="hamburger_menu_col", row="app_header_mobile_row")
    .build(name="AppHeaderMobileMenuLayout")
)

```

These layouts contain render functions with a signature containing the named slots for variables, in the case of AppMainMobileLayout, the hamburger_menu slot is passed a built-in hamburger menu component:

```python
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
```

