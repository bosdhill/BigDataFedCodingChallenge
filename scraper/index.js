const rp = require('request-promise');
const cheerio = require('cheerio');

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

fetchData = (function(options) {
  rp(options)
  .then(($) => {
    $('#results_box').find('table.genTbl.closedTbl.historicalTbl tr').each(
      function(index, element) {
          textArray = $(element).text().split('\n');
          if (index != 0)  {
            let date = toISOStr(textArray[1]);
            let price = textArray[2].replace(/ /g, '');
            console.log("Date: "  + date + " Price: $" + price);
          }
      });
  })
  .catch((err) => {
  console.log(err);
  });
});

// Scrape data from URLs
fetchData(silver);
fetchData(gold);

