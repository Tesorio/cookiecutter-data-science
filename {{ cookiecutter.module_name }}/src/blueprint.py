# -*- coding: utf-8 -*-
from flask import Blueprint

blueprint = Blueprint('{{ cookiecutter.module_name }}', __name__)

@blueprint.route('/health')
def health():
    return 'OK'
