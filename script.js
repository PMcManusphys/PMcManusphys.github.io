


function saveValue() {
    // Get the value of the input element
    var outputname = document.getElementById("opn").value;
    var distric = document.getElementById("distric").value;
    try {
        var selectedColor = document.querySelector('input[name="bw"]:checked');
        var justbw = selectedColor.value;
    } catch (e) {
        var justbw = true;
    }
    try {
        var selectedzeros = document.querySelector('input[name="nozeros"]:checked');
        var nozero = selectedzeros.value;
    } catch (e) {
        var nozero = false;
    }
    
    var at1 = document.getElementById("assessmentt1").value;
    var av1 = document.getElementById("assessmentv1").value;
    
    var assess = [[at1,av1]];
    try {
        var at2 = document.getElementById("assessmentt2").value;
        var av2 = document.getElementById("assessmentv2").value;
        assess.push([at2,av2])
    } catch (e) {
        console.log('myNonExistentVariable is not declared');
    }
    try {
        var at3 = document.getElementById("assessmentt3").value;
        var av3 = document.getElementById("assessmentv3").value;
        assess.push([at3,av3])
    } catch (e) {
        console.log('myNonExistentVariable is not declared');
    }
    try {
        var at4 = document.getElementById("assessmentt4").value;
        var av4 = document.getElementById("assessmentv4").value;
        assess.push([at4,av4])
    } catch (e) {
        console.log('myNonExistentVariable is not declared');
    }
    try {
        var at5 = document.getElementById("assessmentt5").value;
        var av5 = document.getElementById("assessmentv5").value;
        assess.push([at5,av5])
    } catch (e) {
        console.log('myNonExistentVariable is not declared');
    }
    try {
        var at6 = document.getElementById("assessmentt6").value;
        var av6 = document.getElementById("assessmentv6").value;
        assess.push([at6,av6])
    } catch (e) {
        console.log('myNonExistentVariable is not declared');
    }
    try {
        var at7 = document.getElementById("assessmentt7").value;
        var av7 = document.getElementById("assessmentv7").value;
        assess.push([at7,av7])
    } catch (e) {
        console.log('myNonExistentVariable is not declared');
    }
    try {
        var at8 = document.getElementById("assessmentt8").value;
        var av8 = document.getElementById("assessmentv8").value;
        assess.push([at8,av8])
    } catch (e) {
        console.log('myNonExistentVariable is not declared');
    }    try {
        var at9 = document.getElementById("assessmentt9").value;
        var av9 = document.getElementById("assessmentv9").value;
        assess.push([at9,av9])
    } catch (e) {
        console.log('myNonExistentVariable is not declared');
    }    try {
        var at10 = document.getElementById("assessmentt10").value;
        var av10 = document.getElementById("assessmentv10").value;
        assess.push([at10,av10])
    } catch (e) {
        console.log('myNonExistentVariable is not declared');
    }    try {
        var at11 = document.getElementById("assessmentt11").value;
        var av11 = document.getElementById("assessmentv11").value;
        assess.push([at11,av11])
    } catch (e) {
        console.log('myNonExistentVariable is not declared');
    }
    try {
        var selectedtype = document.querySelector('input[name="type"]:checked');
        var type = selectedtype.value;
    } catch (e) {
        var type = "proficiency scale";
    }
    
    var pscale1 = document.getElementById("scale1").value;
    var pscale2 = document.getElementById("scale2").value;
    var pscale3 = document.getElementById("scale3").value;
    var pscale4 = document.getElementById("scale4").value;
    try {
        var selectedcompw = document.querySelector('input[name="compw"]:checked');
        var compw = selectedcompw.value;
    } catch (e) {
        var compw = "average";
    }
    try {
    var selectedoldnew = document.querySelector('input[name="oldnew"]:checked');
    var oldnew = selectedoldnew.value;
    } catch (e) {
        var oldnew = "old";
    }
    
    var wscale = document.getElementById("wscale").value;
    
    var opn = document.getElementById("namename").value;
    
    
    // Do something with the value
    var myObject = { "output_name": outputname,
        "district": distric,
        "just_bw": justbw,
        "no_zero": nozero,
        "weighting": assess,
        "type" : type,
        "prof_scale": [pscale4,pscale3,pscale2,pscale1],
        "weighting_type": compw,
        "new_old": oldnew,
        "scale": wscale,
        "course_name": opn
    };
    
    // Convert the object to a JSON string
    var jsonData = JSON.stringify(myObject);
   
    fetch("https://uvidrr7d1h.execute-api.ca-central-1.amazonaws.com/default/api", {
          method: "POST",
          body: jsonData,
          headers: {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "https://pmcmanusphys.github.io" // Replace with your origin domain
          },
          mode: "cors"
         })
    
    .then(res => res.json())
    .then(json => console.log(json))
    .catch(err => console.error(err));
    // Save the JSON string to a file
    //saveJSON(jsonString, "my-data.json");
    
    // Send the JSON data to the API endpoint
    //var xhr = new XMLHttpRequest();
    //xhr.open('POST', 'http://mr-mcmanus.great-site.net/');           //'http://yourapiendpoint.com/upload');
    //xhr.setRequestHeader('Content-Type', 'application/json');
    //where does the filename come from? how do we know its name? Can I make sure if two go at the same time that it gets the right one.
    //might need to have file saved first not sure.
    //xhr.send(jsonString);
}



