function CccXBlockInitStudio(runtime,element){
    var elemContainer = $(element);
    elemContainer.find('.action-cancel').click(function(){
    	runtime.notify('cancel',{});
    });
	elemContainer.find('.action-save').click(function() {
        var data = {
            'display_name': $('#cc_edit_display_name').val(),
            //'file_id': $('#youku_edit_file_id').val(),
            'video_id': $('#cc_edit_videoid').val(),
            'width': $('#cc_edit_width').val(),
           // 'height': $('#youku_edit_height').val(),
        };

        runtime.notify('save', {state: 'start'});

        var handlerUrl = runtime.handlerUrl(element, 'save_cc');
        $.post(handlerUrl, JSON.stringify(data)).done(function(response) {
            if (response.result === 'success') {
                runtime.notify('save', {state: 'end'});
                // Reload the whole page :
                // window.location.reload(false);
            } else {
                runtime.notify('error', {msg: response.message})
            }
        });
    });
}