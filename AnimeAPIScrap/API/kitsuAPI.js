var request = require("request");

module.exports = KitsuAPI = () => {
    var options = { method: 'GET',
    url: 'https://kitsu.io/api/edge/anime',
    qs: 
    { 'page[limit]': '20',
        'page[offset]': '0',
        'fields[anime]': 'id,titles' },
    headers: 
    { 'Postman-Token': 'ef15bcb3-3bf1-4e24-9416-90d8d02b65df',
        'cache-control': 'no-cache',
        'Content-Type': 'application/vnd.api+json',
        'Accept': 'application/vnd.api+json' } };

    request(options, function (error, response, body) {
        if (error) throw new Error(error);

        console.log(body)
        return body

    });
}

