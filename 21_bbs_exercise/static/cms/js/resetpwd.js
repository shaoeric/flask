$(function () {

    $('#submit').click(function (event) {
        event.preventDefault();//为了阻止按钮的默认提交表单事件
        var oldpwdE = $('input[name=oldpwd]');
        var newpwdE = $('input[name=newpwd]');
        var newpwd2E = $('input[name=newpwd2]');

        var oldpwd = oldpwdE.val();
        var newpwd = newpwdE.val();
        var newpwd2 = newpwd2E.val();

        //要在模板meta标签中渲染一个csrf_token
        //在ajax请求头部中设置x-csrftoken
        //调用static common zlajax.js
        zlajax.post({
            'url': '/cms/resetpwd/',
            'data':{
                'oldpwd': oldpwd,
                'newpwd': newpwd,
                'newpwd2': newpwd2
            },
            'success': function (data) {
                if(data['code'] == 200){
                    xtalert.alertSuccessToast("密码修改成功");
                    oldpwdE.val('');
                    newpwdE.val('');
                    newpwd2E.val('');

                }else{
                    var message = data['message'];
                    xtalert.alertInfo(message);
                }
            },
            'fail': function (error) {
                xtalert.alertNetworkError();
            }
        });
    });
});