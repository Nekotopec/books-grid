Ext.define('BooksApp.view.login.LoginView', {
    extend: 'Ext.Dialog',
    xtype: 'loginview',
    controller: 'login',
    closable: true,

    autoSize: true,
    width: 340,
    height: 544,
    layout: {
        type: 'vbox',
        pack: Ext.platformTags.phone && window.orientation === 0 ? 'center' : undefined,
        align: 'middle'
    },
    scrollable: 'y',
    // setting the background of the container
    style: 'background-color: var(--base-color)',

    items: [
        {
            xtype: 'formpanel',
            height: 514,
            width: 340,
            reference: 'formLogin',
            layout: {
                type: 'vbox',
                align: 'middle'
            },
            bodyPadding: 30,
            items: [
                {
                    xtype: 'component',
                    width: 280,
                    height: 27,
                    html: 'Login Into Admin Account',
                    style: {
                        'font-size': '20px',
                        'text-align': 'center',
                        'margin': 'auto'
                    }
                },
                {
                    xtype: 'textfield',
                    allowBlank: false,
                    required: true,
                    width: 280,
                    label: 'Username',
                    name: 'username',
                    placeholder: 'Username',
                    errorTarget: 'qtip',
                    style: {
                        'margin': 'auto'
                    },
                    responsiveConfig: {
                        'desktop': {
                            errorTarget: 'side'
                        }
                    }
                },
                {
                    xtype: 'passwordfield',
                    revealable: true,
                    required: true,
                    width: 280,
                    label: 'Password',
                    name: 'pass',
                    placeholder: 'password',
                    errorTarget: 'qtip',
                    style: {
                        'margin': 'auto'
                    },
                    responsiveConfig: {
                        'desktop': {
                            errorTarget: 'side'
                        }
                    }
                }, {
                    xtype: 'button',
                    text: 'LOG IN',
                    autoSize: true,
                    handler: 'onLoginClick',
                    width: 280,
                    ui: 'action',
                    style: {
                        'text-align': 'center',
                        'letter-spacing': '1.25px',
                        'font-size': '14px',
                        'margin': 'auto'
                    }
                },
            ]
        },
    ]
});