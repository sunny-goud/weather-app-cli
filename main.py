print("Weather App")

city = input("Enter city name: ")

if city.lower() == "hyderabad":
    print("Temperature: 35°C")
    print("Humidity: 60%")
    print("Condition: Sunny")

elif city.lower() == "delhi":
    print("Temperature: 38°C")
    print("Humidity: 45%")
    print("Condition: Hot")

else:
    print("Weather data not available for", city)