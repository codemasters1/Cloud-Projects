// console.log('hello world 👋');
// *************
// process.on('exit', function () {

// })
// *************
// const {EventEmitter} = require('events');
// const EventEmitter = new EventEmitter();

// EventEmitter.on('lunch', () => {

//     console.log('yum 🍲')
// })

// eventEmitter.EventEmitter('lunch');
// *************
// const { readFile, readFileSync } = require('fs'); // sync === blocking, it needs to finish all of its work before any of the other code can run

// const txt = readFileSync('./hello.txt', 'utf-8')

// console.log(txt)

// console.log('do this ASAP')
// *************
// readFile('./hello.txt', 'utf-8', (err, txt) => {
//     console.log(txt)
// })

// console.log('do this ASAP')
// *************
// const { readFile } = require('fs').promises;

// async function hello() {
//     const file = await readFile('./hello.txt', 'utf-8');
// }
// *************
// const myModule = require('./my-modules');

// console.log(myModule)
// *************
const express = require('express');
// *************