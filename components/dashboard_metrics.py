from layouts.saas_app import AppDashboardLayout
from pydzn.components import Card, Text, Button


def dashboard(debug=False):

    sub_txt = Text(
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam gravida mattis ex sit amet elementum. Donec tincidunt nunc ac diam ullamcorper, euismod gravida est pretium. Sed tincidunt, nisl at sollicitudin dictum, urna mauris maximus mi, vitae blandit ipsum neque eu velit. Pellentesque sagittis commodo vehicula. Nunc aliquam metus non augue viverra sollicitudin. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Sed id sem a nisl tincidunt sodales.",
        dzn="text-center p-4")
    v1_txt = Text("Built-in Card Variant: plain", tag="h2", dzn="text-center")
    v1_btn = Button(
        text="Save",
        dzn="w-[fit-content] self-center",
        # variant="acme:glass", # custom variant
        variant="acme:glass", # built-in variant
        size="xl"
    )
    v1_card = Card(tag="div", variant="plain", children=v1_txt.render() + sub_txt.render() + v1_btn.render()).render()

    return AppDashboardLayout(
        debug=debug,
        region_dzn= {
            "orders": "p-4",
            "tasks": "p-4",
            "customers": "p-4"
            }
    ).render(
        orders=v1_card,
        tasks=v1_card,
        customers=v1_card
    )
    
