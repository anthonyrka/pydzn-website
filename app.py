from flask import Flask, Response, render_template
from pydzn.dzn import compile_used_css
from pages.app_root import app_root_page
from pages.app_widget_billing import app_widget_billing_page
from pages.marketing_home import marketing_home_page

from pydzn.components import Button, Text, Card, NavItem, Sidebar
from pydzn.grid_builder import layout_builder


# Button.set_default_choices(variant="acme:danger", size="lg") # set project defaults

# Set to True if you want to see layout red dotted
DZN_DEBUG=False

app = Flask(__name__)


# route required to support dzn css semantic classes
@app.get("/_dzn.css")
def dzn_css():
    try:
        css = compile_used_css()
        return Response(css, mimetype="text/css", headers={"Cache-Control": "no-store"})
    except Exception as e:
        # Helpful error in the browser if something goes sideways
        import traceback
        return Response(
            "/* dzn error:\n" + traceback.format_exc() + "*/",
            status=500,
            mimetype="text/plain",
        )


def register_project_variants():
    Button.attach_variant_library(
        "acme",  # namespace
        variants={
            "glass": (
                "rounded-md border border-transparent "
                "bg-[rgba(255,255,255,.12)] backdrop-blur "
                "text-[black] shadow-md hover:shadow-lg"
            ),
            "danger": (
                "rounded-sm border-0 "
                "bg-[rgb(220,38,38)] text-[white] "
                "shadow-md hover:shadow-lg"
            ),
        },
        sizes={
            "sm": "px-3 py-1",
            "md": "px-5 py-2",
            "xs": "px-2 py-1 text-[12px]",
            "xl": "px-7 py-4"
        },
        # tones={}  # optional for later
    )

# call this once on startup
register_project_variants()


@app.get("/")
def home():
    """
    Serve an app organized with layout/ and pages/
    """
    body = marketing_home_page(debug=DZN_DEBUG)
    return render_template("app-home.html", body=body)


@app.get("/dashboard")
def dashboard():
    body = app_root_page(debug=DZN_DEBUG)
    return render_template("app.html", body=body)


@app.get("/widget-billing")
def widget_billing():
    body = app_widget_billing_page(debug=DZN_DEBUG)
    return render_template("app.html", body=body)


