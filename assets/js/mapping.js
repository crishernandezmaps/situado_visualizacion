    let options = {
      show_lines: true,
      line_follows_path: false,
      show_lines: false,
      show_history_line: false
    };

    let storymap_data = '../data/x.json';

    let storymap = new VCO.StoryMap('mapdiv', storymap_data, options);
    window.onresize = function(event) {
      storymap.updateDisplay();
    }

    // PARSING FOTOS FROM GITHUB //
    d3.json(storymap_data, function(error, imgs) {

      // ARRAY OF OBJECTS CONTAINING ALL THE DATA //
      const z = imgs.storymap.slides 

      // IMAGES URL //
      let images = []
      for (i = 0; i < z.length; i++) { 
        images.push(z[i].media.url)
      }

      // TAGS //
      let t = []
      for (i = 0; i < z.length; i++) { 
        t.push(z[i].text.tags)
      }    

      // CREATING A SINGLE ARRAY OF SORTED TAGS FREQUENCIES //
      const m = [].concat.apply([], t)
      let freq = _.countBy(m)

      let sortable = [];
      for (let x in freq) {
          sortable.push([x, freq[x]]);
      }

      let r = sortable.sort(function(a, b) {
          return b[1] - a[1];
      });

      // CREATING MENU DINAMICALLY USING SORTED TAGS //
      let select = d3.select('#menu')
        .append('select')
          .attr('class','select')
          .on('change',onchange)

      let options = select
        .selectAll('option')
        .data(r).enter()
        .append('option')
          .text(function (d) { return d.toString().split(',')[0]; })
          .attr('id',function (d) { return d.toString().split(',')[0]; });

      function onchange() {
        selectValue = d3.select('select').property('value')
        d3.select('body')
          .append('p')
          .text(selectValue)
      };            


      // APPENDING FOTOS //
      let fotos = images.forEach(function(img) {
        console.log(img.toString().split('/').slice(-1)[0].split('.')[0])
        d3.select("#gallery")
          // .append('a') // clickable image a
          // .attr('href',img) // clicable image b
          .append('img')
          .attr({
            height: 66,
            src: img
          })
          .attr('id','foto');         
      });

      // CAPTURING CLICK ON FOTO //
      var el = document.getElementById('foto');
      el.onclick = function() {
        let code = (el.src).toString().split('/').slice(-1)[0].split('.')[0]
        console.log(code);
      };      
    

    });   
