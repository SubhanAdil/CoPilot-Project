window.onload = function () {

const high = Number(document.getElementById("high").value);
const medium = Number(document.getElementById("medium").value);
const low = Number(document.getElementById("low").value);

// ---------------- Pie Chart ----------------

new Chart(document.getElementById("pieChart"),{

type:"pie",

data:{

labels:["High","Medium","Low"],

datasets:[{

data:[high,medium,low]

}]

}

});


// ---------------- Bar Chart ----------------

new Chart(document.getElementById("barChart"),{

type:"bar",

data:{

labels:["High","Medium","Low"],

datasets:[{

label:"Students",

data:[high,medium,low]

}]

}

});




// ---------------- Line Chart ----------------

new Chart(document.getElementById("lineChart"),{

type:"line",

data:{

labels:["High","Medium","Low"],

datasets:[{

label:"Performance",

data:[high,medium,low],

fill:false

}]

}

});

};