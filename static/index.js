var map;
var markers = []
var locations = [];
var currentRequest;

var timerLoop;


function parseResponse (resp) {

   for (var i = 0 ;  i < resp.length ; i++) {
          resp[i] = resp[i].toString();
    };
    return resp;
}
$(document).ready(function (){


  $('.key-words').change(function() {

    var keyword = $('.key-words option:selected').val();

    clearTheMap();

    if (currentRequest) {

      currentRequest.abort();

    }


    clearInterval (timerLoop);


    timerLoop = setInterval (function () {

    currentRequest =  $.ajax({

      url : "search/" + keyword,
      success: function (resp) {


        resp = parseResponse (resp);

        var difference = differenceBetweenTwoArrays (locations, resp);
        locations =  locations.concat(difference);
        plotNewLocationsOnMap (difference);
      }

    });
    
    }, 1000);
  });


});





function initializeTheMap() {
  
  var coordinates="";
  map = new google.maps.Map(document.getElementById('map'), {
    center: new google.maps.LatLng(0, 0),
    zoom: 2
  });


}

function plotNewLocationsOnMap ( locations) {
  var geocoder = new google.maps.Geocoder();

  for (var i = 0; i < locations.length; i++) {

    geocoder.geocode( { 'address': locations[i] }, function(results, status) {
      if (status == google.maps.GeocoderStatus.OK) {

        coordinates=results[0].geometry.location;

        var marker = new google.maps.Marker({
          position: coordinates,
          map: map

        });

        markers.push(marker);
      }

    });

  }
}

function clearTheMap () {
  locations = [];
  for (var i = 0; i < markers.length; i++) {
          markers[i].setMap(null);
  }

}


function differenceBetweenTwoArrays (a2, a1) {

  var a = [], diff = [];

    for (var i = 0; i < a1.length; i++) {
        a[a1[i]] = true;
    }

    for (var i = 0; i < a2.length; i++) {
        if (a[a2[i]]) {
            delete a[a2[i]];
        } else {
            a[a2[i]] = true;
        }
    }

    for (var k in a) {
        diff.push(k);
    }

    return diff;

}

