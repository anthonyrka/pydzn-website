from pydzn.components import Card, Text, Button
from layouts.app import AppDashboardMobileLayout, AppDashboardLayout
from pydzn.responsive import responsive_pair # combines layouts and allows client to choose, as an example, between mobile or desktop 


def dashboard(debug=False):
    orders_card = Card(
        tag="div",
        variant="plain",
        children=(
            Text("Built-in Card Variant: plain", tag="h2", dzn="text-center").render() +
            Text("Orders metrics", dzn="text-center p-4").render() +
            Button(text="Save", dzn="w-[fit-content] self-center", variant="acme:glass", size="xl").render()
        )
    ).render()

    tasks_card = Card(
        tag="div",
        variant="plain",
        children=(
            Text("Built-in Card Variant: plain", tag="h2", dzn="text-center").render() +
            Text("Taks metrics", dzn="text-center p-4").render() +
            Button(text="Save", dzn="w-[fit-content] self-center", variant="acme:glass", size="xl").render()
        )
    ).render()

    customers_card = Card(
        tag="div",
        variant="plain",
        children=(
            Text("Built-in Card Variant: plain", tag="h2", dzn="text-center").render() +
            Text("Customers metrics", dzn="text-center p-4").render() +
            Button(text="Save", dzn="w-[fit-content] self-center", variant="acme:glass", size="xl").render()
        )
    ).render()

    mobile_html = AppDashboardMobileLayout(
        debug=debug,
        region_dzn={"orders":"p-4","tasks":"p-4","customers":"p-4"}
    ).render(orders=orders_card, tasks=tasks_card, customers=customers_card)

    desktop_html = AppDashboardLayout(
        debug=debug,
        region_dzn={"orders":"p-4","tasks":"p-4","customers":"p-4"}
    ).render(orders=orders_card, tasks=tasks_card, customers=customers_card)

    return responsive_pair(desktop_html=desktop_html, mobile_html=mobile_html)
