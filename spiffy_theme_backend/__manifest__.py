# -*- coding: utf-8 -*-
# Developed by Bizople Solutions Pvt. Ltd.
# See LICENSE file for full copyright and licensing details
{
    'name': 'Spiffy Backend Theme',
    'category': 'Themes/Backend',
    'version': '15.0.0.4',
    'author': 'Bizople Solutions Pvt. Ltd.',
    'website': 'https://www.bizople.com/',
    'summary': 'The ultimate Odoo Backend theme with the most advanced key features of all time. Get your own personalized view while working on the Backend system with a wide range of choices. Spiffy theme has 3 in 1 Theme Style, Progressive Web App, Fully Responsive for all apps, Configurable Apps Icon, App Drawer with global search, RTL & Multi-Language Support, and many other key features.',
    'description': """ The ultimate Odoo Backend theme with the most advanced key features of all time. Get your own personalized view while working on the Backend system with a wide range of choices. Spiffy theme has 3 in 1 Theme Style, Progressive Web App, Fully Responsive for all apps, Configurable Apps Icon, App Drawer with global search, RTL & Multi-Language Support, and many other key features. """,
    'depends': ['web', 'base_setup', 'portal', 'resource'],
    'data': [
        'security/ir.model.access.csv',
        'data/backend_config_data.xml',
        'data/global_level_config.xml',
        'views/manifest.xml',
        'views/pwa_offline.xml',
        'views/backend_configurator_view.xml',
        'views/backend_configurator_template.xml',
        'views/res_config_setting.xml',
        'views/login_page_style.xml',
        'views/templates_inherit.xml',
        'views/ir_module_view.xml',
        'views/pwa_shortcuts_view.xml',
        'views/menuitems.xml',
    ],
    'demo': [
        'data/spiffy_default_images.xml',
    ],
    'assets': {
        'web.assets_qweb': [
            '/spiffy_theme_backend/static/src/xml/web_inherit.xml',
            '/spiffy_theme_backend/static/src/xml/menu.xml',
            '/spiffy_theme_backend/static/src/xml/bookmark.xml',
            '/spiffy_theme_backend/static/src/xml/base.xml',
            '/spiffy_theme_backend/static/src/xml/controlpanel.xml',
            '/spiffy_theme_backend/static/src/xml/view_button_icons.xml',
        ],
        'web.assets_backend': [
            # scss files
            "/spiffy_theme_backend/static/src/scss/custom_varibles.scss",
            "/spiffy_theme_backend/static/src/scss/font_size.scss",
            "/spiffy_theme_backend/static/src/scss/font_icons.scss",
            "/spiffy_theme_backend/static/src/scss/font-family.scss",

            "/spiffy_theme_backend/static/src/scss/modal.scss",
            "/spiffy_theme_backend/static/src/scss/search_modal.scss",
            "/spiffy_theme_backend/static/src/scss/chat_window.scss",
            "/spiffy_theme_backend/static/src/scss/common_view.scss",
            "/spiffy_theme_backend/static/src/scss/discuss_style.scss",
            "/spiffy_theme_backend/static/src/scss/list_view.scss",
            "/spiffy_theme_backend/static/src/scss/kanban_view.scss",

            "/spiffy_theme_backend/static/src/scss/form_view.scss",
            "/spiffy_theme_backend/static/src/scss/form_chatter.scss",
            "/spiffy_theme_backend/static/src/scss/tree_form_split_view.scss",

            "/spiffy_theme_backend/static/src/scss/activity_view.scss",
            "/spiffy_theme_backend/static/src/scss/pivot_view.scss",
            "/spiffy_theme_backend/static/src/scss/graph_view.scss",
            "/spiffy_theme_backend/static/src/scss/dashboards.scss",
            "/spiffy_theme_backend/static/src/scss/calendear_view.scss",
            "/spiffy_theme_backend/static/src/scss/setting_page.scss",
            "/spiffy_theme_backend/static/src/scss/tab_styles.scss",
            "/spiffy_theme_backend/static/src/scss/popup_styles.scss",
            "/spiffy_theme_backend/static/src/scss/checkbox_styles.scss",
            "/spiffy_theme_backend/static/src/scss/radio_styles.scss",
            "/spiffy_theme_backend/static/src/scss/separator_styles.scss",
            "/spiffy_theme_backend/static/src/scss/search_panel.scss",
            "/spiffy_theme_backend/static/src/scss/loader.scss",
            "/spiffy_theme_backend/static/src/scss/appdrawer.scss",
            "/spiffy_theme_backend/static/src/scss/bookmarks.scss",
            "/spiffy_theme_backend/static/src/scss/controlpannel.scss",
            "/spiffy_theme_backend/static/src/scss/side_menu.scss",
            "/spiffy_theme_backend/static/src/scss/responsive.scss",
            "/spiffy_theme_backend/static/src/scss/notification.scss",
            "/spiffy_theme_backend/static/src/scss/multi_tab.scss",
            "/spiffy_theme_backend/static/src/scss/datetime_pickers.scss",

            # js files
            "/spiffy_theme_backend/static/src/js/color_pallet.js",
            "/spiffy_theme_backend/static/src/js/flip_min.js",
            "/spiffy_theme_backend/static/src/js/menu.js",
            "/spiffy_theme_backend/static/src/js/user_menu.js",
            "/spiffy_theme_backend/static/src/js/apps_menu.js",
            "/spiffy_theme_backend/static/src/js/SwitchCompanyMenu.js",
            "/spiffy_theme_backend/static/src/js/form_view_renderer.js",
            "/spiffy_theme_backend/static/src/js/list_view_renderer.js",
            "/spiffy_theme_backend/static/src/js/SpiffyPageTitle.js",
            "/spiffy_theme_backend/static/src/js/pwebapp.js",
            "/spiffy_theme_backend/static/src/js/iconpack_load.js",
            "/spiffy_theme_backend/static/src/js/responsive.js",
            "/spiffy_theme_backend/static/src/js/action_service.js",
        ],
        'web.assets_frontend': [
            '/spiffy_theme_backend/static/src/scss/loginpage.scss',
        ],
    },
    'live_test_url': 'http://bit.ly/3Oq8T3H',
    'images': [
        'static/description/spiffy_cover.png',
        'static/description/spiffy_screenshot.gif',
    ],
    'sequence': 1,
    'installable': True,
    'application': True,
    'price': 140,
    'license': 'OPL-1',
    'currency': 'EUR',
}
