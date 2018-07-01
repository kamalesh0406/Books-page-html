
var discover = $('#discover');
var books_display=$('#books');
var query_data;
var url = "https://www.googleapis.com/books/v1/volumes?q=subject:fiction&orderBy=newest&langRestrict=en&key=AIzaSyB75KOXOcgjftFtFcc5OiuXXVpa1QzGSCc"

books_display.on('click','form',function(){
	$.ajax({
		url:'/book',
		data:$(this).serialize(),
		type:'POST',
		success:function(response){
			console.log(response);
		}
	});
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
		var booklabel = "<label>"+book_name+" "+"</label>";
		var bookoptions = "<select id='options'><option>Want To Read</option><option>Currently Reading</option><option>Read</option>"
		var tick = "<input type='button' value='&#10003;'>"
		var addtolib = "<input type='button' class='add' value='Add To Library'>"

		books_display.append("<form method='POST'>"+booklabel+bookoptions+tick+addtolib+"</form>");

	}
	$('li').css('list-style-type','none');
	$('label').css('margin','5px')
	$('.add').css('margin','7px')
	});
});
