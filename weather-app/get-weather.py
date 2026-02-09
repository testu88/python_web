import requests
from flask import Flask, render_template

app = Flask(__name__)


url = "https://api-open.data.gov.sg/v2/real-time/api/twenty-four-hr-forecast"
response = requests.get(url)

'''data = [('code', 0), ('data', {'records': [{'date': '2026-02-09', 'updatedTimestamp': '2026-02-09T11:40:54+08:00', 'general': {'temperature': {'low': 24, 'high': 33, 'unit': 'Degrees Celsius'}, 'relativeHumidity': {'low': 55, 'high': 90, 'unit': 'Percentage'}, 'forecast': {'code': 'WD', 'text': 'Windy'}, 'validPeriod': {'start': '2026-02-09T12:00:00+08:00', 'end': '2026-02-10T12:00:00+08:00', 
'text': '12 PM 9 Feb to 12 PM 10 Feb'}, 'wind': {'speed': {'low': 15, 'high': 30}, 'direction': 'NNE'}}, 'periods': [{'timePeriod': {'start': '2026-02-09T12:00:00+08:00', 'end': '2026-02-09T18:00:00+08:00', 'text': 'Midday to 6 pm 09 Feb'}, 'regions': {'west': {'code': 'WD', 'text': 'Windy'}, 'east': {'code': 'WD', 'text': 'Windy'}, 'central': {'code': 'WD', 'text': 'Windy'}, 'south': {'code': 'WD', 'text': 'Windy'},
'north': {'code': 'WD', 'text': 'Windy'}}}, {'timePeriod': {'start': '2026-02-09T18:00:00+08:00', 'end': '2026-02-10T06:00:00+08:00', 'text': '6 pm 09 Feb to 6 am 10 Feb'}, 'regions': {'west': {'code': 'PN', 'text': 'Partly Cloudy (Night)'}, 'east': {'code': 'PN', 'text': 'Partly Cloudy (Night)'}, 'central': {'code': 'PN', 'text': 'Partly Cloudy (Night)'}, 'south': {'code': 'PN', 'text': 'Partly Cloudy (Night)'},
'north': {'code': 'PN', 'text': 'Partly Cloudy (Night)'}}}, {'timePeriod': {'start': '2026-02-10T06:00:00+08:00', 'end': '2026-02-10T12:00:00+08:00', 'text': '6 am to Midday 10 Feb'}, 'regions': {'west': {'code': 'PC', 'text': 'Partly Cloudy (Day)'}, 'east': {'code': 'PC', 'text': 'Partly Cloudy (Day)'}, 'central': {'code': 'PC', 'text': 'Partly Cloudy (Day)'}, 'south': {'code': 'PC', 'text': 'Partly Cloudy (Day)'},                                                                                                                                                                                                   
'north': {'code': 'PC', 'text': 'Partly Cloudy (Day)'}}}], 'timestamp': '2026-02-09T11:30:00+08:00'}]}), ('errorMsg', '')]
'''

#print('The response:')
#print(response.json())
data = response.json()

@app.route('/')
def get_forecast():
    records = data["data"]["records"]
    print(f'Records: {records[0]["general"]}')
    info = records[0]["general"]
    forecast = info["forecast"]["text"]
    low_temperature = info["temperature"]["low"]
    high_temperature = info["temperature"]["high"]
    print(f'Forecast: {forecast}')
    return render_template('forecast.html', forecast = forecast, low_temperature = low_temperature, high_temperature=high_temperature)




if __name__ == '__main__':
    app.run(debug=True)