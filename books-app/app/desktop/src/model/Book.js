Ext.define('BooksApp.model.Book', {
    extend: 'Ext.data.Model',
    requires: [
        'Ext.data.proxy.Rest',
        'Ext.Date'
    ],
    fields: [{
        name: 'id',
        mapping: 'id'
    }, {
        name: 'title',
        mapping: 'title'
    }, {
        name: 'year',
        mapping: 'year'
    }, {
        name: 'number_of_pages',
        mapping: 'number_of_pages'
    
    }, {
        name: 'author_fullname',
        mapping: 'author.full_name'
    }, {
        name: 'author_firstname',
        mapping: 'author.first_name',
        convert: function (value, record) {
            if (record.get('id') !== null) {
                return record.get('author_fullname').split(' ')[0];
            } else {
                return null
            }
        },
    }, {
        name: 'author_lastname',
        mapping: 'author.last_name',
        convert: function (value, record) {
            if (record.get('id') !== null) {
                return record.get('author_fullname').split(' ')[1];
            } else {
                return null
            }
        },
    }, {
        name: 'number_of_books',
        mapping: 'number_of_books'
    }],
    hasOne: [{
        name: 'author',
        model: 'BooksApp.model.Author',
        instanceName: 'author',
        getterName: 'getAuthor',
        setterName: 'setAuthor',
        foreignKey: 'author_id',
        associationKey: 'author',
    }],
    proxy: {

        type: 'rest',
        url: 'http://localhost:8080/api/books/',
        limitParam: 'limit',
        startParam: 'offset',
        noCache: false,
        actionMethods: {
            create: 'POST',
            read: 'GET',
            update: 'PATCH',
            destroy: 'DELETE'
        },
        reader: {
            rootProperty: 'results',
            totalProperty: 'count',
        },
        writer: {
            type: 'json',
            allDataOptions: {
                associated: true
            },
        },

    }
});