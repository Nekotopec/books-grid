Ext.define('BooksApp.view.main.MainView', {
    extend: 'Ext.Container',
    xtype: 'mainview',
    controller: 'mainviewcontroller',
    requires: [
        'BooksApp.view.main.MainViewController',
        'BooksApp.view.main.MainViewModel',
        'BooksApp.view.BooksGrid',
        'BooksApp.security.Firewall'
    ],
    viewModel: {
        type: 'mainviewmodel'
    },
    items: [
        {
            title: 'Books',
            xtype: 'booksgrid',
            reference: 'books-grid',
            bind: {
                store: '{books}'
            }
        },
        {
            xtype: 'toolbar',
            docked: 'top',
            ui: 'transparent',
            padding: '5 8',
            layout: {
                type: 'hbox',
                align: 'stretch'
            },
            defaults: {
                margin: '0 10 0 0',
                shadow: 'true',
                ui: 'action'
            },
            items: [{
                text: 'Add',
                iconCls: 'x-fa fa-plus',
                handler: 'onAddData'
            }, {
                text: 'Delete',
                iconCls: 'x-fa fa-minus',
                handler: 'onDelete'
            }, {
                xtype: 'spacer'
            }, {
                text: 'Login',
                iconCls: 'x-fa fa-user',
                handler: 'onLogin',
                reference: 'loginButton',
                listeners: {
                    loggedIn: function () {
                        if (BooksApp.security.Firewall.isLoggedIn()) {
                            var loginButton = this.lookup('loginButton');
                            loginButton.setText('Logout');
                            loginButton.setHandler('onLogout');
                        }
                    }
                }
            },
            ]

        }],
})
