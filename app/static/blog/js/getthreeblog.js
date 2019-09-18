<script src="{{url_for('static',filename='js/jquery-1.8.0.min.js')}}"></script>

$("document").ready(function(){
    $.ajax({
         url:"{{ url_for('main.getrecent') }}",
         cache:false,
         processData:false,
         contentType:false,
         type:'POST',
        success:function (data) {
             if(data.signal==1){
                $.each(data.posts,function(i,item){
                id =item['id']
                 var addhtml=' <div class="recent-post cf"><a href="/single/?id='+id+'" class="thumb"><img src="data:;base64,'+item['pic']+'" alt="Post" style="height:60px;width:60px" /></a><div class="post-head"><a href="/single/?id='+id+'">'+item['title']+'</a><span class="date">'+item['timestamp']+'</span></div></div>'
                 $('#tiezi').append(addhtml)
                }); 
            }

         }
     })
})