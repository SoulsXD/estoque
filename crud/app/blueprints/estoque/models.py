from app.extensions import db

class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.Text)
    preco = db.Column(db.Float, nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)
    categoria = db.Column(db.String(50), nullable=False)
    
    def __repr__(self):
        return f'<Produto {self.nome}>'