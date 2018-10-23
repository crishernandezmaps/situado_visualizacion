// var storymap_data = 'data/catastro.json';
var storymap_data = 'data/x.json';

var storymap_options = {
   show_lines: false,
   line_follows_path: false,
   show_lines: false,
   show_history_line: false
};

var storymap = new VCO.StoryMap('mapdiv', storymap_data, storymap_options);

d3.json(storymap_data, function(error, data) {
	a = data.storymap.slides
	b = []
	for (let i of a){
		for (let j of i.text.tags){
			b.push(j)
		}
	}
	var select = d3.select('#menu')
	  .append('select')
	  	.attr('id','select')
	    .on('change',onchange)

	var options = select
	  .selectAll('option')
		.data(b).enter()
		.append('option')
			.text(function (d) { return d; })
			.attr('id',function (d) { return d; });

	// MENU
	function addID(){
		selectValue = d3.select('select').property('value')	
		d3.select('#menu')
			.attr('id',selectValue)		
	};

	function onchange() {
		selectValue = d3.select('select').property('value')
		d3.select('#menu')
			.append('p')
	};	

	// Render images //
	$(document).ready(function() {
	    $("option").click(function(event) {
	    	$("#img").empty();
	    	x = d3.select('select').property('value')
	    	for (let i of a){
	    		tags = i.text.tags
	    		if (tags.includes(x)) {	
	    			f = '"' + String(i.media.url) + '"'
	        		// $("#img").append('<img src=' + f + 'alt=' + x + '>');
	        		$("#img").append('<a href=' + f + ' ' + 'data-lightbox=' + '"' + 'invi' + '"' + ' ' + '> ' + '<img src=' + f + 'alt=' + x + '>' + '</a>' );
	    		}
			}
	    });

	    $("img").click(function(){    
	        $("img").animate({height: "300px"});
	    });
	});

});

window.onresize = function(event) {
    storymap.updateDisplay(); // this isn't automatic
}