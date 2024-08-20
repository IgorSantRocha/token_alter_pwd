from odoo import models, fields, api
from datetime import datetime, timedelta


class UserTokenAlterPwd(models.Model):
    _name = 'user.token.alter.pwd'
    _description = 'Modelo para conter o token de autorização para alterar a senha'
    # _rec_name é o campo que será usado de nome do registro do modelo ao abrir as vizualizações
    #  _rec_name = 'campo_char'

    def _get_prazo_token(self):
        valor = datetime.now() + timedelta(minutes=5)
        return valor

    def _cria_token(self):
        valor = str(self).id+str(self.crieate_uid)
        return valor

    expira_em = fields.Datetime(
        string='Expira em', required=True,
        default=_get_prazo_token)

    token = fields.Char(
        string='Token de validação',
        index=False,  # Cria ou não um indice nessa coluna, com foco em melhorar a performance das consultas
        # translate=True,
        size=6,
        Default='000000'
    )
    # res_users_id = fields.Many2one(
    #    'res.users',  # nome da tabela relacionada
    # )
    res_users_id = fields.One2many(
        'res.users',  # nome da tabela relacionada
        'id',
        string='UserID',
        groups='base.group_user'
    )

    token_usado = fields.Boolean(
        string='Token ativo?',
        default=True,
        help='Após a utilização, o token será marcado como usado, para não poder ser usado duas vezes'
    )
