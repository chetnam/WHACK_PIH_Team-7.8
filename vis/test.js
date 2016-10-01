


var graph = new Rickshaw.Graph( {
	element: document.querySelector("#chart"),
	renderer: 'scatterplot',
	stroke: true,
	series: [{
		data: [ { x: 0, y: 40 },
            { x: 1, y: 49 },
            { x: 2, y: 50 },
            { x: 3, y: 60 },
            { x: 4, y: 50 },
            { x: 5, y: 80 } ] ,
		color: 'steelblue'
	}]
} );

graph.render();
