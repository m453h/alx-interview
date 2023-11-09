#!/usr/bin/node

const request = require('request');
const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

request(url, function (error, response) {
  if (error) {
    console.log(error);
  } else {
    if (response.statusCode === 200) {
      try {
        const movie = JSON.parse(response.body);
        const characters = movie.characters;
        for (const character of characters) {
          request(character, function (error, response) {
            if (error) {
              console.log(error);
            } else {
              if (response.statusCode === 200) {
                try {
                  const character = JSON.parse(response.body);
                  console.log(character.name);
                } catch (parseError) {
                  console.error(parseError);
                }
              } else {
                console.log(response.statusCode);
              }
            }
          });
        }
      } catch (parseError) {
        console.error(parseError);
      }
    } else {
      console.log(response.statusCode);
    }
  }
});
