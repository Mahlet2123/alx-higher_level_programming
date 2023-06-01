// JavaScript script that adds a <li> element to a list
// when the user clicks on the tag DIV#add_item

$('DIV#add_item').click(function(){
	const newItem = $('<li>Item</li>')
	$('ul.my_list').append(newItem);
});