function submitForm() {
    // Get the form element
    var form = document.getElementById('uploadForm');
    
    // Submit the form
    form.submit();
}


function saveJSON(jsonString, fileName) {
    var blob = new Blob([jsonString], {type: "application/json"});
    saveAs(blob, fileName);
}
var count = 0;
function addQuestion()
{
    // Get the quiz form element
    var data = document.getElementById('data');
    
    // Good to do error checking, make sure we managed to get something
    if (data)
    {
        if (count < 11)
        {
        // Create the new text box
        var newInput = document.createElement('input');
        newInput.type = 'text';
        newInput.name = 'assessmenttype[]';
        var newInputtwo = document.createElement('input');
        newInputtwo.type = 'text';
        newInputtwo.name = 'assessmentvalue[]';
        if (count == 0){
            newInput.id = "assessmentt2";
            newInputtwo.id = "assessmentv2";
            
        }
        if (count == 1){
            newInput.id = "assessmentt3";
            newInputtwo.id = "assessmentv3";
            
        }
        if (count == 2){
            newInput.id = "assessmentt4";
            newInputtwo.id = "assessmentv4";
            
        }
        if (count == 3){
            newInput.id = "assessmentt5";
            newInputtwo.id = "assessmentv5";
            
        }
        if (count == 4){
            newInput.id = "assessmentt6";
            newInputtwo.id = "assessmentv6";
            
        }
        if (count == 5){
            newInput.id = "assessmentt7";
            newInputtwo.id = "assessmentv7";
            
        }
        if (count == 6){
            newInput.id = "assessmentt8";
            newInputtwo.id = "assessmentv8";
            
        }
        if (count == 7){
            newInput.id = "assessmentt9";
            newInputtwo.id = "assessmentv9";
            
        }
        if (count == 8){
            newInput.id = "assessmentt10";
            newInputtwo.id = "assessmentv10";
            
        }
        if (count == 9){
            newInput.id = "assessmentt11";
            newInputtwo.id = "assessmentv11";
            
        }
        if (count == 10){
            newInput.id = "assessmentt12";
            newInputtwo.id = "assessmentv12";
            
        }
        if (count == 11){
            newInput.id = "assessmentt13";
            newInputtwo.id = "assessmentv13";
            
        }
        // Good practice to do error checking
        
            // Add the new elements to the form
            data.appendChild(newInput);
            data.appendChild( document.createTextNode( '\u00A0' ) );
            data.appendChild(newInputtwo);
            data.appendChild(document.createElement("br"));
            
            // Increment the count
            count++;

            
        }
        else
        {
            alert('Assessment type limit reached');
        }
    }
}


function ShowHideDiva() {
    var chkYes = document.getElementById("time_amount");
    var dva = document.getElementById("newold");
    dva.style.display = chkYes.checked ? "block" : "none";
    var dva = document.getElementById("weightingscale");
    dva.style.display  = "block";
    
    
}
function ShowHideDivb() {

    var chkYes = document.getElementById("time_based");
    var dva = document.getElementById("newold");
    dva.style.display = chkYes.checked ? "block" : "none";
    var dva = document.getElementById("weightingscale");
    dva.style.display  = "block";
    
}


function HideScale() {
    
    var chkYes = document.getElementById("average");
    var dva = document.getElementById("weightingscale");
    dva.style.display  = "none";
    var dv = document.getElementById("newold");
    dv.style.display  = "none";
    
    
}





//<h2>Checkboxes</h2>
//<p>The <strong>input type="checkbox"</strong> defines a checkbox:</p>


//<input type="checkbox" id="vehicle1" name="vehicle1" value="Bike">
//<label for="vehicle1"> I have a bike</label><br>
//<input type="checkbox" id="vehicle2" name="vehicle2" value="Car">
//<label for="vehicle2"> I have a car</label><br>
//<input type="checkbox" id="vehicle3" name="vehicle3" value="Boat">
//<label for="vehicle3"> I have a boat</label><br><br>
//<input type="submit" value="Submit">
//</form>
