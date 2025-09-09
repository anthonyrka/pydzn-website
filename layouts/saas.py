from pydzn.grid_builder import layout_builder


# ----- Outer layout -----
DashboardLayout = (
    layout_builder()
      .columns(sidebar=180, main="1fr")
      .rows(hero="100px", subhero="100px", dsubhero="60px", content="1fr")
      .region("sidebar",  col="sidebar", row=None, row_span=None)
      .region("hero",     col="main",    row="hero")
      .region("subhero",  col="main",    row="subhero")
      .region("dsubhero",  col="main",    row="dsubhero")
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
