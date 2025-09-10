from layouts.marketing import MarketingHomeLayout
from pydzn.components import Text


def marketing_home_page(debug=False):
    """
    This the landing page of the app when users first log in
    """
    
    return MarketingHomeLayout(
        debug=debug,
        region_dzn={
            "hero": "border-0 border-r border-slate-300 border-solid",        }
    ).render(
        hero=Text(text="A").render(),
        subheader=Text(text="B").render(),
        main_left=Text(text="C.1").render(),
        main_center=Text(text="C.2").render(),
        main_right=Text(text="C.3").render(),
        prices=Text(text="D").render(),
        footer=Text(text="E").render(),
    )
