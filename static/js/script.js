// function to change track image on main page
document.addEventListener('click', function(element) {
    let track_id = element.target.id;
    console.log(track_id);
    if (track_id === 'track_graphic') {
        document.getElementById('track_graphic').setAttribute("src", "https://res.cloudinary.com/grawnya/image/upload/v1674393438/formula1_dublin_street_race_map_vpf8oo.png")
        document.getElementById('track_graphic').setAttribute("alt", "Track mapped onto Google Maps")
        document.getElementById('track_graphic').setAttribute('id', 'track_map')}
        else if (track_id === 'track_map') {
        document.getElementById('track_map').setAttribute("src", "https://res.cloudinary.com/grawnya/image/upload/v1674393431/track_with_stands_fok6ra.png")
        document.getElementById('track_map').setAttribute("alt", "Track image with stands")
        document.getElementById('track_map').setAttribute('id', 'track_graphic')
    }
})

// function to make checkered flag image travel to the bottom of the screen if a large screen
document.addEventListener("DOMContentLoaded", function() {
    let screenWidth = screen.width;
    if (screenWidth >= 1024) {
        let scrollHeight = document.documentElement.scrollHeight;
        const flag = document.getElementById("flag")
        let position = -100;
        id = setInterval(downMotion, 3);
        function downMotion() {
            if (position < scrollHeight-60) {
                position += 5;
                flag.style.top = position + "px";
            }
        }
    }
}) 