import marimo

__generated_with = "0.14.5"
app = marimo.App(width="medium")


@app.cell
def _():
    import amazing_project as ap
    import importlib
    importlib.reload(ap)

    ap.hello_world()
    return (ap,)


@app.cell
def _(ap):
    ap.shout("hi")
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
