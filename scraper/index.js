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
      console.log($(element).find('td').text());
  });
})
.catch((err) => {
console.log(err);
});