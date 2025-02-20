1. Please write a program to fetch the historical prices and dates of gold and silver from these 2 URLs:

* ```https://www.investing.com/commodities/gold-historical-data```

* ```https://www.investing.com/commodities/silver-historical-data```

  and store them locally (in a csv file, or other file or database, as you see fit).
  Please extract the Date and Price fields only from the current static page.

2. Please write a second program that will start an API web-service on port 8080 (use flask) that will return the stored data

  * Create an endpoint that will accept HTTP GET with following arguments, and returning a json time series, mean and variance computed over the specified period:

    * start_date - required (iso format like 2017-05-10)

    * end_date - required (iso format like 2017-05-22)

    * commodity_type - required (gold, silver)

    example of calling by using curl:

    ```curl 'http://127.0.0.1:8080/commodity?start_date=2017-05-10&end_date=2017-05-22&commodity_type=gold'```

    example of output data:
    ```javascript
    {
      "data": {
        "2017-05-10": 1253.06,
        "2017-05-11": 1280.46,
        "2017-05-12": 1278.21
      }
      "mean": 1270.57,
      "variance": 231.39
    }
    ```
