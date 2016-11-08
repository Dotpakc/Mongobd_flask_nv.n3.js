/**
 * Created by dpack on 07.11.16.
 */
var base = [{
    values: []
}];

// get json
d3.json('/get-cities', function (error, data) {
    if (error) return console.warn(error);
    var items = data.map(function (item) {
        return base[0].values.push({"label": item.label, "value": item.value});
    });
});


//graph
nv.addGraph(function() {
        var chart = nv.models.discreteBarChart()
            .x(function(d) { return d.label })
            .y(function(d) { return d.value })
            .staggerLabels(true)
            .showValues(true)
            .duration(100)
            ;
        d3.select('#chart1 svg')
            .datum(base)
            .call(chart);
        nv.utils.windowResize(chart.update);
        return chart;
    });
