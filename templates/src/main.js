////////////////////////////////////////////////////////////// Our code, take out if doesn't work
function init_top(){
    d3.json("/api/top10actors").then(data => {
        console.log(data)

        // var mySchedule = [{name:"Wake up", date: "2012-09-28T06:00:00"},
        // {name:"Breakfast", 	date:"2012-09-28T06:30:00"},
        // {name:"Leave kids at school", 	date:"2012-09-28T07:45:00"},
        // {name:"Check email", date:	"2012-09-28T08:00:00"},
        // {name:"Lunch", date:	"2012-09-28T11:30:00"},
        // {name:"Send report", date:	"2012-09-28T13:15:00"},
        // {name:"Pick kids", date:	"2012-09-28T17:16:00"},
        // {name:"Dinner", date:	"2012-09-28T18:13:00"},
        // {name:"Watch a movie", date:	"2012-09-28T20:16:00"},
        // {name:"Go to sleep", date:	"2012-09-28T23:00:00"}
        // ];

        // TimeKnots.draw("#timeline2", mySchedule, {horizontalLayout: false, color: "#669", height: 450, width:200, showLabels: true, labelFormat:"%H:%M"});
    })
}

// function upd_timeline(){

// }
// d3.select("#my_button").on("click", upd_timeline);

init_top();