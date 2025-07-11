from flask import render_template, redirect, url_for, flash, request
from app.blueprints.estoque.models import Produto
from app.blueprints.estoque.forms import ProdutoForm
from app.extensions import db
from . import bp

@bp.route('/')
def listar_produtos():
    produtos = Produto.query.all()
    return render_template('estoque/listar.html', produtos=produtos)

@bp.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar_produto():
    form = ProdutoForm()
    if form.validate_on_submit():
        produto = Produto(
            nome=form.nome.data,
            descricao=form.descricao.data,
            preco=form.preco.data,
            quantidade=form.quantidade.data,
            categoria=form.categoria.data
        )
        db.session.add(produto)
        db.session.commit()
        flash('Produto cadastrado com sucesso!', 'success')
        return redirect(url_for('estoque.listar_produtos'))
    return render_template('estoque/cadastrar.html', form=form)

@bp.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar_produto(id):
    produto = Produto.query.get_or_404(id)
    form = ProdutoForm(obj=produto)
    if form.validate_on_submit():
        produto.nome = form.nome.data
        produto.descricao = form.descricao.data
        produto.preco = form.preco.data
        produto.quantidade = form.quantidade.data
        produto.categoria = form.categoria.data
        db.session.commit()
        flash('Produto atualizado com sucesso!', 'success')
        return redirect(url_for('estoque.listar_produtos'))
    return render_template('estoque/editar.html', form=form)

@bp.route('/excluir/<int:id>', methods=['POST'])
def excluir_produto(id):
    produto = Produto.query.get_or_404(id)
    db.session.delete(produto)
    db.session.commit()
    flash('Produto excluído com sucesso!', 'success')
    return redirect(url_for('estoque.listar_produtos'))