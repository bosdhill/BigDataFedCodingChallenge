const rp = require('request-promise');
const cheerio = require('cheerio');
const fs = require('fs');

// Constants
GOLD_DATA_PATH = "data/golddateandprice.csv"
SILVER_DATA_PATH = "data/silverdateandprice.csv"
SILVER_DATA_URL = `https://www.investing.com/commodities/silver-historical-data`
GOLD_DATA_URL = `https://www.investing.com/commodities/gold-historical-data`

const silver = {
    uri: SILVER_DATA_URL,
    transform: function (body) {
      return cheerio.load(body);
    },
    headers: {
      'User-Agent': 'Request-Promise'
    }
};

const gold = {
  uri: GOLD_DATA_URL,
  transform: function (body) {
    return cheerio.load(body);
  },
  headers: {
    'User-Agent': 'Request-Promise'
  }
};

// Methods
toISOStr = (function(str) {
  return new Date(new Date(new Date(str)
            .toISOString().split("T")[0]) - 1)
            .toISOString().split("T")[0];
});

scrapeAndWriteData = (function(outFile, options) {
  rp(options)
  .then(($) => {
    $('#results_box').find('table.genTbl.closedTbl.historicalTbl tr').each(
      function(index, element) {
          textArray = $(element).text().split('\n');
          if (index != 0)  {
            let date = toISOStr(textArray[1]);
            let price = textArray[2].replace(/ /g, '').replace(/,/g, '');
            fs.appendFile(outFile, date + "," + price + "\n", function (err) {
              if (err) throw err;
            });
          }
      });
  })
  .catch((err) => {
  console.log(err);
  });
});

generateCSVs = (function() {
  fs.truncate(GOLD_DATA_PATH, 0, function(){});
  scrapeAndWriteData(GOLD_DATA_PATH, gold);
  fs.truncate(SILVER_DATA_PATH, 0, function(){});
  scrapeAndWriteData(SILVER_DATA_PATH, silver);
});

// Main
generateCSVs();