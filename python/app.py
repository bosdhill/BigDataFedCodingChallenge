from flask import Flask, jsonify, request

# Globals and Constants
app = Flask(__name__)
GOLD_DATA_PATH = "data/golddateandprice.csv"
SILVER_DATA_PATH = "data/silverdateandprice.csv"

# Methods
# Computes E(X ^ power)
def compute_mean(prices):
    return sum(float(price) for price in prices) / len(prices)

# Computes E(X^2) - [E(X)]^2
def compute_variance(mean, prices):
    return sum((float(price) - mean) ** 2 for price in prices) / len(prices)

# Reads prices from file at path in date range of startDate to endDate
def fetch_data(path, startDate, endDate):
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
            data = fetch_data(GOLD_DATA_PATH, start_date, end_date)
        if commodity_type == "silver":
            data = fetch_data(SILVER_DATA_PATH, start_date, end_date)
        prices = data.values()
        mean = compute_mean(prices)
        variance = compute_variance(mean, prices)
        return jsonify({"data": data, "mean" : round(mean, 2), "variance" : round(variance, 2)})
    except:
        return jsonify({"data": {}, "mean" : "null", "variance" : "null"})

# Main
if __name__ == '__main__':
    app.run(debug=True, port=8080)