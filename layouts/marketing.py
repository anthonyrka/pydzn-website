from pydzn.grid_builder import layout_builder


# ----- Marketing Page Layout ----#
MarketingHomeLayout = (
    layout_builder()
    .fill_height("100vh", property="min-height") # min-height lets content exceed viewport
    .columns(col1="1fr", col2="1fr", col3="1fr")
    .rows(
        header=480,
        sub_header=240,
        main=600,
        prices=480,
        footer=360
    )
    .region("hero",       col="col1", row="header",     col_span="all")
    .region("subheader",  col="col1", row="sub_header", col_span="all")
    .region("main_left",   col="col1", row="main")
    .region("main_center", col="col2", row="main")
    .region("main_right",  col="col3", row="main")
    .region("prices",     col="col1", row="prices",     col_span="all")
    .region("footer",     col="col1", row="footer",     col_span="all")
    .build(name="MarketingHomeLayout")
)
