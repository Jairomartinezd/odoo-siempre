from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class Eficiencia(models.Model):
    _name = 'eficiencia'
    _description = 'Modelo Eficiencia'
    # _rec_name = 'nombre'
    _order = 'fecha_balance'

    unid_prod = fields.Integer('Unidades Producidas', required=True)
    val_prod = fields.Float('Valor de Produccion', required=True, digits=(20, 3))
    fact_prod = fields.Integer('Factor Productivo', required=True)
    cost_merc = fields.Float('Costo de Mercancias Vendidas', required=True, digits=(20, 3))
    inv_prom = fields.Float('Inventario Promedio', required=True, digits=(20, 3))
    vent_cred = fields.Float('Venta a Credito', required=True, digits=(20, 3))
    prom_cobrar = fields.Float('Promedio de Cuentas por Cobrar', required=True, digits=(20, 3))
    vent_net = fields.Float('Ventas Netas', required=True, digits=(20, 3))
    act_tot = fields.Float('Activo Total', required=True, digits=(20, 3))
    compr_per = fields.Float('Compras del Periodo', required=True, digits=(20, 3))
    prov_prom = fields.Float('Proveedores Promedio', required=True, digits=(20, 3))
    fecha_balance = fields.Date('Fecha de Validacion para el Balance', store=True,
        readonly=False, )
