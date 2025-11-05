const result = document.getElementById("weatherResults")

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
        displayWeather(data)
    }

    catch (error) {
        console.error(error)
    }
}

function displayWeather(data){
    console.log(data)
    result.innerHTML = ""

    const weatherArticle = document.createElement("article")

    const cityDisplay = document.createElement("h1")
    cityDisplay.textContent = data["location"]

    const forecastDisplay = document.createElement("h2")
    forecastDisplay.textContent = data["forecast"]

    const tempDisplay = document.createElement("h2")
    tempDisplay.textContent = data["temp"]

    const timeDisplay = document.createElement("h2")
    timeDisplay.textContent = data["time"]

    weatherArticle.append(cityDisplay, forecastDisplay, tempDisplay, timeDisplay)
    result.append(weatherArticle)
}
    

