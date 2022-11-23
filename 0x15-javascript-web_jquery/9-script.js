/*
 * JavaScript script that fetches from https://fourtonfish.com/hellosalut/?lang=fr and displays the value
 * of hello from that fetch in the HTML tag DIV#hello.
 */
$(document).ready(function(){
	const url = "https://fourtonfish.com/hellosalut/?lang=fr";
	$.get(url, function(data, stat){
		$("DIV#hello").text(data.hello);
	});

});
