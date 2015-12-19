/* Javascript for CccXBlock. */
function CccXBlockInitView（runtime,element){
    get_params(runtime,element);
    console.log("mytest");

}
function get_params(runtime,element){

    $.ajax({
        type:"POST"
        url: runtime.handlerUrl(element, 'get_params'),
        data: JSON.stringify({a: 'a'}),
        success: function(result) {
                console.log(result);
                video_id = result.video_id;
                //app_id = result.app_id;
                width = result.width;
                //height = result.height;
                //
               }

    });
}

   