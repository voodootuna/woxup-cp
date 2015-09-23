function initialize() {

  var mapOptions = {
    zoom: 13,
	   scrollwheel: false,
    center: new google.maps.LatLng(lat1, lng1)
  };
  var map = new google.maps.Map(document.getElementById('map-canvas'),
      mapOptions);

  // Create a marker and set its position.
  var marker = new google.maps.Marker({
    map: map,
    position: new google.maps.LatLng(lat1, lng1),
 });

  var trafficLayer = new google.maps.TrafficLayer();


 google.maps.event.addDomListener(document.getElementById("traficToggle"), 'click', function() {
        if ( trafficLayer.getMap() != null ) {
            trafficLayer.setMap(null);
        }
        else {
            trafficLayer.setMap(map);
        }
    });



};
  var panorama = new google.maps.StreetViewPanorama(
    document.getElementById('street-view-canvas'),
    {
      position: {lat:lat1, lng:lng1},
      pov :{heading:165, pitch:0},
      zoom:1
    });


google.maps.event.addDomListener(window, 'load', initialize);

