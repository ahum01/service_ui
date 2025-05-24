from dash_extensions import WebSocket
from dash_extensions.enrich import DashProxy, Input, Output, dcc, html

# Client-side function (for performance) that updates the graph.
update_graph = """function(msg) {
    if(!msg){return {};}  // no data, just return
    const data = JSON.parse(msg.data);  // read the data
    console.log(data); 
    console.log(typeof(data));
    const data_rt = [];
    //data_rt[0]  = data[0]["discount_factors"];
    //data_rt[1]  = data[1]["discount_factors"];
    //data_rt[2]  = data[2]["discount_factors"];
    //data_rt[3]  = data[3]["discount_factors"];
    //data_rt[4]  = data[4]["discount_factors"];
    //data_rt[5]  = data[5]["discount_factors"];
    var arr_length = data.length; 
    for(var i = 0; i < arr_length; i++)
    {
        data_rt[i] = data[i]["discount_factors"];
    }

    return {data: [{y: data_rt, type: "scatter"}]}};  // plot the data
"""
# Create small example app.
app = DashProxy(__name__)
app.layout = html.Div(
    [
        html.H1(children='SONIA Curve Construction', style={'textAlign': 'center'}, id='label_id'),
        WebSocket(id="ws", url="ws://127.0.0.1:8000/ws"), dcc.Graph(id="graph")]
)
app.clientside_callback(update_graph,
                        Output("graph", "figure"),
                        Input("ws", "message"))

if __name__ == "__main__":
    app.run()