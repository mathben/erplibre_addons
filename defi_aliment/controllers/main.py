from odoo import http
from odoo.http import request


class DefiAlimentController(http.Controller):
    @http.route(
        ["/defi_aliment/helloworld"],
        type="json",
        auth="public",
        website=True,
        methods=["POST", "GET"],
        csrf=False,
    )
    def hello_world(self):
        return {"hello": "Hello World!"}
