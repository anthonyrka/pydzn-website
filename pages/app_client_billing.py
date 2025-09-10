from layouts.saas_app import WCAppMainLayout, ContentBillingLayout
from pydzn.components import Text


def app_client_billing_page(debug=False):
    """
    This the client billing page of the app
    """
    
    billing_content = ContentBillingLayout(
        debug=debug,
        region_dzn={
            "client_billing": "border-0 border-r border-slate-300 border-solid"
        }
        ).render(
            client_billing=Text(text="Client Billing").render(),
            billing_program=Text(text="Billing Program").render()
            )

    body = WCAppMainLayout(
        debug=debug,
        region_dzn={
            "left_sidebar": "border-0 border-r border-slate-300 border-solid",
            "appbar": "border-0 border-b border-slate-300 border-solid"
        }
    ).render(
        left_sidebar=Text(text="A").render(),
        appbar=Text(text="B").render(),
        content=billing_content,
    )

    return body
