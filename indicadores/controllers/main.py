import logging

from odoo import http
from odoo.http import request

import json
import qrcode
import base64


class MainController(http.Controller):

	_logger = logging.getLogger(__name__)

	#Pagina Inicio
	@http.route(['/indicadores'], auth='public', website=True)
	def inicio(self):
		return http.request.render('indicadores.inicio_indicador')

	#Paginas de Liquidez
	@http.route(['/indicadores/liquidez'], auth='public', website=True)
	def inicio_liquidez(self):
		return http.request.render('indicadores.inicio_liquidez')

	@http.route(['/indicadores/liquidez/razonCorriente'], auth='public', website=True)
	def inicio_liquidez_RC(self):

		modelo_liquidez = http.request.env['liquidez'].sudo().search([])


		diccionario_res = {
			'modelo_liquidez': modelo_liquidez,
		}

		return http.request.render('indicadores.inicio_liquidez_rc', diccionario_res)

	@http.route(['/indicadores/liquidez/pruebaAcida'], auth='public', website=True)
	def inicio_liquidez_pa(self):

		modelo_liquidez = http.request.env['liquidez'].sudo().search([])


		diccionario_res = {
			'modelo_liquidez': modelo_liquidez,
		}

		return http.request.render('indicadores.inicio_liquidez_pa', diccionario_res)

	@http.route(['/indicadores/liquidez/pruebaSuperAcida'], auth='public', website=True)
	def inicio_liquidez_psa(self):

		modelo_liquidez = http.request.env['liquidez'].sudo().search([])


		diccionario_res = {
			'modelo_liquidez': modelo_liquidez,
		}

		return http.request.render('indicadores.inicio_liquidez_psa', diccionario_res)

	@http.route(['/indicadores/liquidez/capitalTrabajo'], auth='public', website=True)
	def inicio_liquidez_cnt(self):

		modelo_liquidez = http.request.env['liquidez'].sudo().search([])


		diccionario_res = {
			'modelo_liquidez': modelo_liquidez,
		}

		return http.request.render('indicadores.inicio_liquidez_cnt', diccionario_res)

	@http.route(['/indicadores/liquidez/dispInmediata'], auth='public', website=True)
	def inicio_liquidez_di(self):

		modelo_liquidez = http.request.env['liquidez'].sudo().search([])


		diccionario_res = {
			'modelo_liquidez': modelo_liquidez,
		}

		return http.request.render('indicadores.inicio_liquidez_di', diccionario_res)

	@http.route(['/indicadores/liquidez/coberturaPago'], auth='public', website=True)
	def inicio_liquidez_cp(self):

		modelo_liquidez = http.request.env['liquidez'].sudo().search([])


		diccionario_res = {
			'modelo_liquidez': modelo_liquidez,
		}

		return http.request.render('indicadores.inicio_liquidez_cp', diccionario_res)

	#Paginas de Eficiencia
	@http.route(['/indicadores/eficiencia'], auth='public', website=True)
	def inicio_eficiencia(self):
		return http.request.render('indicadores.inicio_eficiencia')

	@http.route(['/indicadores/eficiencia/eficiencia'], auth='public', website=True)
	def inicio_eficiencia_ef(self):

		modelo_eficiencia = http.request.env['eficiencia'].sudo().search([])


		diccionario_res = {
			'modelo_eficiencia': modelo_eficiencia,
		}

		return http.request.render('indicadores.inicio_eficiencia_ef', diccionario_res)

	@http.route(['/indicadores/eficiencia/rotInv'], auth='public', website=True)
	def inicio_eficiencia_ri(self):

		modelo_eficiencia = http.request.env['eficiencia'].sudo().search([])


		diccionario_res = {
			'modelo_eficiencia': modelo_eficiencia,
		}

		return http.request.render('indicadores.inicio_eficiencia_ri', diccionario_res)

	@http.route(['/indicadores/eficiencia/invExist'], auth='public', website=True)
	def inicio_eficiencia_ie(self):

		modelo_eficiencia = http.request.env['eficiencia'].sudo().search([])


		diccionario_res = {
			'modelo_eficiencia': modelo_eficiencia,
		}

		return http.request.render('indicadores.inicio_eficiencia_ie', diccionario_res)

	@http.route(['/indicadores/eficiencia/rotCart'], auth='public', website=True)
	def inicio_eficiencia_rc(self):

		modelo_eficiencia = http.request.env['eficiencia'].sudo().search([])


		diccionario_res = {
			'modelo_eficiencia': modelo_eficiencia,
		}

		return http.request.render('indicadores.inicio_eficiencia_rc', diccionario_res)

	@http.route(['/indicadores/eficiencia/perCob'], auth='public', website=True)
	def inicio_eficiencia_pc(self):

		modelo_eficiencia = http.request.env['eficiencia'].sudo().search([])


		diccionario_res = {
			'modelo_eficiencia': modelo_eficiencia,
		}

		return http.request.render('indicadores.inicio_eficiencia_pc', diccionario_res)

	@http.route(['/indicadores/eficiencia/rotAct'], auth='public', website=True)
	def inicio_eficiencia_ra(self):

		modelo_eficiencia = http.request.env['eficiencia'].sudo().search([])


		diccionario_res = {
			'modelo_eficiencia': modelo_eficiencia,
		}

		return http.request.render('indicadores.inicio_eficiencia_ra', diccionario_res)

	@http.route(['/indicadores/eficiencia/rotProv'], auth='public', website=True)
	def inicio_eficiencia_rp(self):

		modelo_eficiencia = http.request.env['eficiencia'].sudo().search([])


		diccionario_res = {
			'modelo_eficiencia': modelo_eficiencia,
		}

		return http.request.render('indicadores.inicio_eficiencia_rp', diccionario_res)

	