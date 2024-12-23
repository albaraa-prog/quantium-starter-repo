from dash.testing.application_runners import import_app

def test_header_is_present(dash_duo):
    # Import and start the Dash app
    app = import_app("app")
    dash_duo.start_server(app)

    # Check if the header is present
    assert dash_duo.find_element("h1").text == "Pink Morsel Sales Visualizer"

def test_visualization_is_present(dash_duo):
    # Import and start the Dash app
    app = import_app("app")
    dash_duo.start_server(app)

    # Check if the visualization (graph) is present
    assert dash_duo.find_element("div#sales-chart") is not None

def test_region_picker_is_present(dash_duo):
    # Import and start the Dash app
    app = import_app("app")
    dash_duo.start_server(app)

    # Check if the region picker (radio buttons) is present
    assert dash_duo.find_element("div#region-filter") is not None
