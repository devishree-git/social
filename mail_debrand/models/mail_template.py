from lxml import etree
import lxml.html
import re
from odoo import _, api, models


class MailTemplate(models.Model):
    _inherit = "mail.template"

    @api.model
    def _debrand_body(self, html):
        root = lxml.html.fromstring(html)
        for i in root.xpath("//td"):
            try:
                if i.getchildren()[0].text == str('Odoo'):
                    i.clear()
            except:
                pass
            html = etree.tostring(root)
        return html

    @api.model
    def render_post_process(self, html):
        html = super().render_post_process(html)
        return self._debrand_body(html)
