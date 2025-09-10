from flask import Flask, Response, render_template
from pydzn.dzn import compile_used_css
from pages.app_home import app_home
from pydzn.components import Button, Text, Card
from pydzn.grid_builder import layout_builder


# Button.set_default_choices(variant="acme:danger", size="lg") # set project defaults

# Set to True if you want to see layout red dotted
DZN_DEBUG=True

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
    body = app_home()
    return render_template("app-home.html", body=body)


@app.get("/layout-demo")
def demo_layout():
    """
    Construct a layout in debug mode
    """
    
    # ----- Outer layout -----
    DashboardLayout = (
        layout_builder()
        .columns(sidebar=180, main="1fr")
        .rows(hero="20vh", subhero="10vh", content="1fr")
        .region("sidebar",  col="sidebar", row=None, row_span=None)
        .region("hero",     col="main",    row="hero")
        .region("subhero",  col="main",    row="subhero")
        .region("content",  col="main",    row="content")
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
        region_dzn={"sidebar": "bg-elevated p-4", "hero": "p-4", "subhero": "p-4", "dsubhero": "p-4", "content": "p-4"},
        debug=DZN_DEBUG,
    )

    page_content = layout.render(
        sidebar=Text(text="A").render(),
        hero=Text(tag="h1", text="Foo App").render(),
        subhero=Text(tag="h2", text="Created with pydzn!").render(),
        content=content_grid
    )
    return render_template("layout-demo.html", body=page_content)


if __name__ == "__main__":
    # Optional direct run: python app.py
    app.run(debug=True)

