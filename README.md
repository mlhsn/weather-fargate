# Weather Service

This this a microservice that provides current weather information based on given City name, i.g. `Dhaka`.

### Usage

Make HTTP request to `GET <server_name>/weather/{city_name}` to get todays weather condition in JSON format.


### Setup [Development]

- Clone the repostory
- Run in console; to create a virtual env and install package in it.
  ```shell
  poetry sync
  ```
- Run in console; to start the app
  ```shell
  poetry run fastapi dev asgi.py
  ``` 
- Run in console; to to see the weather of Dhaka city.
  ```shell
  curl -s http://127.0.0.1:8000/weather/dhaka
  ``` 

### Stability 
This service is in **beta**.