@app.get("/layout-demo")
def demo_layout():
    """
    Construct a layout in debug mode
    """
    
    # # ----- Outer layout -----
    # DashboardLayout = (
    #     layout_builder()
    #     .columns(sidebar=180, main="1fr")
    #     .rows(hero="20vh", subhero="10vh", content="1fr")
    #     .region("sidebar",  col="sidebar", row=None, row_span=None)
    #     .region("hero",     col="main",    row="hero")
    #     .region("subhero",  col="main",    row="subhero")
    #     .region("content",  col="main",    row="content")
    #     .build(name="DashboardLayout")
    # )
    APPBAR = 48      # px  -> your appbar row height
    SIDEBAR = 180    # px  -> your sidebar column width
    HERO_H = "10vh"  #     -> your hero row height (already in rows())


    DashboardLayout = (
        layout_builder()
        .columns(sidebar=SIDEBAR, main="1fr")                        # 2 columns
        .rows(appbar=f"{APPBAR}px", hero=HERO_H, subhero="10vh", content="1fr")  # add appbar row at the top
        .region("appbar",  col="sidebar", row="appbar", col_span=2)       # spans both columns
        .region("sidebar", col="sidebar", row="hero", row_span=None)      # start under appbar; span rest
        .region("hero",    col="main",    row="hero")
        .region("subhero", col="main",    row="subhero")
        .region("content", col="main",    row="content")
        .build(name="DashboardLayout")
    )

    # ----- Inner sublayout: 3 columns inside content -----
    DashboardContent3Cols = (
        layout_builder()
        .columns(col1="1fr", col2="1fr", col3="1fr")
        .rows(track="1fr")
        .region("col1", col="col1", row="track")
        .region("col2", col="col2", row="track")
        .region("col3", col="col3", row="track")
        .build(name="DashboardContent3Cols")
    )

    
    print(Button.list_variants())          # ['ghost-neutral', 'link-primary', 'outline-primary', 'solid-primary', ...]
    print(Button.list_sizes())             # ['lg', 'md', 'sm', ...]
    print(Button.list_tones())             # [] by default in the example

    # or a structured blob (great for docs or UI pickers)
    print(Button.available_options())
    dft_txt = Text("Built-in Card: default", tag="h2", dzn="text-center")
    sub_txt = Text(
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam gravida mattis ex sit amet elementum. Donec tincidunt nunc ac diam ullamcorper, euismod gravida est pretium. Sed tincidunt, nisl at sollicitudin dictum, urna mauris maximus mi, vitae blandit ipsum neque eu velit. Pellentesque sagittis commodo vehicula. Nunc aliquam metus non augue viverra sollicitudin. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Sed id sem a nisl tincidunt sodales.",
        dzn="text-center p-4")
    dft_btn = Button(
        text="Save",
        dzn="w-[fit-content] self-center",
        # variant="acme:glass", # custom variant
        # variant="solid-primary", # built-in variant
        size="md"
    )
    dft_card = Card(tag="div", variant="glass", children=dft_txt.render() + sub_txt.render() + dft_btn.render())

    v0_txt = Text("Built-in Card Variant: elevated", tag="h2", dzn="text-center")
    v0_btn = Button(
        text="Save",
        dzn="w-[fit-content] self-center",
        # variant="acme:glass", # custom variant
        variant="solid-primary", # built-in variant
        size="lg"
    )
    v0_card = Card(tag="div", variant="elevated", children=v0_txt.render() + sub_txt.render() + v0_btn.render())

    v1_txt = Text("Built-in Card Variant: plain", tag="h2", dzn="text-center")
    v1_btn = Button(
        text="Save",
        dzn="w-[fit-content] self-center",
        # variant="acme:glass", # custom variant
        variant="acme:glass", # built-in variant
        size="xl"
    )
    v1_card = Card(tag="div", variant="plain", children=v1_txt.render() + sub_txt.render() + v1_btn.render())

    content_grid = DashboardContent3Cols(
        region_dzn={"col1": "p-8", "col2": "p-8", "col3": "p-8"}, # column 1 has padding 2px, column 2px has padding 2px and column3 has padding 2px
        debug=DZN_DEBUG,
    ).render(
        col1=dft_card.render(),
        col2=v0_card.render(),
        col3=v1_card.render(),
    )

    layout = DashboardLayout(
        region_dzn={
            "appbar":  "sticky top-0 z-[20] bg-elevated border-0 border-b border-subtle border-solid bg-[white] p-4",

            # sidebar stays fixed at the left
            "sidebar": f"fixed top-[{APPBAR}px] left-0 w-[{SIDEBAR}px] "
                    f"h-[calc(100vh-{APPBAR}px)] overflow-y-auto overscroll-contain" 
                    "border-0 border-r border-subtle border-solid",

            # hero fixed, offset by sidebar using margin-left, and width subtracting sidebar
            "hero": (
                f"fixed top-[{APPBAR}px] left-0 right-0 ml-[{SIDEBAR}px] "
                f"h-[{HERO_H}] z-[15]"
                "bg-elevated border-bottom bg-[white] p-4 border-0 border-b-2 border-subtle border-solid"
            ),


            "subhero": "p-4 shrink-0",
            "content": "",
        },
        debug=DZN_DEBUG,
    )


    # Sidebar list
    sidebar_variant = "sidebar-squared-underline"

    # overview_item = (
    #     NavItem(variant="sidebar-underline", children=Text("Overview").render())
    #     .center()                           # x+y+text centering
    #     .height(64)                         # fixed height
    #     .full_width()                       # fill sidebar width
    #     .bottom_divider("subtle")           # single line below
    #     .hover(bg="rgba(37,99,235,.06)", text="#2563eb", underline="blue-500")
    #     .focus(bg="rgba(37,99,235,.10)")    # optional focus wash
    #     .render()
    # )

    items = [
        # overview_item,
        NavItem(variant=sidebar_variant, children=Text("Overview").render()).render(),
        NavItem(variant=sidebar_variant, children=Text("Activity").render()).render(),
        NavItem(variant=sidebar_variant, children=Text("Reports").render()).render(),
        NavItem(variant=sidebar_variant, children=Text("Settings").render()).render(),
    ]

    sidebar_nav_html = "".join(items)

    SidebarNav4 = (
        layout_builder()
        .columns(track="1fr")  # single column
        # 4 rows for items + a "spacer" that fills remaining height
        .rows(item1="auto", item2="auto", item3="auto", item4="auto", spacer="1fr")
        .region("item1",  col="track", row="item1")
        .region("item2",  col="track", row="item2")
        .region("item3",  col="track", row="item3")
        .region("item4",  col="track", row="item4")
        .region("spacer", col="track", row="spacer")
        .build(name="SidebarNav4")
    )

    sidebar_grid = SidebarNav4(
        # The inner sublayout handles the scrolling & height:
        outer_dzn="h-[calc(100vh-26px)] overflow-y-auto overscroll-contain",
        region_dzn={
            "item1": "", "item2": "", "item3": "", "item4": "",
            "spacer": "",   # just fills space; leave empty
        },
        debug=DZN_DEBUG,
    ).render(
        item1=NavItem(variant=sidebar_variant, children=Text("Overview").render()).render(),
        item2=NavItem(variant=sidebar_variant, children=Text("Activity").render()).render(),
        item3=NavItem(variant=sidebar_variant, children=Text("Reports").render()).render(),
        item4=NavItem(variant=sidebar_variant, children=Text("Settings").render()).render(),
        spacer="",  # nothing to render; keeps items top-aligned
    )


    page_content = layout.render(
        appbar=Text(text="appbar").render(),
        sidebar=sidebar_grid,
        hero=Text(tag="h1", text="Foo App").render(),
        subhero=Text(tag="h2", text="Created with pydzn!").render(),
        content=content_grid
    )
    return render_template("layout-demo.html", body=page_content)


if __name__ == "__main__":
    # Optional direct run: python app.py
    app.run(debug=True)

