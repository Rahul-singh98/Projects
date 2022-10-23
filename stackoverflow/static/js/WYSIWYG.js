function images_upload_handler(blobInfo, success, failure, progress) {
    var xhr, formData;

    xhr = new XMLHttpRequest();
    xhr.withCredentials = true;

    var handler_url = "http://localhost:8000/upload_handle"

    xhr.open('POST', handler_url);   

    xhr.upload.onprogress = function (e) {
        progress(e.loaded / e.total * 100);
    };

    xhr.onload = function () {
        var json;

        //  if error return
        if (xhr.status === 403) {
            failure('HTTP Error: ' + xhr.status, { remove: true });
            return;
        }

        //  if error return
        if (xhr.status < 200 || xhr.status >= 300) {
            failure('HTTP Error: ' + xhr.status);
            return;
        }


        console.log('status 200')

        json = JSON.parse(xhr.responseText);
        if (!json || typeof json.location != 'string') {
            failure('Invalid JSON: ' + xhr.responseText);
            return;
        }

        success(json.location);
    };

    xhr.onerror = function () {
        failure('Image upload failed due to a XHR Transport error. Code: ' + xhr.status);
    };

    formData = new FormData();
    formData.append('file', blobInfo.blob(), blobInfo.filename());
    xhr.send(formData);
};

tinymce.init({
    selector: 'textarea',
    plugins: 'print paste autolink autosave save directionality code image link media charmap hr pagebreak nonbreaking anchor insertdatetime advlist lists noneditable emoticons',
    imagetools_cors_hosts: ['picsum.photos'],
    menubar:"",
    toolbar: 'undo redo | bold codesample template removeformat image| fullscreen  preview | fontselect fontsizeselect styleselect | hr alignleft aligncenter alignright alignjustify | numlist bullist  | italic forecolor backcolor  outdent indent formatselect  | pagebreak | charmap emoticons | insertfile image media link anchor underline strikethrough| ltr rtl',

    toolbar_sticky: true,
    autosave_ask_before_unload: true,
    autosave_interval: '30s',
    autosave_prefix: '{path}{query}-{id}-',
    autosave_restore_when_empty: false,
    autosave_retention: '2m',
    image_advtab: true,

    image_class_list: [
        { title: 's-text-img', value: 's-text-img' },
    ],
    importcss_append: true,

    templates: [
        { title: 'Insert Source Code', description: 'Insert Source Code to Blog with Style : Just add Content and done', content: '<div class="code-ar"><pre><code>Hello World</code></pre></div>' },
    ],

    template_cdate_format: '[Date Created (CDATE): %m/%d/%Y : %H:%M:%S]',
    template_mdate_format: '[Date Modified (MDATE): %m/%d/%Y : %H:%M:%S]',
    height: 200,
    resize: true,
    image_caption: true,
    quickbars_selection_toolbar: 'h1 h2 h3 h4 h5  | quickimage quicktable |',
    quickbars_insert_toolbar: 'quicktable image media codesample templates',
    noneditable_noneditable_class: 'mceNonEditable',
    toolbar_mode: 'sliding',
    contextmenu: 'link image imagetools table templates',
    content_style: 'body { font-family:Helvetica,Arial,sans-serif; font-size:14px }',

    // without images_upload_url set, Upload tab won't show up
    images_upload_url: 'upload.php',

    // override default upload handler to simulate successful upload
    images_upload_handler: images_upload_handler
,

    // content_style: "img { margin: 0 px; }",
      
});
