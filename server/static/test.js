
//convert x times to unix epoch Time
// instantiate our graph!

var graph = new Rickshaw.Graph( {
	element: document.getElementById("chart"),
	width: 960,
	height: 500,
	renderer: 'scatterplot',
	series: [
		{
			color: "#4c4cff",
			data: [{x:1475365030, y:2}, {x:1475365031, y:3}, {x:1475365032, y:3}, {x:1475365034, y:4}, {x:1475365037, y:3}, {x:1475365040, y:2}],
      name: "Syringes"
		}
	]
} );

var xAxis = new Rickshaw.Graph.Axis.Time({
    graph: graph
});


var yAxis = new Rickshaw.Graph.Axis.Y({
    graph: graph
});

graph.renderer.dotSize = 6;
graph.render();

var hoverDetail = new Rickshaw.Graph.HoverDetail( {
	graph: graph,
	formatter: function(series, x, y) {
		var date = '<span class="date">' + new Date(x * 1000).toUTCString() + '</span>';
		var swatch = '<span class="detail_swatch" style="background-color: ' + series.color + '"></span>';
		var content = swatch + series.name + ": " + parseInt(y) + '<br>' + date;
		return content;
	}
} );
