from split_settings.tools import include


base_settings = [
    'user_settings.py',
    'apps_middleware.py',
    'dir.py',
    'password_val.py',
    'Internationalization.py',
    'Internationalization.py',
    'rest_framework.py',
]

include(*base_settings)
