Ext.define('BooksApp.security.Firewall', {
    singleton: true,
    requires: [
        'BooksApp.security.TokenStorage'
    ],

    isLoggedIn: function () {
        return null !== BooksApp.security.TokenStorage.retrieve();
    },

    login: function (username, password) {
        var deferred = new Ext.Deferred();

        Ext.Ajax.request({
            url: '/api/token-auth/',
            method: 'POST',
            jsonData: {
                'username': username,
                'password': password
            },

            success: function (response) {
                var data = Ext.decode(response.responseText);
                if (data.token) {
                    BooksApp.security.TokenStorage.save(data.token);

                    deferred.resolve(data, response);
                } else {
                    deferred.reject(data, response);
                }
            },

            failure: function (response) {
                var data = Ext.decode(response.responseText);

                BooksApp.security.TokenStorage.clear();

                deferred.reject(data, response);
            }
        });
        return deferred.promise;
    },

    logout: function () {
        var deferred = new Ext.Deferred();
        BooksApp.security.TokenStorage.clear();
        deferred.resolve(true);
        return deferred.promise;
    }

}, function () {
    Ext.Ajax.on('beforerequest', function (conn, options) {
        if (BooksApp.security.Firewall.isLoggedIn()) {

            options.headers = options.headers || {};
            options.headers['Authorization'] = 'Token ' + BooksApp.security.TokenStorage.retrieve();
        }
    });
});