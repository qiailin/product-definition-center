#
# Copyright (c) 2015 Red Hat
# Licensed under The MIT License (MIT)
# http://opensource.org/licenses/MIT
#
from django.apps import AppConfig
from pdc.apps.utils.utils import connect_app_models_pre_save_signal


class CommonAppConfig(AppConfig):
    name = 'pdc.apps.common'
    label = 'common'
    verbose_name = 'Common App'

    def ready(self):
        connect_app_models_pre_save_signal(self)
