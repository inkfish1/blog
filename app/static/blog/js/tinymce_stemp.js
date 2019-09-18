tinymce.init({
    menubar:false,
    statusbar:false,
    height:500,
    width:'100%',
    color_cols:7,
    custom_color:false,
    selector:'#mytextarea',
    plugins:'image,code,hr,insertdatetime,fullscreen',
    toolbar:'image code |forecolor|hr|insertdatetime|fullscreen',
    images_upload_url:"{{url_for('main.upload')}}",
    images_upload_base_path:'/..'
         
})