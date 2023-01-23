// function to change track image on main page
function changeTrackImage(element) {
    let track_id = element.target.id
    if (track_id === 'track_graphic') {
        document.getElementById('track_graphic').setAttribute("src", "https://res.cloudinary.com/grawnya/image/upload/v1674393438/formula1_dublin_street_race_map_vpf8oo.png")
        document.getElementById('track_graphic').setAttribute("alt", "Track mapped onto Google Maps")
        document.getElementById('track_graphic').setAttribute('id', 'track_map')}
        else if (track_id === 'track_map') {
        document.getElementById('track_map').setAttribute("src", "https://res.cloudinary.com/grawnya/image/upload/v1674393431/track_with_stands_fok6ra.png")
        document.getElementById('track_map').setAttribute("alt", "Track image with stands")
        document.getElementById('track_map').setAttribute('id', 'track_graphic')
    }
}

document.addEventListener('click', changeTrackImage)