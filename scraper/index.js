const rp = require('request-promise');
const cheerio = require('cheerio');
const fs = require('fs');

// Parameters
const silver = {
    uri: `https://www.investing.com/commodities/silver-historical-data`,
    transform: function (body) {
      return cheerio.load(body);
    },
    headers: {
      'User-Agent': 'Request-Promise'
    }
};

const gold = {
  uri: `https://www.investing.com/commodities/gold-historical-data`,
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

fetchData = (function(outFile, options) {
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
  // Scrape data save historical gold date and price data in CSV
  fs.truncate("golddateandprice.csv", 0, function(){});
  fetchData("golddateandprice.csv", gold);
  // Scrape data save historical silver date and price data in CSV
  fs.truncate("silverdateandprice.csv", 0, function(){});
  fetchData("silverdateandprice.csv", silver);
});

// Main
generateCSVs();