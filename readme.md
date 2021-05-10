# Weather Tracking System

## Implemented:

- Weather Agent API:
  - Weather Agent  CRUD endpoints with access to mongoDB
  - Weather Agent get city last weather data endpoint
- Weather Service API:
  - Current Data Collection from OpenWeatherMap
  - OpenAPI (Swagger) specification support

## ToDOs

* Weather Agent API:
  * Schedule daily background tasks for daily data collection
  * Tests
  * API specification
  * Docker image

* Weather Service API:
  * API internalization
  * Cache weather data to mongoDB. 
  * Clear the old cache data.
  * Tests
  * Docker image
* MongoDB as a Docker Container

## Run System

For the present moment we need to have a running mongoDB  instance on your machine and a virtual python environment to support the system's functionality.

### Weather Service API

To launch the Weather Service API go to the weather_service sub-directory and run server.py. You can go to http://localhost:5200/weather_service_api  to inspect the APIs functionality.

### Weather Agent API

To launch the Weather Agent API go to the weather_agent sub-dir and run server.py. Currently OpenAPI is not supported, instead you can check CRUD functionality by issuing the following commands:

To add a city to city watch list:

```bash
curl -i "localhost:5000/weather_agent/add_city" -d "city"="London"
```

To remove a city from watch list:

```bash
curl -i "localhost:5000/weather_agent/delete_city" -d "city"="London"
```

To get a list of tracked cities:

```bash
curl -i "localhost:5000/weather_agent/get_cities'" -d "city"="London"
```

To get city's last weather data:

```bash
curl -i "localhost:5000/weather_agent/get_city_weather_data" -d "city"="London" -d "unit"="metric"
```

### MongoDB collections instances

* Cities collection

![cities_collection](./images/cities_collection.png)

![weather_collection](./images/weather_collection.png)