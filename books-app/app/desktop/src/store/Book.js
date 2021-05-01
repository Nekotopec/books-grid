Ext.define('BooksApp.store.Book', {
    extend: 'Ext.data.Store',
    storeId: 'bookStore',
    model: 'BooksApp.model.Book',
    alias: 'store.book',
    autoLoad: true,
    autoSync: true,
    pageSize: 14,
    sorters: ['id',],
});

