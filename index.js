// function initMap(data) {
//     var flag = {lat: XXX, lng: YYY};
//     var map = new google.maps.Map( document.getElementById('map'), {zoom: 4, center: flag});
//     var marker = new google.maps.Marker({position: flag, map: map}); } src="https://maps.googleapis.com/maps/api/js?key=AIzaSyBxqMOLD18Q38ZEqTI_Wi-0VctZ1m41H7Q&callback=initMap">
// }

let map;

function initMap() {
  map = new google.maps.Map(document.getElementById("map"), {
    center: { lat: -34.397, lng: 150.644 },
    zoom: 8,
  });
}