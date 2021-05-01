Ext.define('BooksApp.model.Author', {
    extend: 'Ext.data.Model',
    fields: [{
        name: 'id',
        mapping: 'author.id',

    }, {
        name: 'first_name',
        mapping: "author.first_name",
        convert: function (value, record) {
            return record.get('full_name').split(' ')[0];
        },
    }, {
        name: 'last_name',
        mapping: 'author.last_name',
        convert: function (value, record) {
            return record.get('full_name').split(' ')[1];
        },
    }, {
        name: 'full_name',
        mapping: 'author.full_name',
    }]
});