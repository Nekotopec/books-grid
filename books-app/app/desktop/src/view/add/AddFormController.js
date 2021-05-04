Ext.define('BooksApp.view.add.AddFormController', {
    extend: 'Ext.app.ViewController',
    alias: 'controller.add',
    requires: [
       'BooksApp.utils.AddService'
    ],
    onSubmit: function () {
        var data = this.lookup('formAdd').getValues();
        this.getView().destroy();
        BooksApp.utils.AddService.postData(data).then(function () {
            Ext.Msg.alert('Success', data.message || 'Book has been added.');
        });
    }
});