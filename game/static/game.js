

var win_count = 0;
var trials = 0;


  function toggle(i,j) {
          b=document.getElementById("but_"+i+j);
          t = b.innerHTML;
          if (t=="X") {b.innerHTML = "O";
                       b.setAttribute("style", "color:green; background-color:white");
                      }
          if (t=="O") {b.innerHTML = "X";
                       b.setAttribute("style", "color:white; background-color:black");
                      }
        }
        
    
    // Please complete this function
    function press(i,j) {
    trials = trials+1
    var element = document.getElementById("but_"+i+j);
    var id = element.getAttribute("id");
    document.getElementById("trials").innerHTML=trials
    
    var array = id.split("");
    var coord1 = Number(array[4]);
    var coord2 = Number (array[5]);
    var count = 0
        toggle(coord1,coord2);
    try {
        toggle(coord1+1,coord2);
    
         checkAllOff();
    }
    catch(err){
     count = count+1;
    }
    try {
        toggle(coord1-1,coord2);
    
         checkAllOff();
    }
    catch(err){
     count = count+1;
    }
    try {
        toggle(coord1,coord2-1);
    
         checkAllOff();
    }
    catch(err){
     count = count+1;
    }
    try {
        toggle(coord1,coord2+1);
    
         checkAllOff();
    }
    catch(err){
     count = count+1;
    }
    
    
    
    }
    
    // Please complete this function
    function checkAllOff(){
    var count = 0

    for( var y=0; y< 5; y++ ) {
        for(var r=0; r<5; r++){
         var cell = document.getElementById("but_"+y+r);
          f = cell.innerHTML;
          if (f == "X"){ count = count +1;
      } 
     } 
    }
    
    while (count == 25){
    win_count = win_count+1;
    Check_Win(count,win_count)
    return(document.getElementById("end").innerHTML="Congratulations! All lights out!")
    
    }
    while (count < 25){
    Check_Win(count,win_count)    
    return(document.getElementById("end").innerHTML="")
    
    }
    }
    
    function Check_Win(count,win_count){
        
        if(count == 25){
            document.getElementById("wins").innerHTML=win_count
        }
        
    }

    // function doWork(){
    //     var xml = new XMLHttpRequest()
    //     wins = document.getElementById("wins").innerHTML
    //     dataSend =JSON.stringify({
    //         "Wins":"10",
    //         "Trials":"100"
    //     })
    //     console.log("1w")
    //     $.post("result",JSON.stringify(10))
       
    // }

    // window.onload = function() {
    //     // setup the button click
    //     document.getElementById("submit").onclick = function() {
    //        doWork()
    //     };
    // }


    // Please complete this function
    function resetGrid(){
    document.getElementById("end").innerHTML=""
    for( var z=0; z< 5; z++ ) { 
            for(var x=0; x<5; x++){    
                var cell = document.getElementById("but_"+z+x); 
                var state = cell.innerHTML
                if(state == "X"){cell.innerHTML = "O";
                   cell.setAttribute("style", "color:green; background-color:white");
                }
    
    
            
            }
         }
         toggle(2,2)
       
    }
// Add saving button
// // work out how to send info as http request to flask to then update db
//     function sendUserinfo(){
//         console.log("as")
//         userinfo1 = document.getElementById("wins").value
//         console.log(userinfo1)
//         const request = new XMLHttpRequest()
//         x =JSON.stringify(userinfo1)
//         request.open("POST", "/ProcessUserinfo/${JSON.stringify(userinfo1)}" )
//         request.send()
//     }


    // 
    function generateGrid() {
           
            var d = document.getElementById("button-grid");
            var table = document.createElement("table");
            d.appendChild(table);
            for (var i = 0; i < 5; i++) {
                    var row = document.createElement("tr");
                    for (var j = 0; j < 5; j++) {
                            var cell = document.createElement("td");
                            cell.innerHTML = "<button type=button id=but_" + i + j +
                                             " onclick=\"press(" +i + ',' +j + ")\"" + 
                                             " style=\"color:green; background-color:white\"" +
                                             ">O</button>" ;
                            row.appendChild(cell);
                    }
                    table.appendChild(row);
            }
            toggle(2,2) // initial state
    }
    
    window.onload = function() {
            generateGrid();
    };
    