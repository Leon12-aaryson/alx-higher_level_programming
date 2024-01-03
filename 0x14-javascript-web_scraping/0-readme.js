#!/usr/bin/node
const { error } = require('console');
const fs = require('fs');

const filename = process.argv[2]
fs.readFile(process.argv[2], "utf8", (err, data) => {
    if(err){
        console.error(err);
        return;
    }
    console.log(data);
})