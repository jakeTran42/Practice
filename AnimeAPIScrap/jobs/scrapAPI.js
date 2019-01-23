var schedule = require('node-schedule');
var fs = require('fs');
var KitsuAPI = require('../API/kitsuAPI')

var hi = JSON.parse(fs.readFileSync('./animeList/animeSearchList.json', 'utf8'))


module.exports = jobs_schedule = () => {

    var rule = new schedule.RecurrenceRule();
    rule.second = 20;
    schedule.scheduleJob(rule, function(){
        console.log('The answer to life, the universe, and everything!');
        console.log(typeof(KitsuAPI()))
        // fs.writeFileSync('./animeList/animeSearchList.json', JSON.stringify(hi) )
    });
}

// module.exports = {

//     var rule = new schedule.RecurrenceRule();
//     rule.minute = 43;

//     job:  schedule.scheduleJob(rule, function(){
//         console.log('The answer to life, the universe, and everything!');
//     })
// }