
var discover = $('#discover');
var books_display=$('#books');
var query_data;
var url = "https://www.googleapis.com/books/v1/volumes?q=subject:fiction&orderBy=newest&langRestrict=en&key=AIzaSyB75KOXOcgjftFtFcc5OiuXXVpa1QzGSCc"

$('ul').on('click','button',function(){
	console.log($(this).siblings('label').text())
	data = {'name':$(this).siblings('label').text()}
	$.post('/book',data)
});

discover.on('click',function(){
	$.getJSON(url,function(data){
	for(var i=0;i<10;i++){
		var book_loc = data.items[i]
		var book_name = book_loc.volumeInfo.title
		var author = data.items[i].volumeInfo.authors
		var authors=''
		for(var j=0;j<author.length;j++){
			authors+=author;
		}
		var booklabel = "<label name='book' value='"+book_name+"'>"+book_name+" "+"</label>";
		var bookoptions = "<select id='options' name='task'><option>Want To Read</option><option>Currently Reading</option><option>Read</option>"
		//var tick = "<button name='doing'> '&#10003;' </button>"
		var addtolib = "<button name='add' value='addtolib'>Add To Library</button>"
		console.log(addtolib)
		books_display.append("<li>"+booklabel+bookoptions+addtolib+"</li>");

	}
	$('li').css('list-style-type','none');
	$('label').css('margin','5px')
	$('.add').css('margin','7px')
	});
});
