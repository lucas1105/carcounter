var map;
var sensor_point;
var marker

function initMap() {
    var inicial = {lat: -26.915060, lng: -48.663639};

    map = new google.maps.Map(document.getElementById('map'), {
        zoom: 15,
        center: inicial,
    });

    // This event listener will call addMarker() when the map is clicked.
    map.addListener('click', function (event) {



        if (!marker){
            addMarker(event.latLng);
        }
        else{
            marker.setPosition(event.latLng)
        }
        document.getElementById("inputLat").value=event.latLng.lat();
        document.getElementById("inputLng").value=event.latLng.lng();
    });
}

// Adds a marker to the map and push to the array.
function addMarker(location) {
    marker = new google.maps.Marker({
        position: location,
        map: map
    });
    sensor_point=marker;
}