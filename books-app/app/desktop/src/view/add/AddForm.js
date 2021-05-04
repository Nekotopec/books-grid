Ext.define('KitchenSink.view.forms.Register', {
    extend: 'Ext.Dialog',
    xtype: 'addview',
    controller: 'add',
    closable: true,

    autoSize: true,
    // width: 340,
    // height: 600,
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
            reference: 'formAdd',
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
                    html: 'Add book',
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
                    label: 'Title',
                    name: 'title',
                    placeholder: 'Title',
                    style: {
                        'margin': 'auto'
                    },
                }, {
                    xtype: 'fieldset',
                    title: 'Author',
                    defaultType: 'textfield',
                    margin: '20 0 0',
                    items: [{
                        xtype: 'textfield',
                        allowBlank: false,
                        required: true,
                        width: 280,
                        label: 'First Name',
                        name: 'firstname',
                        placeholder: 'FirstName',
                        style: {
                            'margin': 'auto'
                        },
                    }, {
                        xtype: 'textfield',
                        allowBlank: false,
                        required: true,
                        width: 280,
                        label: 'Last Name',
                        name: 'lastname',
                        placeholder: 'LastName',
                        style: {
                            'margin': 'auto'
                        },
                    }]
                }, {
                    xtype: 'numberfield',
                    allowBlank: false,
                    required: true,
                    width: 280,
                    label: 'Year',
                    name: 'year',
                    placeholder: '1900',
                    style: {
                        'margin': 'auto'
                    },
                }, {
                    xtype: 'numberfield',
                    allowBlank: false,
                    required: true,
                    width: 280,
                    label: 'Number of pages.',
                    name: 'number_of_pages',
                    placeholder: '499',
                    style: {
                        'margin': 'auto'
                    },
                }, {
                    xtype: 'numberfield',
                    allowBlank: false,
                    required: true,
                    width: 280,
                    label: 'Number of books.',
                    name: 'number_of_books',
                    placeholder: '32',
                    style: {
                        'margin': 'auto'
                    },
                }, {
                    xtype: 'button',
                    text: 'Submit',
                    autoSize: true,
                    handler: 'onSubmit',
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