// Function to automatically dismiss the alert after 3 seconds
setTimeout(function() {
    var messages = document.getElementById("msg");
    var alert = new bootstrap.Alert(messages);
    alert.close();
}, 3000);

// function to change track image on main page
function changeTrackImage(element) {
    var track_id = element.target.id
    console.log(track_id)
    if (track_id === 'track_graphic') {
        document.getElementById('track_graphic').innerHTML = '<img src="https://res.cloudinary.com/grawnya/image/upload/v1674393438/formula1_dublin_street_race_map_vpf8oo.png" alt="Track mapped onto Google Maps">'
        document.getElementById('track_graphic').setAttribute('id', 'track_map')}
    else if (track_id === 'track_map') {
        document.getElementById('track_map').innerHTML = '<img src="https://res.cloudinary.com/grawnya/image/upload/v1674393431/track_with_stands_fok6ra.png" alt="Track image with stands">'
        document.getElementById('track_map').setAttribute('id', 'track_graphic')
    }
}

document.addEventListener('click', changeTrackImage)