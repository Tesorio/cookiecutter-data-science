# -*- coding: utf-8 -*-
# third party
from flask import Blueprint

blueprint = Blueprint('{{ cookiecutter.module_name }}', __name__,
                      url_prefix='/{{ cookiecutter.module_name }}')

@blueprint.route('/health')
def health():
    return 'OK'
