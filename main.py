import requests
import tkinter as tk
from tkinter import ttk,messagebox
import tkinter.font as font
fhand=open("worldcities.csv")
cities_list = []
for line in fhand :
    line = line.strip()
    line = line.split(",")
    town = line[1]
    cities_list.append(town)
countries = [
    "Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda", "Argentina", "Armenia",
    "Australia", "Austria", "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus",
    "Belgium", "Belize", "Benin", "Bhutan", "Bolivia", "Bosnia and Herzegovina", "Botswana", "Brazil",
    "Brunei", "Bulgaria", "Burkina Faso", "Burundi", "Côte d'Ivoire", "Cabo Verde", "Cambodia", "Cameroon",
    "Canada", "Central African Republic", "Chad", "Chile", "China", "Colombia", "Comoros", "Congo (Congo-Brazzaville)",
    "Costa Rica", "Croatia", "Cuba", "Cyprus", "Czechia (Czech Republic)", "Democratic Republic of the Congo (Congo-Kinshasa)",
    "Denmark", "Djibouti", "Dominica", "Dominican Republic", "Ecuador", "Egypt", "El Salvador", "Equatorial Guinea",
    "Eritrea", "Estonia", "Eswatini (fmr. Swaziland)", "Ethiopia", "Fiji", "Finland", "France", "Gabon", "Gambia",
    "Georgia", "Germany", "Ghana", "Greece", "Grenada", "Guatemala", "Guinea", "Guinea-Bissau", "Guyana", "Haiti",
    "Holy See", "Honduras", "Hungary", "Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland", "Israel", "Italy",
    "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya", "Kiribati", "Kuwait", "Kyrgyzstan", "Laos", "Latvia",
    "Lebanon", "Lesotho", "Liberia", "Libya", "Liechtenstein", "Lithuania", "Luxembourg", "Madagascar", "Malawi",
    "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands", "Mauritania", "Mauritius", "Mexico", "Micronesia",
    "Moldova", "Monaco", "Mongolia", "Montenegro", "Morocco", "Mozambique", "Myanmar (formerly Burma)", "Namibia",
    "Nauru", "Nepal", "Netherlands", "New Zealand", "Nicaragua", "Niger", "Nigeria", "North Macedonia (formerly Macedonia)",
    "Norway", "Oman", "Pakistan", "Palau", "Palestine State", "Panama", "Papua New Guinea", "Paraguay", "Peru",
    "Philippines", "Poland", "Portugal", "Qatar", "Romania", "Russia", "Rwanda", "Saint Kitts and Nevis", "Saint Lucia",
    "Saint Vincent and the Grenadines", "Samoa", "San Marino", "Sao Tome and Principe", "Saudi Arabia", "Senegal",
    "Serbia", "Seychelles", "Sierra Leone", "Singapore", "Slovakia", "Slovenia", "Solomon Islands", "Somalia", "South Africa",
    "South Korea", "South Sudan", "Spain", "Sri Lanka", "Sudan", "Suriname", "Sweden", "Switzerland", "Syria", "Tajikistan",
    "Tanzania", "Thailand", "Timor-Leste", "Togo", "Tonga", "Trinidad and Tobago", "Tunisia", "Turkey", "Turkmenistan", "Tuvalu",
    "Uganda", "Ukraine", "United Arab Emirates", "United Kingdom", "United States of America", "Uruguay", "Uzbekistan", "Vanuatu",
    "Venezuela", "Vietnam", "Yemen", "Zambia", "Zimbabwe"
]


def fetch_prayer_times(city,country) :
  url = f"http://api.aladhan.com/v1/timingsByCity?city={city}&country={country}&method=3"
  response = requests.get(url)
  response = response.json()
  return(response["data"]["timings"])

def gui_fetch_prayer_times():
  city = city_entry.get()
  country = country_entry.get()
  try :
    country = country.replace(country[0],country[0].upper(),1)
    if country in countries and city in cities_list :
      city = city.replace(city[0],city[0].upper(),1)
      result = fetch_prayer_times(city,country)
      text1=f"Prayer Times in {city} :"
      output.insert(tk.END,text1)
      output.insert(tk.END,"-"*len(text1))
      for prayer,time in result.items():
        output.insert(tk.END,f"{prayer} : {time}")
      output.insert(tk.END,"-"*len(text1))
    else :
      messagebox.showerror("Error","Please Check the City and Country")  
  except : 
    messagebox.showerror("Error","Please Enter a City and a Country")

app = tk.Tk()
app.title("Prayers Fetcher")

custom_font = font.Font(weight="normal",size=10)


frame = ttk.Frame(app,padding=22)
frame.grid(row=0,column=0)

city_label = ttk.Label(frame,text="City : ",font=custom_font)
city_label.grid(row=0,column=0,pady=5)
city_entry = ttk.Entry(frame)
city_entry.grid(row=0,column=1,pady=5)

country_label = ttk.Label(frame,text="Country : ",font=custom_font)
country_label.grid(row=1,column=0,pady=5)
country_entry = ttk.Entry(frame)
country_entry.grid(row=1,column=1,pady=5)

search_button = ttk.Button(frame,text="S E A R C H",command=gui_fetch_prayer_times)
search_button.grid(row=2,column=0,columnspan=2,pady=5)

output = tk.Listbox(frame,height=10,width=30)
output.grid(row=3,column=0,columnspan=2)
output.insert(tk.END," ")
output.insert(tk.END,"                     Welcome  :) ")
output.insert(tk.END,"                 (Scroll for results)")
output.insert(tk.END," ")

style = ttk.Style(app)
style.theme_use('clam')


tk.mainloop()

