document.getElementById("myForm").addEventListener("submit", async (event) => {
    event.preventDefault()
    let city = document.getElementById("city").value
    city = city.trim().toLowerCase()
    await fetchWeather(city)
    document.getElementById("myForm").reset()
});

async function fetchWeather(city){
    try {
        const response = await fetch(`http://127.0.0.1:8000/weather?city=${city}`)

        if (!response.ok){
            throw new Error(`An error occured getting weather for ${city}`)
        }
        const data = await response.json()
        console.log(data)
    }

    catch (error) {
        console.error(error)
    }
}
