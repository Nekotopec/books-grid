Ext.define('BooksApp.view.main.MainViewModel', {
    extend: 'Ext.app.ViewModel',
    alias: 'viewmodel.mainviewmodel',
    requires: [
        'BooksApp.model.Book'
    ],
    data: {
        clickTime: Date.now()
    },
    stores: {
        books: {
            type: 'book',
            // extend: 'Ext.data.virtual.Store',
            // model: 'BooksApp.model.Book',
            // autoLoad: true,
            // autoSync: true,
            // sorters: ['title', 'author_full_name'],
        }

    }
});
