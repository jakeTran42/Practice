// index.js
const express = require("express");
const fs = require("fs");
var app = express();
var job = require('./jobs/scrapAPI')


job()

app.listen(process.env.PORT || 3000, function () {
    console.log('App listening on port 3000!')
})