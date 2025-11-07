const result = document.querySelector(".weather-results")

document.getElementById("myForm").addEventListener("submit", async (event) => {
    event.preventDefault()
    result.innerHTML=""
    let city = document.getElementById("city").value
    city = city.trim().toLowerCase()
    await fetchWeather(city)
    document.getElementById("myForm").reset()
});

async function fetchWeather(city){
    try {
        const response = await fetch(`http://127.0.0.1:8000/weather?city=${city}`)

        if (!response.ok){
            if (response.status == 404){
                throw new Error(`Unable to find weather for: ${city}.`)
            }
            else{
                throw new Error(`An error occured getting weather.`)
            }
        }
        const data = await response.json()
        displayWeather(data)
    }

    catch (error) {
        if ((error.message.includes("Unable to find weather for")) || (error.message.includes("An error occured getting weather"))){
            console.error(error)
            displayError(error)
        }
        else{
            console.error(error)
            displayError("Something went wrong please try again later.")
        }
    }
}

function displayWeather(data){
    console.log(data)

    const weatherArticle = document.createElement("article")
    weatherArticle.classList.add("card", "weather")

    const cityDisplay = document.createElement("h2")
    cityDisplay.textContent = data["location"]

    const timeDisplay = document.createElement("h3")
    timeDisplay.textContent = data["time"]

    const tempDisplay = document.createElement("h3")
    tempDisplay.textContent = `${data["temp"]}°F`

    const forecastDisplay = document.createElement("h3")
    forecastDisplay.textContent = data["forecast"]

    const weatherIcon = document.createElement("img")
    weatherIcon.src = `https://openweathermap.org/img/wn/${data["icon-id"]}@2x.png`
    weatherIcon.alt = "Weather icon image"


    weatherArticle.append(cityDisplay, timeDisplay, tempDisplay,forecastDisplay, weatherIcon)
    result.append(weatherArticle)
}


function displayError(errorMessage){

    const errorArticle = document.createElement("article")
    errorArticle.classList.add("card", "error")

    const errorDisplay = document.createElement("h2")
    errorDisplay.textContent = errorMessage

    errorArticle.append(errorDisplay)
    result.append(errorArticle)
}

