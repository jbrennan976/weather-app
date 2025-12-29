
# Weather App
A small web app that fetches current weather from OpenWeatherMap via a FastAPI backend and displays it in a lightweight frontend.

Deployed via Render and Netlify: https://jbweather-appv1.netlify.app/

**Tech Stack:**
- **Backend:** FastAPI
- **Frontend:** Vanilla HTML/CSS/JS
- **External API:** OpenWeatherMap Current Weather API
- **Deployment:** Render for backend, Netlify for frontend

**Requirements**
- **Python:** 3.10+ recommended
- **Pip packages:** See `backend/requirements-prod.txt`

**Setup (local, macOS)**
-
- **1. Clone & open project:**

	```
	git clone <repo-url>
	cd weather-app
	```

- **2. Backend environment**
    - Create a virtual environment and install dependencies:

    ```
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r backend/requirements-prod.txt
    ```

- Create a `backend/.env` file with your OpenWeatherMap API key:

	```env
	WEATHER_API_KEY=your_openweathermap_key_here
	```

- **3. Run the backend**

	```
	# Navigate to backend directory
    cd backend
    # Run app
	uvicorn app:app --reload --host 127.0.0.1 --port 8000
	```

	- Health check: `http://127.0.0.1:8000/health`
	- Weather endpoint example: `http://127.0.0.1:8000/weather?city=London`

- **4. Run the frontend (static)**

	The frontend uses `frontend/config.js` to point to the API base URL. By default it is set to `http://127.0.0.1:8000`.

	A simple way to serve the frontend locally:

	```
	cd frontend
	python3 -m http.server 5500
	```

	Then open `http://127.0.0.1:5500` in your browser.


**Next Steps**
-
- Add TTL Response Caching
- User Login and Authentication
- Rate Limiting per user
- Saved weather widgets per user




