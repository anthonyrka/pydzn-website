# from layouts.saas_app import DashboardLayout, DashboardContent3Cols
# from components.sidebar.component import Sidebar
# from components.nav_item.component import NavItem
# from components.text.component import Text
# from components.card.component import Card
from pydzn.components import Button, Text
# from components.drawer.component import Drawer


def app_home():
    # drawer_id = "drawer-panel"
    # text_elem_0 = Text(text="Controls", tag="span"); text_elem_0.set_style("color", "black")
    # text_elem_1 = Text(text="Hello world!", tag="span", **{"data-count": "0"}); text_elem_1.set_style("color", "black")

    # button_elem_0 = Button(
    #     text="Open Drawer",
    #     tag="button",
    #     dzn="px-5 py-2 rounded-sm border-2 border-blue-500 shadow-sm hover:shadow-md bg-[transparent] text-[#2563eb]",
    #     **{
    #         "class": "btn",
    #         "type": "button",
    #         "hx-on:click": (
    #             f"var d=document.getElementById('{drawer_id}');"
    #             "var hidden=d.classList.toggle('hidden');"
    #             "this.textContent = hidden ? 'Open Drawer' : 'Close Drawer';"
    #             "this.setAttribute('aria-expanded', (!hidden).toString());"
    #         ),
    #     },
    # )

    # button_elem_1 = Button(
    #     text="Click me",
    #     tag="button",
    #     dzn="px-5 py-2 rounded-sm border-2 border-blue-500 shadow-sm hover:shadow-md bg-[transparent] text-[#2563eb]",
    #     **{
    #         "class": "btn",
    #         "type": "button",
    #         "hx-on:click": (
    #             f"var t=document.getElementById('{text_elem_1.id}');"
    #             "var n=parseInt(t.dataset.count||'0',10)+1;"
    #             "t.dataset.count=n;"
    #             "t.textContent='Click ' + n;"
    #         ),
    #     },
    # )

    # card_elem_0 = Card(
    #     children=text_elem_0.render() + button_elem_0.render(),
    #     dzn="flex flex-col gap-8 p-8 rounded-xl border shadow-lg hover:shadow-xl focus:shadow-xl w-[100px] text-center",
    #     **{"class": "card"}
    # )

    # card_elem_1 = Card(
    #     children=text_elem_1.render() + button_elem_1.render(),
    #     dzn="flex flex-col gap-8 p-8 rounded-xl border shadow-lg hover:shadow-xl focus:shadow-xl w-[100px] text-center",
    #     **{"class": "card"}
    # )

    # drawer_elem = Drawer(
    #     id=drawer_id,
    #     children=card_elem_1.render(),
    #     dzn=(
    #         "fixed top-0 right-0 "                 # ⬅️ anchor to the left, not right
    #         "h-[100vh] w-[50vw] overflow-y-auto "
    #         "bg-elevated border-r border-subtle " # ⬅️ divider on the right edge
    #         "shadow-[4px_0_16px_rgba(0,0,0,.12)] " # ⬅️ shadow cast to the right
    #         "hidden"
    #     ),
    #     **{"class": "drawer"}
    # )


    # # Sidebar
    # item = (
    #     "w-[100%] h-[64px] flex items-center justify-center text-center "
    #     "rounded-none border-solid border-b border-subtle border-t-0 border-l-0 border-r-0"
    # )
    # sidebar_html = Sidebar(
    #     children=(
    #         NavItem(children=Text(text='Overview', tag='span').render(), dzn=item).render() +
    #         NavItem(children=Text(text='Activity', tag='span').render(), dzn=item).render() +
    #         NavItem(children=Text(text='Reports',  tag='span').render(), dzn=item).render() +
    #         NavItem(children=Text(text='Settings', tag='span').render(), dzn=item + " border-b-0").render()
    #     ),
    #     dzn="flex flex-col"
    # ).render()

    # # Duplicate the CARD into each content column (avoid duplicating the Drawer id)
    # card_only_html = card_elem_0.render()

    # content_grid = DashboardContent3Cols(
    #     region_dzn={"col1": "p-2", "col2": "p-2", "col3": "p-2"},
    #     debug=True,
    # ).render(
    #     col1=Text(text="D.1").render(),
    #     col2=Text(text="D.2").render(),
    #     col3=Text(text="D.3").render(),
    # )

    # # Add the drawer once (still inside the content area)
    # content_html = content_grid + drawer_elem.render()

    # hero_html = Text(text="Hero area", tag="span").render()

    # layout = DashboardLayout(
    #     region_dzn={"sidebar": "bg-elevated p-4", "hero": "p-4", "subhero": "p-4", "dsubhero": "p-4", "content": "p-4"},
    #     debug=True,
    # )

        # button_elem_0 = Button(
    #     text="Open Drawer",
    #     tag="button",
    #     dzn="px-5 py-2 rounded-sm border-2 border-blue-500 shadow-sm hover:shadow-md bg-[transparent] text-[#2563eb]",
    #     **{
    #         "class": "btn",
    #         "type": "button",
    #         "hx-on:click": (
    #             f"var d=document.getElementById('{drawer_id}');"
    #             "var hidden=d.classList.toggle('hidden');"
    #             "this.textContent = hidden ? 'Open Drawer' : 'Close Drawer';"
    #             "this.setAttribute('aria-expanded', (!hidden).toString());"
    #         ),
    #     },
    # )

    # return layout.render(
    #     sidebar=Text(text="A").render(),
    #     hero=Text(text="B").render(),
    #     subhero=Text(text="C").render(),
    #     content=content_grid
    # )
    return None