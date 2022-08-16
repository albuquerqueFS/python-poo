employees = { 
    "chef": "Amy",
    "ceo": "Jason"
}

print(employees)
print(employees["chef"])

employees["waiter"] = "Mike"
print(employees)

print(employees["ceo"].upper())

mydict = { "OUTER": { "INNER": 100 }}
print(mydict["OUTER"])

stock_prices = { "GOOGL": [200, 210, 220], "GME": [20,100,300]}
print(stock_prices)
print(stock_prices.items())