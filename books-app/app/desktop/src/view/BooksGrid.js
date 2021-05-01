Ext.define('BooksApp.view.BooksGrid', {
    extend: 'Ext.grid.Grid',
    requires: [
        'Ext.grid.column.Column',
        'Ext.grid.*',
        'BooksApp.store.Book',
        'Ext.grid.filters.Plugin',
        'Ext.grid.rowedit.Plugin',
        'Ext.grid.plugin.CellEditing',
        'Ext.grid.plugin.Editable',
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
    dockedItems: [{
        xtype: 'toolbar',
        dock: 'top',
        items: [{
            xtype: 'button',
            text: 'Left Button'
        }, {
            xtype: 'button',
            text: 'Right Button'
        }]
    }]

});