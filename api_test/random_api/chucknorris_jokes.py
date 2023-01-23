import requests

url = "https://api.chucknorris.io/jokes/random"

result = requests.get(url)
print("Status code ==> " + str(result.status_code))
assert 200 == result.status_code
if result.status_code == 200:
    print("Тест успешно пройден, получена новая шутка!!")
else:
    print("Тест не пройден :-(, FAILED!!")
result.encoding = 'utf-8'
print(result.text)
