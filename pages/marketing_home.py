from layouts.marketing import (
    MarketingHomeLayout,
    MarketingAppbarLayout,
    MarketingHeroLayout,
    MarketingFeaturesLayout,
    MarketingPartnersLayout,
    MarketingBrandsLayout,
    MarketingCertificationsLayout,
    MarketingCTALayout,
    MarketingFooterLayout,
    # ---- mobile layouts ----- #
    MarketingMobileHomeLayout
)
from components.marketing_appbar import marketing_appbar

from pydzn.components import Text
from pydzn.responsive import responsive_pair


def marketing_home_page(debug=False):
    """
    This the landing page of the app when users first log in
    """

    # ---- Desktop ---- #
    # appbar_desktop = MarketingAppbarLayout(
    #     debug=debug
    # ).render()

    hero_desktop = MarketingHeroLayout(
        debug=debug
    ).render()

    feature_desktop = MarketingFeaturesLayout(
        debug=debug
    ).render()

    partners_desktop = MarketingPartnersLayout(
        debug=debug
    ).render()
    
    brands_desktop = MarketingBrandsLayout(
        debug=debug
    ).render()
        
    certifications_desktop = MarketingCertificationsLayout(
        debug=debug
    ).render()
    
    cta_desktop = MarketingCTALayout(
        debug=debug
    ).render()

    footer_desktop = MarketingFooterLayout(
        debug=debug
    ).render()

    desktop_html = MarketingHomeLayout(
        debug=debug,
        region_dzn={
            "appbar": "sticky top-0 border-0 border-b border-slate-300 border-solid bg-[white] z-[100]" # setting sticky semantic class in order to fix appbar on mobile
        }
    ).render(
        appbar=marketing_appbar(debug),
        hero=hero_desktop,
        features=feature_desktop,
        partners=partners_desktop,
        brands=brands_desktop,
        certifications=certifications_desktop,
        cta=cta_desktop,
        footer=footer_desktop,
    )

    # ---- Mobile ---- #
    mobile_html = MarketingMobileHomeLayout(
        debug=debug,
        region_dzn={
            "appbar": "sticky top-0 border-0 border-b border-slate-300 border-solid bg-[white] z-[1000]" # setting sticky semantic class in order to fix appbar on mobile
        }

    ).render(
        appbar=marketing_appbar(debug)
    )

    return responsive_pair(desktop_html=desktop_html, mobile_html=mobile_html)
