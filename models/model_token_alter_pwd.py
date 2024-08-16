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
    res_users_id = fields.Many2one(
        'res.users',  # nome da tabela relacionada
    )

    uid = fields.Integer(
        # ,groups='São níveis de acesso'
        # Ao usar o compute, definir como "store" false, pois não precisa gravar essa informaçao no banco. Já que ela é sempre recalculada
        # Usado para chamar funções que inserem os valores nesse campo
        string='ID do usuário que solicitou o token',
        default=0,
        help='Vou armazenar o id do usuário que solicitou o token para validar depois',
        required=True,
        readonly=True,
    )

    token_usado = fields.Boolean(
        string='Token ativo?',
        default=True,
        help='Após a utilização, o token será marcado como usado, para não poder ser usado duas vezes'
    )
