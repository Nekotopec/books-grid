Ext.define('BooksApp.utils.AddService', {
    singleton: true,
    requires: [
        'BooksApp.model.Book',
        'BooksApp.store.Book'
    ],

    postData: function (data) {
        var deferred = new Ext.Deferred();
        var jsonData = this.buildJson(data);

        Ext.Ajax.request({
            url: '/api/books/',
            method: 'POST',
            jsonData: jsonData,
            success: function (response) {
                Ext.first('mainview').getViewModel().getStore('books').reload()
                deferred.resolve(data, response);
                deferred.reject(data, response);

            },
            failure: function (response) {
                var data = Ext.decode(response.responseText);

                deferred.reject(data, response);
            },

        });

        return deferred.promise;


    },


    buildJson: function (data) {
        return {
            'title': data.title,
            'author': {
                'first_name': data.firstname,
                'last_name': data.lastname
            },
            'year': data.year,
            'number_of_pages': data.number_of_pages,
            'number_of_books': data.number_of_books,
        }
    }
});