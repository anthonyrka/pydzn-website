from pydzn.grid_builder import layout_builder
from pydzn.components import Text, Button, Table
from pydzn.responsive import responsive_pair


DashboardLayout = (
    layout_builder()
    .fill_height("auto", property="height")
    .columns(c0="1fr", c1="1fr", c2="1fr", c3="1fr")
    .rows(r0="1fr", r1="3fr")
    .region("tasks", row="r0", col="c0", col_span=1)
    .region("quotes", row="r0", col="c1", col_span=1)
    .region("opportunity", row="r0", col="c2", col_span=1)
    .region("revenue", row="r0", col="c3", col_span=1)
    .region("tabular", row="r1", col="c0", col_span="all")
    .build(name="DashboardLayout")
)

DashboardMobileLayout = (
    layout_builder()
    .fill_height("auto", property="height")
    .columns(c0="1fr")
    .rows(r0="1fr", r1="1fr", r2="1fr", r3="1fr", r4="3fr")
    .region("tasks", row="r0", col="c0")
    .region("quotes", row="r1", col="c0")
    .region("opportunity", row="r2", col="c0")
    .region("revenue", row="r3", col="c0")
    .region("tabular", row="r4", col="c0")
    .build(name="DashboardMobileLayout")
)


MetricCardLayout = (
    layout_builder()
    .fill_height("auto", property="height")
    .columns(c0="1fr")
    .rows(r0="40px", r1="40px", r2="60px")
    .region("title", row="r0", col="c0", col_span=1)
    .region("metric", row="r1", col="c0", col_span=1)
    .region("actions", row="r2", col="c0", col_span=1)
    .build(name="MetricCardLayout")
)

cols = [
    {"key": "id", "label": "ID", "sortable": True, "width": "80px", "align": "right"},
    {"key": "name", "label": "Name", "sortable": True},
    {"key": "status", "label": "Status", "sortable": True, "align": "center"},
]

rows = [
    {"id": "1", "name": "Widget A", "status": "<span class='text-[green]'>OK</span>"},
    {"id": "2", "name": "Widget B", "status": "<span class='text-[red]'>Fail</span>"},
    {"id": "3", "name": "Widget C", "status": "<span class='text-[red]'>Fail</span>"},
    {"id": "4", "name": "Widget D", "status": "<span class='text-[green]'>OK</span>"},
]

table = Table(
    columns=cols,
    rows=rows,
    sort_url="/tables/inventory",     # your endpoint should re-render this Table with new sort
    sort_key="name",
    sort_dir="asc",
    export_url="/tables/inventory/export.csv",  # plain navigation for file download
    add_column_url="/tables/inventory/add-col", # returns updated Table HTML
    show_toolbar=True,
    striped=True,
    variant="surface",  # "minimal" | "soft" | "outlined"
    size="lg",          # "sm" | "md" | "lg"
    tone="primary",     # "primary" | "danger" | "success"
)

table_html = table.render()


def dashboard(debug):
    task_actions = (
        Button(text="Late", variant="acme:danger-outline", size="sm", dzn="m-[4px]").render() +
        Button(text="Shipping", variant="acme:danger-outline", size="sm", dzn="m-[4px]").render()
    )

    tasks = MetricCardLayout(
        debug=debug,
        region_dzn={
            "title": "flex items-center px-4",
            "metric": "flex items-start py-[0] px-4 text-[red]",
            "actions": "px-4 m-0"
            
        }
        ).render(
            title=Text(tag="h4", text="TASKS").render(),
            metric=Text(tag="h3", text="44", dzn="m-0 ml-[4px]").render(),
            actions=task_actions
        )

    quotes_actions = (
        Button(text="Incomplete records", variant="acme:warning-outline", size="sm", dzn="m-[4px]").render() 
        )

    quotes = MetricCardLayout(
        debug=debug,
        region_dzn={
            "title": "flex items-center px-4",
            "metric": "flex items-start py-[0] px-4 text-[rgb(245,158,11)]",
            "actions": "px-2 m-0 ml-[4px]"
            
        }
        ).render(
            title=Text(tag="h4", text="QUOTES").render(),
            metric=Text(tag="h3", text="73", dzn="m-0 ml-[4px]").render(),
            actions=quotes_actions
        )

    opportunity_actions = (
        Button(text="Accounts receivable", variant="acme:neutral-outline", size="sm", dzn="m-[4px]").render() 
        )

    opportunity = MetricCardLayout(
        debug=debug,
        region_dzn={
            "title": "flex items-center px-4",
            "metric": "flex items-start py-[0] px-4 text-[black]",
            "actions": "px-2 m-0 ml-[4px]"
            
        }
        ).render(
            title=Text(tag="h4", text="OPPORTUNITY").render(),
            metric=Text(tag="h3", text="$4,909,544.32", dzn="m-0 ml-[4px]").render(),
            actions=opportunity_actions
        )

    revenue_actions = (
        Button(text="Collections management", variant="acme:neutral-outline", size="sm", dzn="m-[4px]").render() 
        )

    revenue = MetricCardLayout(
        debug=debug,
        region_dzn={
            "title": "flex items-center px-4",
            "metric": "flex items-start py-[0] px-4 text-[black]",
            "actions": "px-2 m-0 ml-[4px]"
            
        }
        ).render(
            title=Text(tag="h4", text="REVENUE").render(),
            metric=Text(tag="h3", text="$55,077,230.88", dzn="m-0 ml-[4px]").render(),
            actions=revenue_actions
        )

    desktop_html = DashboardLayout(
        debug=debug,
        region_dzn={
            "tasks": "p-4 ml-[18px] mt-[24px] mr-[8px] rounded-sm border border-[1px] border-gray-100",
            "quotes": "p-4 ml-[4px] mt-[24px] mr-[8px] rounded-sm border border-[1px] border-gray-100",
            "opportunity": "p-4 ml-[4px] mt-[24px] mr-[8px] rounded-sm border border-[1px] border-gray-100",
            "revenue": "p-4 ml-[4px] mt-[24px] mr-[18px] rounded-sm border border-[1px] border-gray-100",
            "tabular": "p-4"
        }).render(
        tasks=tasks,
        quotes=quotes,
        opportunity=opportunity,
        revenue=revenue,
        tabular=table_html
    )

    mobile_html = DashboardMobileLayout(
        debug=debug,
        region_dzn={
            "tasks": "p-4 m-[24px] rounded-sm border border-[1px] border-gray-100",
            "quotes": "p-4 m-[24px] rounded-sm border border-[1px] border-gray-100",
            "opportunity": "p-4 m-[24px] rounded-sm border border-[1px] border-gray-100",
            "revenue": "p-4 m-[24px] rounded-sm border border-[1px] border-gray-100",
        }).render(
        tasks=tasks,
        quotes=quotes,
        opportunity=opportunity,
        revenue=revenue
    )

    return responsive_pair(desktop_html=desktop_html, mobile_html=mobile_html)
