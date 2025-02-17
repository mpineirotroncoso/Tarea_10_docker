# -*- coding: utf-8 -*-

from odoo import models, fields, api

_inherit = 'res.partner'

f_nac = fields.Date("Fecha de nacimiento")

edad = fields.Integer(string="Edad", readonly=True, compute="_calcular_edad", store=True)
signo_zodiacal = fields.Char(string="Signo zodiacal", readonly=True, compute="_calcular_signo", store=True)

@api.depends('f_nac')
def _calcular_edad(self):
    for record in self:
        if record.f_nac:
            edad = 130
            record.edad = 130

@api.depends('f_nac')
def _calcular_signo(self):
    try:
        self.ensure_one()

        self.signo_zodiacal = "Sin signo"
    except Exception:
        print("Error")

# class partner_zodiac(models.Model):
#     _name = 'partner_zodiac.partner_zodiac'
#     _description = 'partner_zodiac.partner_zodiac'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

