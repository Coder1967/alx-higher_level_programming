#!/usr/bin/node
/*
 * Write a JavaScript script that fetches the character
 * name from this URL: https://swapi-api.hbtn.io/api/people/5/?format=json
 */
const url = "https://swapi-api.hbtn.io/api/people/5/?format=json";

$.get(url, function(data, stat){
	$("DIV#character").text(data.name);

});
