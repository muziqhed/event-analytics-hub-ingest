

TEST_GOOD_TEMP_DATA = [
    {
        "sensor_type": "xyzTempsensor",
        "sensor_name": "Sensor1",
        "temperature_scale": "fahrenheit",
        "temperature": 32.3,
        "timestamp": "2024-01-01T12:00:00"
    },
    {
        "sensor_type": "xyzTempsensor",
        "sensor_name": "Sensor1",
        "temperature_scale": "fahrenheit",
        "temperature": 32.5,
        "timestamp": "2024-01-01T12:00:05"
    },
    {
        "sensor_type": "xyzTempsensor",
        "sensor_name": "Sensor1",
        "temperature_scale": "fahrenheit",
        "temperature": 33.95,
        "timestamp": "2024-01-01T12:00:10"
    },
    {
        "sensor_type": "xyzTempsensor",
        "sensor_name": "Sensor2",
        "temperature_scale": "fahrenheit",
        "temperature": 90,
        "timestamp": "2024-01-01T12:05:00"
    },
    {
        "sensor_type": "xyzTempsensor",
        "sensor_name": "Sensor1",
        "temperature_scale": "fahrenheit",
        "temperature": 35.5
    }
]

TEST_BAD_TEMP_DATA = [
    {
        "sensor_type": "xyzTempsensor",
        "somebadfieldname": "baddata",
        "temperature_scale": "fahrenheit",
        "temperature": 32.3,
        "timestamp": "2024-01-01T12:00:00"
    },
    {
        "sensor_type": "xyzTempsensor",
        "sensor_name": "Sensor1",
        "temperature_scale": "fahrenheit",
        "temperature": 32.5,
        "timestamp": "2024-01-01T12:00:05"
    },
    {
        "timestamp": "2024-01-01T12:00:10"
    },
    {
        "sensor_type": "xyzTempsensor",
        "sensor_name": "Sensor2",
        "temperature_scale": "fahrenheit",
        "timestamp": "2024-01-01T12:05:00"
    },
    {
        "sensor_type": "xyzTempsensor",
        "sensor_name": "Sensor1",
        "temperature_scale": "fahrenheit",
        "temperature": 35.5,
        "timestamp": "2024-01-01T12:00:15"
    }
]
