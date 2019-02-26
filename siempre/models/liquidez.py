from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class Liquidez(models.Model):
    _name = 'liquidez'
    _description = 'Modelo Liquidez'
    # _rec_name = 'nombre'
    _order = 'fecha_balance'

    activo_corriente = fields.Float('Activo Corriente', required=True, digits=(20, 3))
    pasivo_corriente = fields.Float('Pasivo Corriente', required=True, digits=(20, 3))
    inventario = fields.Float('Inventario', required=True, digits=(20, 3))
    equivalente_efectivo = fields.Float('Efectivo y Equivalente de Efectivo', required=True, digits=(20, 3))
    cuentas_por_cobrar = fields.Float('Cuentas por Cobrar', required=True, digits=(20, 3))
    pasivo_circulante = fields.Float('Pasivo Circulante', required=True, digits=(20, 3))
    caja_banco = fields.Float('Caja y Bancos', required=True, digits=(20, 3))
    total_pasivo_corriente = fields.Float('Total Pasivo Corriente', required=True, digits=(20, 3))
    cobranzas = fields.Float('Cobranzas', required=True, digits=(20, 3))
    pago_efectivo = fields.Float('Pagos en Efectivo', required=True, digits=(20, 3))
    fecha_balance = fields.Date('Fecha de Validacion para el Balance', store=True, readonly=False)
