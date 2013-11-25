    var position=new google.maps.LatLng(44.63694,  -63.58958);
    var pdiv=document.getElementById("demo");
    var map;
    function initialize() {
      var mapOptions = {
        center: position,
        zoom: 16,
        mapTypeId: google.maps.MapTypeId.ROADMAP
      };
      map = new google.maps.Map(document.getElementById("map"),
        mapOptions);

      addMarker(position);

    }
     google.maps.event.addDomListener(window, 'load', initialize);

	google.maps.event.addDomListener(document.getElementById("button"), 'click', getLocation);


    function getLocation()
    {
      if (navigator.geolocation)
      {
        navigator.geolocation.getCurrentPosition(showPosition);
      }
      else{pdiv.innerHTML="Geolocation is not supported";}
    }

    function showPosition(p)
    {
      position = p;
      pdiv.innerHTML="Latitude: " + position.coords.latitude +
      "<br>Longitude: " + position.coords.longitude;
    }

    function getPosition()
    {
      return position;
    }
    function addMarker(p) {
      var markerOptions = {
        position: p,
        title: 'your location',
        map : map,
        icon: 'https://maps.gstatic.com/mapfiles/ms2/micons/blue-dot.png'
      };
      var marker = new google.maps.Marker(markerOptions);

    }
