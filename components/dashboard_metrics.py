from pydzn.components import Card, Text, Button
from layouts.saas_app import AppDashboardMobileLayout, AppDashboardLayout
from pydzn.responsive import responsive_pair # combines layouts and allows client to choose, as an example, between mobile or desktop 


def dashboard(debug=False):
    sub_txt = Text(
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam gravida mattis ex sit amet elementum. "
        "Donec tincidunt nunc ac diam ullamcorper, euismod gravida est pretium. Sed tincidunt, nisl at sollicitudin "
        "dictum, urna mauris maximus mi, vitae blandit ipsum neque eu velit.",
        dzn="text-center p-4"
    )
    v1_txt = Text("Built-in Card Variant: plain", tag="h2", dzn="text-center")
    v1_btn = Button(text="Save", dzn="w-[fit-content] self-center", variant="acme:glass", size="xl")
    v1_card = Card(tag="div", variant="plain", children=v1_txt.render() + sub_txt.render() + v1_btn.render()).render()

    mobile_html = AppDashboardMobileLayout(
        debug=debug,
        region_dzn={"orders":"p-4","tasks":"p-4","customers":"p-4"}
    ).render(orders=v1_card, tasks=v1_card, customers=v1_card)

    desktop_html = AppDashboardLayout(
        debug=debug,
        region_dzn={"orders":"p-4","tasks":"p-4","customers":"p-4"}
    ).render(orders=v1_card, tasks=v1_card, customers=v1_card)

    return responsive_pair(desktop_html=desktop_html, mobile_html=mobile_html)
