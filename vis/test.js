
// set up our data series with 50 random data points


//convert x to unix epoch Time

var seriesData = [ [{x:1475365030, y:2}, {x:1475365031, y:3}, {x:1475365032, y:3}, {x:1475365034, y:4}, {x:1475365037, y:3}, {x:1475365040, y:2}] ];


console.log(seriesData);

// instantiate our graph!

var graph = new Rickshaw.Graph( {
	element: document.getElementById("chart"),
	width: 960,
	height: 500,
	renderer: 'scatterplot',
	series: [
		{
			color: "#ff9030",
			data: seriesData[0],
		}//,{
		// 	color: "#4c4cff",
		// 	data: seriesData[1],
		// }
	]
} );

var xAxis = new Rickshaw.Graph.Axis.Time({
    graph: graph
});

var yAxis = new Rickshaw.Graph.Axis.Y({
    graph: graph,
    tickFormat: Rickshaw.Fixtures.Number.formatKMBT
});


graph.renderer.dotSize = 6;

new Rickshaw.Graph.HoverDetail({ graph: graph });

graph.render();
xAxis.render();
yAxis.render();
