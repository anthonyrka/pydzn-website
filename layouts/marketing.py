from pydzn.grid_builder import layout_builder


APPBAR_HEIGHT=60
APPBAR_HEIGHT_MOBILE=APPBAR_HEIGHT
HERO_HEIGHT=600
FEATURES_HEIGHT=500
PARTNERS_HEIGHT=200
BRANDS_HEIGHT=400
CERTIFICATIONS_HEIGHT=600
CTA_HEIGHT=400
FOOTER_HEIGHT=500

BRAND_WIDTH=264

# ---- Desktop Layouts ----- #
MarketingHomeLayout = (
    layout_builder()
    .fill_height("100vh", property="min-height")
    .columns(c0="1fr")
    .rows(r0=APPBAR_HEIGHT, r1=HERO_HEIGHT, r2=FEATURES_HEIGHT, r3=PARTNERS_HEIGHT,
        r4=BRANDS_HEIGHT, r5=CERTIFICATIONS_HEIGHT, r6=CTA_HEIGHT, r7=FOOTER_HEIGHT)
    .region("appbar", row="r0", col="c0", col_span="all")
    .region("hero", row="r1", col="c0", col_span="all")
    .region("features", row="r2", col="c0", col_span="all")
    .region("partners", row="r3", col="c0", col_span="all")
    .region("brands", row="r4", col="c0", col_span="all")
    .region("certifications", row="r5", col="c0", col_span="all")
    .region("cta", row="r6", col="c0", col_span="all")
    .region("footer", row="r7", col="c0", col_span="all")
    .build(name="MarketingHomeLayout")
)

MarketingAppbarLayout = (
    layout_builder()
    .fill_height("auto", property="min-height")
    .columns(c0="2fr", c1="2fr", c2="1fr", c3="1fr", c4="1fr", c5="1fr", c6="3fr", c7="1fr", c8="2fr", c9="1fr")
    .rows(r0=APPBAR_HEIGHT)
    .region("spacer0", row="r0", col="c0", col_span=1)
    .region("brand", row="r0", col="c1", col_span=1)
    .region("product", row="r0", col="c2", col_span=1)
    .region("testimonials", row="r0", col="c3", col_span=1)
    .region("integrations", row="r0", col="c4", col_span=1)
    .region("security", row="r0", col="c5", col_span=1)
    .region("spacer", row="r0", col="c6", col_span=1)
    .region("login", row="r0", col="c7", col_span=1)
    .region("demo", row="r0", col="c8", col_span=1)
    .region("spacer1", row="r0", col="c9", col_span=1)
    .build(name="MarketingAppbarLayout")
)

MarketingHeroLayout = (
    layout_builder()
    .fill_height("auto")
    .columns(c0="1fr", c1="1fr")
    .rows(r0=HERO_HEIGHT)
    .region("info-cta-box", row="r0", col="c0", col_span=1)
    .region("info-img-box", row="r0", col="c1", col_span=1)
    .build(name="MarketingHeroLayout")
)

MarketingFeaturesLayout = (
    layout_builder()
    .fill_height("auto")
    .columns(c0="1fr", c1="1fr", c2="1fr")
    .rows(r0=100, r1=FEATURES_HEIGHT-100)
    .region("title", row="r0", col="c1", col_span=1)
    .region("card0", row="r1", col="c0", col_span=1)
    .region("card1", row="r1", col="c1", col_span=1)
    .region("card2", row="r1", col="c2", col_span=1)
    .build(name="MarketingFeaturesLayout")
)

MarketingPartnersLayout = (
    layout_builder()
    .fill_height("auto")
    .columns(c0="1fr", c1="1fr", c2="1fr", c3="1fr", c4="1fr", c5="1fr", c6="1fr")
    .rows(r0=round(PARTNERS_HEIGHT/2), r1=round(PARTNERS_HEIGHT/2))
    .region("title", row="r0", col="c2", col_span=3)
    .region("spacer0", row="r1", col="c0", col_span=1)
    .region("partner0", row="r1", col="c1", col_span=1)
    .region("partner1", row="r1", col="c2", col_span=1)
    .region("partner2", row="r1", col="c3", col_span=1)
    .region("partner3", row="r1", col="c4", col_span=1)
    .region("partner4", row="r1", col="c5", col_span=1)
    .region("spacer1", row="r1", col="c6", col_span=1)
    .build(name="MarketingPartnersLayout")
)

