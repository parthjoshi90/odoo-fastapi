# -*- coding: utf-8 -*-

import odoo
from odoo.api import Environment


def odoo_env() -> Environment:
    # TODO: Needs to have the user specific environment rather then using SUPERUSER_ID
    regitry = odoo.registry(odoo.tools.config["db_name"]).check_signaling()
    with regitry.manage_changes():
        with regitry.cursor() as cr:
            yield Environment(cr, odoo.SUPERUSER_ID, {})