from pydzn.grid_builder import layout_builder


# ----- Main App Layout ----#
# the content section accepts various layouts

LEFT_SIDEBAR_WIDTH=128 # the width of the sidebar
MAIN_SHARE="1fr" # remaining share of the space

WCAppMainLayout = (
    layout_builder()
    .fill_height("100vh", property="height") # sets up the page to restrict height to view height
    .columns(left_sidebar=LEFT_SIDEBAR_WIDTH, main="1fr") # split the main layout into two columns: sidebar and main
    .rows(header=108, content="1fr") # add 2 rows: a header section and a content section stacked 
    .region("left_sidebar", col="left_sidebar", row="header", row_span=2) # place the sidebar into the left_sidebar column in the first row and span both rows
    .region("appbar", col="main", row="header", col_span=1) # Add the appbar to the right of sidebar in the main section and span the last row
    .region("content", col="main", row="content") # declar the empty content section which is the last row in main
    .build(name="WCAppLayout")
)

# ----- Billing Page Layout ----#
ContentBillingLayout = (
    layout_builder()
    .fill_height("100%", property="height", apply_to="both") # both refers to the section and it's wrapper so that the page height is restricted to view height
    .columns(left_section="1fr", right_section="1fr")
    .rows(row1="1fr")
    .region("client_billing", col="left_section", row="row1")
    .region("billing_program", col="right_section", row="row1")
    .build(name="ContentBillingLayout")
)
