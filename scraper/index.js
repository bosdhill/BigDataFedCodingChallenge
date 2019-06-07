const rp = require('request-promise');
const cheerio = require('cheerio');

const options = {
    uri: `https://www.investing.com/commodities/silver-historical-data`,
    transform: function (body) {
      return cheerio.load(body);
    },
    headers: {
      'User-Agent': 'Request-Promise'
    }
  };

rp(options)
.then(($) => {
$('#results_box').find('table.genTbl.closedTbl.historicalTbl tr').each(
  function(index, element) {
      textArray = $(element).text().split('\n');
      if (index != 0)  {
        let date = new Date(textArray[1]).toISOString().split("T")[0];
        let price = textArray[2].replace(/ /g, '');
        console.log("Date: "  + date + " Price: $" + price);
      }
  });
})
.catch((err) => {
console.log(err);
});