Ext.define('BooksApp.view.main.MainViewController', {
    extend: 'Ext.app.ViewController',
    alias: 'controller.mainviewcontroller',
    onButtonClick: function (button) {
        this.lookupReference('df').setValue(Date.now())
    },
    onAddData: function () {
        var grid = this.lookup('books-grid');
        var store = grid.getStore()
        var rec = new BooksApp.model.Book(),
            rowEditing = grid.findPlugin('rowediting');

        store.insert(0, rec);
        rowEditing.startEdit(rec, 0);
    },

    onDelete: function () {
        var grid = this.lookup('books-grid');
        var records = grid.getSelections();
        console.log(records)
        if (records.length) {
            Ext.Msg.confirm('Confirm Delete',
                '<h3>Are you sure you want to delete selected records?',
                function (choice) {
                    if (choice === 'yes') {
                        grid.getStore().remove(records);
                    }
                });
        } else {
            Ext.Msg.alert('Deletion',
                'There are no selected records in the grid.')

        }
    },



})
