from odoo import fields, models



class Book(models.Model):
    _name = 'book'
    _description = "Book Management"

    name = fields.Char(string='Title', required=True)
    author = fields.Char(string='Author', required=True)
    publication_date = fields.Date(string='Publication Date')