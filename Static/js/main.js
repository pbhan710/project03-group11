function init(){
    d3v7.json('/api/top10actors').then(function(data) {
        for (let i = 0; i < data.length; i++) {
            
            let actor = data[i];
            console.log(`${i}: ${actor}`)
            let actor_thumbnail_col = d3.select("#Actors").select(".container").select(".row").append("div").attr("class", "column");
            let actor_thumbnail_img = actor_thumbnail_col.append("img").attr("class", "demo cursor").attr("src", `https://image.tmdb.org/t/p/w185${actor[3]}`).attr("style", "width:50%").attr("onclick", `currentSlide(${i+1})`).attr("alt", actor[1]);

            let actor_slide = d3.select("#Actors").select(".row").select(".column").append("div").attr("class", "mySlides");
            let actor_slide_num = actor_slide.append("div").attr("class", "numbertext").text(`${i+1} / 10`);
            let actor_slide_img = actor_slide.append("img").attr("src", `https://image.tmdb.org/t/p/w185${actor[3]}`).attr("style", "width:100%");
        };
    });
}


// function upd_timeline(){

// }
// d3v7select("#my_button").on("click", upd_timeline);

init();