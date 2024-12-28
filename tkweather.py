import tkinter as tk
import requests

# Function to fetch weather data
def get_weather():
    api_key = '3fc9568cf7494ad3beb185004241912'  # Replace with your WeatherAPI key
    city = entry_city.get().strip()
    if city:
        try:
            # API request
            response = requests.get(f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no")
            data = response.json()

            if response.status_code == 200:
                temp = data['current']['temp_c']
                condition = data['current']['condition']['text']
                result_label.config(text=f"Temperature: {temp}°C\nCondition: {condition}")
            elif data.get('error') and data['error']['code'] == 1006:
                result_label.config(text="City not found.")
            else:
                result_label.config(text="Unexpected error occurred.")
        except requests.exceptions.RequestException as e:
            result_label.config(text="Network error. Please check your internet connection.")
    else:
        result_label.config(text="Please enter a city.")

# Create the main Tkinter window
root = tk.Tk()
root.title("Weather App")
root.geometry("300x200")

# Labels and Entry Widget
tk.Label(root, text="Enter City:", font=("Arial", 14)).grid(row=0, column=0, padx=10, pady=10)
entry_city = tk.Entry(root, font=("Arial", 14))
entry_city.grid(row=0, column=1, padx=10, pady=10)

# Fetch Weather Button
fetch_button = tk.Button(root, text="Get Weather", command=get_weather, font=("Arial", 14))
fetch_button.grid(row=1, column=0, columnspan=2, pady=10)

# Result Label
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.grid(row=2, column=0, columnspan=2, pady=10)

# Run the application
root.mainloop()
