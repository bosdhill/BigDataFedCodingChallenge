from flask import Flask, jsonify, request

# Globals and Constants
app = Flask(__name__)
GOLD_DATA_PATH = "data/golddateandprice.csv"
SILVER_DATA_PATH = "data/silverdateandprice.csv"

# Methods
# Computes E(X ^ power)
def computeMean(data, power):
    x = 0.0
    n = 0
    for _, price in data.items():
        x += float(price) ** power
        n += 1
    return x / n

# Computes E(X^2) - [E(X)]^2
def computeVariance(mean, data):
    return computeMean(data, 2) - mean * mean

# Fetchs prices from file at path in date range of startDate to endDate
def fetchData(path, startDate, endDate):
    data = {}
    fp = open(path, "r")
    for _, line in enumerate(fp):
        values = line.split(",")
        date = values[0]
        price = values[1][:-1]
        if date >= startDate and date <= endDate:
            data[date] = price
    fp.close()
    return data

# API function
@app.route('/commodity', methods=['GET'])
def commodity():
    try:
        start_date = request.args.get("start_date")
        end_date = request.args.get("end_date")
        commodity_type = request.args.get("commodity_type")
        if commodity_type == "gold":
            data = fetchData(GOLD_DATA_PATH, start_date, end_date)
        if commodity_type == "silver":
            data = fetchData(SILVER_DATA_PATH, start_date, end_date)
        mean = computeMean(data, 1)
        variance = computeVariance(mean, data)
        return jsonify({"data": data, "mean" : round(mean, 2), "variance" : round(variance, 2)})
    except:
        return jsonify({"data": {}, "mean" : "null", "variance" : "null"})

# Main
if __name__ == '__main__':
    app.run(debug=True, port=8080)