{
    "name": "G2P Service Provider Portal",
    "category": "G2P",
    "version": "15.0.1.1.0",
    "sequence": 1,
    "author": "OpenG2P",
    "website": "https://openg2p.org",
    "license": "Other OSI approved licence",
    "development_status": "Alpha",
    "depends": [
        "g2p_self_service_portal",
        "g2p_program_reimbursement",
    ],
    "data": [
        "views/auth_oauth_provider.xml",
        "views/aboutus.xml",
        "views/base.xml",
        "views/contactus.xml",
        "views/form_page.xml",
        "views/form_submitted.xml",
        "views/login.xml",
        "views/myprofile.xml",
        "views/others.xml",
        "views/reimbursement.xml",
    ],
    "assets": {
        "web.assets_backend": [],
        "web.assets_qweb": [],
        "web.assets_frontend": [
            "g2p_service_provider_portal/static/src/js/form_action.js",
            "g2p_service_provider_portal/static/src/js/multiple_file_upload.js",
            "g2p_service_provider_portal/static/src/js/table_sr_no.js",
            "g2p_service_provider_portal/static/src/js/pagination.js",
        ],
        "web.assets_common": [],
    },
    "demo": [],
    "images": [],
    "application": True,
    "installable": True,
    "auto_install": False,
}
