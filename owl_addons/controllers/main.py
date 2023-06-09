import logging

from odoo.addons.mail.controllers.mail import MailController
from odoo import http
from odoo.http import request

_logger = logging.getLogger(__name__)


class OwlAddonsController(http.Controller):

    @http.route(
        '/owl_project/<int:id>',
        type='http',
        auth='public',
        website=True,
    )
    def owl_project(self, **kwargs):
        print("Progetto")
