/*
 * JavaScript script that fetches and lists the title for all movies by
 * using this URL: https://swapi-api.hbtn.io/api/films/?format=json
 */
const url = "https://swapi-api.hbtn.io/api/films/?format=json";

$.get(url, function(data, stat){
	data_list = data.results;

	for (let val of data_list){
		$("UL#list_movies").append('<li>'+val.title+'</li>')
	}
});
