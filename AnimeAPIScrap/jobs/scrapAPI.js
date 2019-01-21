var schedule = require('node-schedule');


module.exports = jobs_schedule = () => {
    var rule = new schedule.RecurrenceRule();
    rule.second = 45;

    schedule.scheduleJob(rule, function(){
        console.log('The answer to life, the universe, and everything!');
    });
}

// module.exports = {

//     var rule = new schedule.RecurrenceRule();
//     rule.minute = 43;

//     job:  schedule.scheduleJob(rule, function(){
//         console.log('The answer to life, the universe, and everything!');
//     })
// }