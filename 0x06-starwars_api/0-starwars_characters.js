#!/usr/bin/node
/**
  prints all characters of a Star Wars movie
*/

const commandLineArgs = process.argv.slice(2);
const requestModule = require('request');
const filmUrl = 'https://swapi-api.hbtn.io/api/films/' + commandLineArgs[0];

requestModule(filmUrl, async function (error, response, body) {
  if (!error) {
    const filmData = JSON.parse(body);
    const charactersEndpoints = filmData.characters;

    for (const characterEndpoint of charactersEndpoints) {
      await new Promise(function (resolve, reject) {
        requestModule(characterEndpoint, function (error, response, body) {
          if (!error) {
            const characterData = JSON.parse(body);
            console.log(characterData.name);
            resolve();
          }
        });
      });
    }
  }
});
