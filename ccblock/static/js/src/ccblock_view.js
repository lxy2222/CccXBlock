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
                user_id = result.user_id;
                height = result.height;
                //height = result.height;
                show_player(user_id,video_id);
               }

    });
}
function show_player(user_id,video_id){
    var swfobj=new SWFObject('http://union.bokecc.com/flash/player.swf', 'playerswf', '800', '450', '8');
    swfobj.addVariable("user_id",user_id);
    swfobj.addVariable("video_id",video_id);
    swfobj.addVariable（"mode","api");
    swfobj.addVariable("autostart","false");
    swfobj.addVariable("jscontrol","true");
    swfobj.addParam('allowFullscreen','true');
    swfobj.addParam('allowScriptAccess','always');
    swfobj.addParam('wmode','transparent');
    swfobj.write('ccplayer');
}
   