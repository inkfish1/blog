$("document").ready(function(){
    $.ajax({
         url:"{{ url_for('main.getcategory') }}",
         cache:false,
         processData:false,
         contentType:false,
         type:'POST',
        success:function (data) {
             if(data.signal==1){
             $.each(data.category,function(i,item){
             var addhtml='<li class="cat-item"><a href="/categorylist/?id='+item['id']+'">'+item['name']+'('+item['length']+')'+'</a></li>'
             $('#kind').append(addhtml)
             });
              
            }

         }
     })
})