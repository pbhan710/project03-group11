function init(){
    d3v7.json('/api/top10actors').then(function(data) {
        let firstActor = data[0];
        let firstActorID = firstActor[0];
    
        d3v7.json(`/api/actorsmovies/${firstActorID}`).then(function(data) {
            let movie_lst = []; // Create an empty array.
            for (let i = 0; i < data.length; i++) {
                let movie = data[i]
                let releaseDate = new Date(movie[1])
                movie_lst.push({
                    'name': movie[0], 
                    'date': releaseDate,
                    'img': `https://image.tmdb.org/t/p/w185${movie[2]}`
                    // 'Total Revenue': movie[3]
                })
            }
            TimeKnots.draw("#timeline", movie_lst, {horizontalLayout: true, color: "#669", height: 450, width:500, showLabels: true, labelFormat:"%H:%M"});
        });
    });
}

// function upd_timeline(){

// }
// d3v7select("#my_button").on("click", upd_timeline);

init();