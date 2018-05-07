from openerp import http
from openerp.exceptions import ValidationError
from openerp.tools import DEFAULT_SERVER_DATETIME_FORMAT, DEFAULT_SERVER_DATE_FORMAT
from datetime import datetime, timedelta, date
import re
import  werkzeug
import json as json

class web(http.Controller):

# ==========================================================================================================================

	@http.route('/home', auth='user', type="http", website=True)
	def home(self, **kw):
		return http.request.render('membership_point.home', {})

# ==========================================================================================================================

	@http.route('/vouchers', auth='user', type='http', website=True)
	def vouchers(self, **kw):

		uid = http.request.env['membership.point.member'].get_member_by_uid
		mode = http.request.env['membership.point.voucher.setting']
		vouc = mode.search([['is_purchaseable', '=', 'True'],['voucher_type','=','member']],order="write_date desc")

		return http.request.render('membership_point.vouchers', {
			'ids' : uid,
			'vouchers' : vouc,
		})

# ==========================================================================================================================

	@http.route('/vouchers/detail/<int:id>', auth='user', type='http', website=True)
	def detail(self, id):

		model_user = http.request.env['res.users']
		id_user =	model_user._uid
		model_member = http.request.env['membership.point.member']
		member_id = model_member.env['membership.point.member'].get_member_by_uid(id_user)
		member = model_member.search([['id','=',member_id.id]])
		mode = http.request.env['membership.point.voucher.setting']
		vouc = mode.search([['is_purchaseable', '=', 'True'],['voucher_type','=','member'],['id','=',int(id)]])

		return http.request.render('membership_point.detail', {
			'member' : member,
			'id' : id,
			'vouchers' : vouc,
		})

# ==========================================================================================================================

	@http.route('/vouchers/<int:id>', auth='user', type='http', website=True)
	def detail_inweb(self, id):

		model_user = http.request.env['res.users']
		id_user =	model_user._uid
		model_member = http.request.env['membership.point.member']
		member_id = model_member.env['membership.point.member'].get_member_by_uid(id_user)
		member = model_member.search([['id','=',member_id.id]])
		mode = http.request.env['membership.point.voucher.setting']
		vouc = mode.search([['is_purchaseable', '=', 'True'],['voucher_type','=','member'],['id','=',int(id)]])

		return http.request.render('membership_point.details_voucher_row', {
			'member' : member,
			'id' : id,
			'vouchers' : vouc,
		})
# ==========================================================================================================================

	@http.route('/vouchers/purchase', auth='user', type='http', website=True)
	def purchase(self, **kw):


		model_user = http.request.env['res.users']
		id_user =	model_user._uid
		model_member = http.request.env['membership.point.member']
		member_id = model_member.env['membership.point.member'].get_member_by_uid(id_user)
		member = model_member.search([['id','=',member_id.id]])
		model_voucher_setting = http.request.env['membership.point.voucher.setting']
		vouc = model_voucher_setting.search([['id', '=', int(kw['voucher_id']) ]])
		vouc.purchase_member_voucher(member_id, int(kw['qty']))

		return werkzeug.utils.redirect('/mypurchases')

# ==========================================================================================================================

	@http.route('/mypurchases', auth='user', type='http', website=True)
	def mypurchases(self, **kw):

		fmt = '%Y-%m-%d'
		model_user = http.request.env['res.users']
		id_user =	model_user._uid
		model_member = http.request.env['membership.point.member']
		member_id = model_member.env['membership.point.member'].get_member_by_uid(id_user)
		model_voucher = http.request.env['membership.point.voucher']
		# vouc = model_voucher.search([['member_id','=', member_id.id]], order="expired_date asc")
		vouc = model_voucher.search([['member_id','=', member_id.id],['state','=', 'generated']], order="expired_date asc")

		# d1 = []

		return http.request.render('membership_point.mypurchases', {
			'vouchers' : vouc,
		})
# ==========================================================================================================================

	@http.route('/mypurchases/<string:filters>', auth='user', type='http', website=True)
	def mypurchasesx(self, filters):

		fmt = '%Y-%m-%d'
		model_user = http.request.env['res.users']
		id_user =	model_user._uid
		model_member = http.request.env['membership.point.member']
		member_id = model_member.env['membership.point.member'].get_member_by_uid(id_user)
		model_voucher = http.request.env['membership.point.voucher']
		vouc = model_voucher.search([['member_id','=', member_id.id],['state','=', filters]], order="expired_date asc")
		# d1 = []

		return http.request.render('membership_point.mypurchases_row', {
			'vouchers' : vouc,
		})
