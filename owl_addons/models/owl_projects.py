from odoo import models, api, fields


class OwlProjects(models.Model):
    _name = 'owl.projects'

    name = fields.Char(string='Owl Project')
    link_project = fields.Html(String="Url Project")

    def get_owl_project(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_url',
            'name': "Owl Project",
            'target': 'new',
            'url': '/owl_project/{}'.format(self.id),
        }
