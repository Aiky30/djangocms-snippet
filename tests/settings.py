#!/usr/bin/env python
HELPER_SETTINGS = {
    'INSTALLED_APPS': [
        'tests.utils',
        'djangocms_versioning',
        'djangocms_snippet',
    ],
    'CMS_LANGUAGES': {
        1: [{
            'code': 'en',
            'name': 'English',
        }]
    },
    'LANGUAGE_CODE': 'en',
    'ALLOWED_HOSTS': ['localhost'],
    'DJANGOCMS_SNIPPET_VERSIONING_ENABLED': True,
    'DJANGOCMS_SNIPPET_MODERATION_ENABLED': True,
}


def run():
    from app_helper import runner
    runner.cms('djangocms_snippet')


if __name__ == '__main__':
    run()
