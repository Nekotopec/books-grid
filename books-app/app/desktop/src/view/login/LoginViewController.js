Ext.define('BooksApp.view.login.LoginController', {
    extend: 'Ext.app.ViewController',
    alias: 'controller.login',
    requires: [
       'BooksApp.security.Firewall',
    ],
    onLoginClick: function () {
        var data = this.lookup('formLogin').getValues();
        this.getView().destroy();
        BooksApp.security.Firewall.login(data.username, data.pass).then(function () {
            Ext.Msg.alert('Success', data.message || 'Yoy are logged in.');
        });
    }
});