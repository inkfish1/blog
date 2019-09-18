jinrishici.load(function(result) {
    // 自己的处理逻辑
    content=result.data.content
    dynasty=result.data.origin.dynasty
    author=result.data.origin.author
    title=result.data.origin.title
    addhtml='<p>'+content+'</p><p>------【'+dynasty+'】'+author+'《'+title+'》'
    $('#sentence').append(addhtml)
});