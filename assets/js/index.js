// Repo: https://github.com/crishernandezmaps/situado_demo
catastroVarasMena = 'img-out/catastroVarasMena.json'
terrenoVarasMena = 'img-out/terrenoVarasMena.json'
terrenoVillaLaReina = 'img-out/terrenoVillaLaReina.json'

function updateChart(sourcefile) {
	d3.json(sourcefile, function(error, data) {
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

		// MENU //
		function addID(){
			selectValue = d3.select('select').property('value')	
			d3.select('#menu')
				.attr('id',selectValue)		
		};

		function onchange() {
			$("value").remove();
			selectValue = d3.select('select').property('value')
			d3.select('#menu')
				.append('p');
			
			let PagesEle = document.getElementById("imagenes");
			let arr = [];	
			$("#imagenes").empty();
			for (let i of a){
				const tags = i.text.tags;
				if (tags.includes(selectValue)) {
					f = i.media.url;
					let element = document.createElement("img");
					element.src = f;
					arr[i] = element.src;
					PagesEle.appendChild(element);
				}
			}
		};	

		// To create points
		points = []
		for (let i of a){
			plon = i.location.lon
			plat = i.location.lat
			f = '"' + String(i.media.url) + '"'
			pt = [plon,plat,'<img src=' + f + ' >']
			points.push(pt)
		}

		centering = [points[0][1],points[0][0]]

		///// MAPA LEAFLET /////
		// Map //
		var m = L.map('map').setView(centering, 15); 
		const tk = 'pk.eyJ1IjoiY3Jpc2htaWxsIiwiYSI6ImNqb3owNDRhdDAwZHQzeHFxaHVtejBrN3kifQ.Ic3TJ8UroP7NB3T9M5DWZg'

		// Basemaps //
		var black = L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
			attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
			maxZoom: 18,
			id: 'mapbox.dark',
			accessToken: tk
		}).addTo(m);	

		//Loop through the markers array //
		for (var i=0; i<points.length; i++) {
		   var lon = points[i][0];
		   var lat = points[i][1];
		   var popupText = points[i][2];
		    var markerLocation = new L.LatLng(lat, lon);
		    var marker = new L.Marker(markerLocation);
		    m.addLayer(marker);
		    marker.bindPopup(popupText);
		} 

		// Adding Posts //
		var iconPost = L.icon({
		    iconUrl: 'images/post_icon.png',
		    iconSize:     [38, 38], // size of the icon
		    shadowSize:   [50, 64], // size of the shadow
		    iconAnchor:   [22, 94], // point of the icon which will correspond to marker's location
		    shadowAnchor: [4, 62],  // the same for the shadow
		    popupAnchor:  [-3, -76] // point from which the popup should open relative to the iconAnchor
		});


		var posts = [
			['Post: Varas Mena',-33.512222,-70.633889],
			['Post: Villa La Reina',-33.452187,-70.539026],
			['Post: institucional',-33.452217,-70.558866],
			['Post: Catastro Varas Mena',-33.513037,-70.626454],
			['Post: New Map',-33.450808,-70.53188899999998],
			['Post: New Map',-33.45210076654909,-70.53637204239737],
			['Post: Valle de Azapa',-33.407505,-70.735732],
			['Post: Centros Culturales',-33.476797,-70.645698]
		]

		for (var i = 0; i < posts.length; i++) {
			marker = new L.marker([posts[i][1],posts[i][2]],{icon: iconPost})
				.bindPopup(posts[i][0])
				.addTo(m);
		}		

})}//Cierre updateChart//

updateChart(terrenoVarasMena);

$( "#terrenovaras" ).click(function() {
	$("#menu").empty();
  	updateChart(terrenoVarasMena);
});

$( "#catastrovaras" ).click(function() {
	$("#menu").empty();
  	updateChart(catastroVarasMena);
});

$( "#terrenoLaReina" ).click(function() {
	$("#menu").empty();
  	updateChart(terrenoVillaLaReina);
});