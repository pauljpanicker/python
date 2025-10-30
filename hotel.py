from main_teavelist import date_obj
from tracker import info
import json
from datetime import datetime
details=[
  info("paul","i am from kollam","1-10-1910"),
  info ("abi", "i am from tvm", "12-9-1910"),
  info ("vishnu", "i am from jaipur", "16-10-1910"),
]
for info in details:
    date_obj = datetime.strptime(info["date"], "%d-%m-%Y")
    format_data = date_obj.strftime("%B,%d,%Y")
    info["date"] = format_data

json_data = json.dumps(details)
print(json_data)

