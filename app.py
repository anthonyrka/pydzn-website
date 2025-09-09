from flask import Flask, Response, render_template
# pydzn: register utilities you actually use; compile to CSS
from pydzn.dzn import register_dzn_classes, compile_used_css
from pages.app_home import app_home


app = Flask(__name__)


@app.get("/_dzn.css")
def dzn_css():
    try:
        css = compile_used_css()
        return Response(css, mimetype="text/css", headers={"Cache-Control": "no-store"})
    except Exception as e:
        # Helpful error in the browser if something goes sideways
        import traceback
        return Response(
            "/* dzn error:\n" + traceback.format_exc() + "*/",
            status=500,
            mimetype="text/plain",
        )

@app.get("/")
def home():
    # Classes we’ll use on this page (must be registered so /_dzn.css emits rules)
    # wrapper = "flex justify-center"
    # card    = "flex flex-col gap-4 p-4 rounded border shadow-md text-center w-[320px]"
    # # Register both strings (space-separated)
    # register_dzn_classes(wrapper)
    # register_dzn_classes(card)

    body = app_home()


    return render_template("base.html", body=body)


if __name__ == "__main__":
    # Optional direct run: python app.py
    app.run(debug=True)

