import requests
import folium
import webbrowser

print("===== IP Geolocation Tracker =====")

ip = input("Enter IP Address: ")

try:
    response = requests.get(f"http://ip-api.com/json/{ip}")
    data = response.json()

    if data["status"] == "success":

        city = data["city"]
        state = data["regionName"]
        country = data["country"]
        lat = data["lat"]
        lon = data["lon"]

        print("\nIP Address:", ip)
        print("City:", city)
        print("State:", state)
        print("Country:", country)
        print("Latitude:", lat)
        print("Longitude:", lon)

        map = folium.Map(location=[lat, lon], zoom_start=12)

        folium.Marker(
            [lat, lon],
            popup=f"{city}, {country}"
        ).add_to(map)

        map.save(r"D:\HexSoftwares_Python_Programming\HexSoftwarePP_Task-3\Task3_Project1_Geolocation_Tracker\location_map.html")


        print("\nMap Generated Successfully!")
        webbrowser.open(r"D:\HexSoftwares_Python_Programming\HexSoftwarePP_Task-3\Task3_Project1_Geolocation_Tracker\location_map.html")
    else:
        print("Invalid IP Address!")

except Exception as e:
    print("Error:", e)