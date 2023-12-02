from english.englishTrcp import data

# from hindiTrcp import data
results = data['response']['results']
from pprint import pprint

for i in range(1):
    result = results[i]
    print(result['alternatives'][0]['transcript'])
    print(result['alternatives'][0])
    print()
    print()
    pprint(result['alternatives'][0]['words'])
