
var discover = $('#discover');
var books_display=$('#books');
var my_library = $('#library');
var activity_display = $('#activity');
var search = $('#search')
var query_data;
var url = "https://www.googleapis.com/books/v1/volumes?q=subject:fiction&orderBy=newest&langRestrict=en&key=AIzaSyB75KOXOcgjftFtFcc5OiuXXVpa1QzGSCc"

$('ul').on('click','button',function(){
	
	if($(this).text()=='Add To Library'){
		data = {'id':$(this).siblings('.id').val(),'name':$(this).siblings('.bookname').text(),'activity':'lib','author':$(this).siblings('.authorname').text()}
		$.post('/book',data,function(response){
			console.log(response);
		})
	}
	else{
		data = {'id':$(this).siblings('.id').val(),'activity':$(this).siblings('select').val(),'name':$(this).siblings('label').text(),'author':$(this).siblings('.authorname').text()}
		$.post('/book',data,function(response){

			if (JSON.parse(response).status == "ok"){
				console.log("In here")
				$(this).css('background','green');
			}
		});
	}

});
search.on('keypress',function(event){
	var parameter =$(this).siblings('select').val()
	console.log(parameter)
	if (event.keyCode==13){
		books_display.empty();
		if (parameter=='author'){
			var para = "inauthor:"
		}
		if (parameter=='title'){
			var para = "intitle:"
		}
		if (parameter=='isbn'){
			var para = "isbn:"
		}
		var new_url = "https://www.googleapis.com/books/v1/volumes?q="+para+$(this).val()+"&orderBy=newest&langRestrict=en&key=AIzaSyB75KOXOcgjftFtFcc5OiuXXVpa1QzGSCc"
		$.getJSON(new_url,function(data){
			books_display.empty();
			for(var i=0;i<10;i++){
				var book_loc = data.items[i]
				var book_name = book_loc.volumeInfo.title
				var author = data.items[i].volumeInfo.authors
				var authors=''

				for(var j=0;j<author.length;j++){
					authors+=author;
				}
				var booklabel = "<label class='bookname'>"+book_name+" "+"</label>";
				var bylabel = "<label>By:</label>"
				var authorname = "<label class='authorname'>"+authors+"</label>"
				var hidden = "<input type='hidden' class='id' value='"+data.items[i].id+"'>"
				var bookoptions = "<select id='options' name='task'><option value='want'>Want To Read</option><option value='reading'>Currently Reading</option><option value='read'>Read</option></select>";
				var tick = "<button> &#10003; </button>"
				var addtolib = "<button>Add To Library</button>";
				var rating = "<label>Rating</label>";
				var rating_input = "<input type='number' class='rating'>"
				var fav = "<label>Favourite</label>"
				var favourite = "<input type='checkbox' class='fav'>"
				books_display.append("<li>"+booklabel+bylabel+authorname+hidden+bookoptions+tick+addtolib+rating+rating_input+favourite+"</li>");

			}
			$('li').css('list-style-type','none');
			$('label').css('margin','5px');
			$('button').css('margin','5px');
		});
	}
})
activity_display.on('click',function(){
	books_display.empty()
	$.post('/activity',function(response){
		console.log(response);
		data = JSON.parse(response)
		if (data.want.length != 0){
			for(i=0;i<data.want.length;i++){
				var li = "<li>You want to read "+data.want[i][0]+" By: "+data.want[i][1]
				books_display.append(li)
			}
		}
		if (data.isreading.length != 0){
			for(i=0;i<data.isreading.length;i++){
				var li = "<li>You are currently reading "+data.isreading[i][0]+" By: "+data.isreading[i][1]
				books_display.append(li)
			}
		}
		if (data.read.length != 0){
			for(i=0;i<data.read.length;i++){
				var li = "<li>You have read "+data.read[i][0]+" By: "+data.read[i][1]
				books_display.append(li)
			}
		}
		if (data.favourite.length != 0){
			for(i=0;i<data.favourite.length;i++){
				var li = "<li>You have marked "+data.favourite[i][0]+" By: "+data.favourite[i][1]+"as favourite"
				books_display.append(li)
			}
		}
		if (data.rating.length != 0){
			for(i=0;i<data.rating.length;i++){
				var li = "<li>You have rated "+data.rating[i][0]+" By: "+data.rating[i][1]+" as "+data.rating[i][2]+" stars "
				books_display.append(li)
			}
		}
	});
})

$('ul').on('click','.fav',function(){
	data = {'id':$(this).siblings('.id').val(),'name':$(this).siblings('.bookname').text(),'activity':'fav','author':$(this).siblings('.authorname').text()}
	$.post('/book',data,function(response){
		console.log(response);
	})
})
$('ul').on('keypress','.rating',function(event){
	if (event.keyCode == 13){
		console.log(event.keyCode)
		data = {'id':$(this).siblings('.id').val(),'name':$(this).siblings('.bookname').text(),'activity':'rating','author':$(this).siblings('.authorname').text(),rating:$(this).val()};
		$.post('/book',data,function(response){
			console.log(response);
		})
	}
})
my_library.on('click',function(){
	books_display.empty();
	$.post('/library',function(response){
		var k=0;
		console.log(response)
		var response = JSON.parse(response)
		for(k=0;k<response.length;k++){
			console.log(typeof(response))
			console.log(response[k][1])
			var booklabel = "<label class='bookname'>"+response[k][1]+" "+"</label>";
			var authorname = "<label class='authorname'> BY:"+response[k][2]+"</label>";
			console.log(booklabel)
			books_display.append("<li>"+booklabel+authorname+"</li>");
		}
	})
})
discover.on('click',function(){
	$.getJSON(url,function(data){
	books_display.empty();
	for(var i=0;i<10;i++){
		var book_loc = data.items[i]
		var book_name = book_loc.volumeInfo.title
		var author = data.items[i].volumeInfo.authors
		var authors=''

		for(var j=0;j<author.length;j++){
			authors+=author;
		}
		var booklabel = "<label class='bookname'>"+book_name+" "+"</label>";
		var bylabel = "<label>By:</label>"
		var authorname = "<label class='authorname'>"+authors+"</label>"
		var hidden = "<input type='hidden' class='id' value='"+data.items[i].id+"'>"
		var bookoptions = "<select id='options' name='task'><option value='want'>Want To Read</option><option value='reading'>Currently Reading</option><option value='read'>Read</option></select>";
		var tick = "<button> &#10003; </button>"
		var addtolib = "<button>Add To Library</button>";
		var rating = "<label>Rating</label>";
		var rating_input = "<input type='number' class='rating'>"
		var fav = "<label>Favourite</label>"
		var favourite = "<input type='checkbox' class='fav'>"
		books_display.append("<li>"+booklabel+bylabel+authorname+hidden+bookoptions+tick+addtolib+rating+rating_input+fav+favourite+"</li>");

	}
	$('li').css('list-style-type','none');
	$('label').css('margin','5px');
	$('button').css('margin','5px');
	});
});
