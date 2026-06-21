import os

# Par défaut, on charge l'environnement de développement local
ENV = os.environ.get('DJANGO_ENV', 'dev_local')

if ENV == 'prod':
    from .prod import *
elif ENV == 'dev_local':
    from .dev_local import *