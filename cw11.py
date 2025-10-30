from travel_blog import trip_data
from datetime import datetime
import json
trips=[
    trip_data("Paul","10-2-2023","tokyo is good"),
    trip_data("sith", "11-2-2023", "japan is cultured"),
    trip_data("aromal", "12-2-2023", "china is disciplined")
]
for trip in trips:
    date_obj=datetime.strptime(trip["date"],"%d-%m-%Y")
    format_data=date_obj.strftime("%B,%d,%Y")
    trip["date"]=format_data

json_data = json.dumps(trips, indent=4)
print(json_data)