MarketingBrandsLayout = (
    layout_builder()
    .fill_height("auto")
    .columns(c0="2fr", c1="1fr", c2="1fr", c3="1fr", c4="1fr", c5="1fr", c6="2fr")
    .rows(r0=round(BRANDS_HEIGHT/2), r1=round(BRANDS_HEIGHT/2))
    .region("title", row="r0", col="c2", col_span=3)
    .region("spacer0", row="r1", col="c0", col_span=1)
    .region("brand0", row="r1", col="c1", col_span=1)
    .region("brand1", row="r1", col="c2", col_span=1)
    .region("brand2", row="r1", col="c3", col_span=1)
    .region("brand3", row="r1", col="c4", col_span=1)
    .region("brand4", row="r1", col="c5", col_span=1)
    .region("spacer1", row="r1", col="c6", col_span=1)
    .build(name="MarketingBrandsLayout")
)

MarketingCertificationsLayout = (
    layout_builder()
    .fill_height("auto")
    .columns(c0="1fr", c1="1fr", c2="1fr", c3="1fr", c4="1fr", c5="1fr")
    .rows(r0=round(CERTIFICATIONS_HEIGHT*.4), r1=round(CERTIFICATIONS_HEIGHT*.6))
    .region("title", row="r0", col="c2", col_span=2)
    .region("spacer0", row="r1", col="c0", col_span=2)
    .region("card0", row="r1", col="c1", col_span=2)
    .region("card1", row="r1", col="c3", col_span=2)
    .region("spacer1", row="r1", col="c4", col_span=2)
    .build(name="MarketingCertificationsLayout")
)

MarketingCTALayout = (
    layout_builder()
    .fill_height("auto")
    .columns(c0="1fr", c1="3fr", c2="1fr")
    .rows(r0=CTA_HEIGHT)
    .region("spacer0", row="r0", col="c0", col_span=1)
    .region("card", row="r0", col="c1", col_span=1)
    .region("spacer1", row="r0", col="c2", col_span=1)
    .build(name="MarketingCTALayout")
)

MarketingFooterLayout = (
    layout_builder()
    .fill_height("auto")
    .columns(c0="1fr", c1="3fr", c2="1fr")
    .rows(r0=FOOTER_HEIGHT-100, r1=100)
    .region("footer-brand", row="r0", col="c0", col_span="all")
    .region("footer-copyright", row="r1", col="c0", col_span="all")
    .build(name="MarketingFooterLayout")
)

# ---- Mobile Layouts ----- #

MarketingMobileHomeLayout = (
    layout_builder()
    .fill_height("100vh", property="height")
    .columns(c0="1fr")
    .rows(r0=APPBAR_HEIGHT, r1=HERO_HEIGHT, r2=FEATURES_HEIGHT, 
    r3=PARTNERS_HEIGHT, r4=BRANDS_HEIGHT, r5=CERTIFICATIONS_HEIGHT, r6=CTA_HEIGHT, r7=FOOTER_HEIGHT)
    .region("appbar",  col="c0", row="r0")
    .region("hero", col="c0", row="r1")
    .region("features", col="c0", row="r2")
    .region("partners", col="c0", row="r3")
    .region("brands", col="c0", row="r4")
    .region("certificates", col="c0", row="r5")
    .region("cta", col="c0", row="r6")
    .region("footer", col="c0", row="r7")
    .build(name="MarketingMobileHomeLayout")
)

# ----- App header mobile menu layout ----#
MarketingMobileAppbarLayout = (
    layout_builder()
    .fill_height("100%", property="height", apply_to="both")
    .columns(c0="2fr", c1="1fr", c2="1fr")
    .rows(r0=f"minmax({APPBAR_HEIGHT_MOBILE}px, auto)") # this container holds the app header for mobile layout so height must match
    .region("brand", col="c0", row="r0")
    .region("demo", col="c1", row="r0", col_span=2)
    .build(name="MarketingMobileAppbarLayout")
)