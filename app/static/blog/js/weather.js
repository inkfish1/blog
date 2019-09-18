$.ajax({
    type:'GET',
    url:'https://www.tianqiapi.com/api/',
    data:'appid=87116792&appsecret=yT7WUXZt&version=v61',
    dataType:'JSON',
    error:function(){
        alert('获取天气失败，网络错误')
    },
    success:function(res){
        date=res.date
        week=unescape(res.week.replace(/\u/g,"%u"))
        city=unescape(res.city.replace(/\u/g,"%u"))
        weather=unescape(res.wea.replace(/\u/g,"%u"))
        template=unescape(res.tem.replace(/\u/g,"%u"))
        pm25=unescape(res.air_pm25.replace(/\u/g,"%u"))
        tip=unescape(res.air_tips.replace(/\u/g,"%u"))
        addhtml='<p>'+date+'&nbsp;&nbsp'+week+'&nbsp;&nbsp&nbsp;'+city+'</p><p>天气：'+weather+'&nbsp;&nbsp;&nbsp;温度：'+template+'°c&nbsp;&nbsp;&nbsp;&nbsp;pm2.5：'+pm25+'μg/m3</p><p>'+tip+'</p>'
        $('#weather').append(addhtml)
    }


});