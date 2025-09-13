from layouts.marketing import (
    MarketingAppbarLayout,
    MarketingMobileAppbarLayout
)
from pydzn.responsive import responsive_pair
from pydzn.components import NavItem, Text, Button

def marketing_appbar(debug):
    nav_variant="simple-item"
   
    brand = (
        NavItem(
            variant=nav_variant,
            children=Text("Acme Widget Co").render(),
            )
        .center()
        .as_link("/")
        .render()
    )

    demo_btn = Button(text="Schedule a Demo", variant="solid-primary", size="lg").hx_navigate("/dashboard").render()

    mobile_html = MarketingMobileAppbarLayout(
        debug=debug,
        region_dzn={
            "brand": "flex justify-left items-center px-4",
            "demo": "flex justify-center items-center px-4"
            }
    ).render(brand=brand, demo=demo_btn)

    

    desktop_html = MarketingAppbarLayout(
        debug=debug,
        region_dzn={
            "brand": "flex justify-center items-center",
            "demo": "flex justify-center items-center px-4"
            }
    ).render(brand=brand,demo=demo_btn)

    return responsive_pair(desktop_html=desktop_html, mobile_html=mobile_html)

    #     layout_builder()
    #     .fill_height("auto", property="min-height")
    #     .columns(c0="2fr", c1="2fr", c2="1fr", c3="1fr", c4="1fr", c5="1fr", c6="3fr", c7="1fr", c8="1fr", c9="2fr")
    #     .rows(r0=APPBAR_HEIGHT)
    #     .region("spacer0", row="r0", col="c0", col_span=1)
    #     .region("brand", row="r0", col="c1", col_span=1)
    #     .region("product", row="r0", col="c2", col_span=1)
    #     .region("testimonials", row="r0", col="c3", col_span=1)
    #     .region("integrations", row="r0", col="c4", col_span=1)
    #     .region("security", row="r0", col="c5", col_span=1)
    #     .region("spacer", row="r0", col="c6", col_span=1)
    #     .region("login", row="r0", col="c7", col_span=1)
    #     .region("demo", row="r0", col="c8", col_span=1)
    #     .region("spacer1", row="r0", col="c9", col_span=1)
    #     .build(name="MarketingAppbarLayout")
    # )