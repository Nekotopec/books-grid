Ext.define('BooksApp.view.BooksGrid', {
    extend: 'Ext.grid.Grid',
    requires: [
        'Ext.grid.column.Column',
        'Ext.grid.*',
        'BooksApp.store.Book',
        'Ext.grid.rowedit.Plugin',
    ],
    xtype: 'booksgrid',
    cls: 'books-grid',
    // store: "bookStore",
    scrollable: true,
    height: '100%',
    width: '100%',
    bufferSize: 50,
    plugins: {
        rowedit: {
            // selectOnEdit: true
            autoConfirm: false
        },
        pagingtoolbar: true,


    },

    columns: [{
        text: 'Book title',
        dataIndex: 'title',
        editable: true,
        flex: 1,
    }, {
        text: 'Author',
        dataIndex: 'author_fullname',
        editable: true,
        flex: 1,
    }, {
        text: 'Release year',
        dataIndex: 'year',
        type: 'int',
        editable: true,
        flex: .4,
        editor: {
            xtype: 'numberfield',
            required: true,
        },
    }, {
        text: 'Number of pages',
        dataIndex: 'number_of_pages',
        editable: true,
        flex: .4,
        editor: {
            xtype: 'numberfield',
            required: true,
        },

    }, {
        text: 'Number of books',
        dataIndex: 'number_of_books',
        editable: true,
        type: 'int',
        flex: .4,
        editor: {
            xtype: 'numberfield',
            required: true,
        },

    }],
    bbar: {
        xtype: 'pagingtoolbar',
        displayInfo: true
    },

});