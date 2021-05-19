# Weather Tracking System



## Implemented:

- ### Weather Agent API:
  
  - Weather Agent  CRUD endpoints with access to mongoDB
  - Weather Agent get city last weather data endpoint
  - Schedule daily background tasks for daily data collection at specific time of day
  - CRUD endpoints unit tests
- ### Weather Service API:
  
  - Current Weather Data Collection from OpenWeatherMap
  - OpenAPI (Swagger) specification support
  - Caching OpenWeatherMap API responses with Redis backend. Redis key is the city name and the values are the external api's response. Keys expire after we specify elapsed time after storing it in cache.
  - Docker Image
  - Tests
  
- Docker Compose YAML for running the system

## ToDOs



- Unit test GetCurrentWeatherData response before storing into database

* API internalization

## Run System

### Using Docker

Download repo  and from weather tracker directory run:

```bas
$ docker-compose build
$ docker-compose up -d
```

### Weather Agent API

To access the Weather Service API  endpoints, execute the following commands:

To add a city to city watch list:

```bash
curl -XPOST -H 'Content-Type: application/json' http://localhost:5000/WeatherAgent/insert_city -d '{"city": "Volos"}'
```

To remove a city from watch list:

```bash
curl -XDELETE -H 'Content-Type: application/json' http://localhost:5000/WeatherAgent/delete_city/Volos
```

To get a list of tracked cities:

```bash
curl -i "http://localhost:5000/WeatherAgent/ListCities"
```

To get city's last weather data:

```bash
curl -i "localhost:5000/WeatherAgent/get_city_weather_data" -d "city"="Volos"
```

![cities_collection](./images/weather-agent.png)

### Weather Service API

To access the Weather Wervice API head to  <docker-hosted-service-url/weather_service> and inspect the API documentation via swagger ui.

![cities_collection](./images/weather-service.png)



### Weather Agent API

### MongoDB collections instances

![cities_collection](./images/cities_collection.png)

