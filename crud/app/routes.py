from flask import Blueprint, render_template, request, redirect, url_for
from .models import Tarefa
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    tarefas = Tarefa.query.all()
    return render_template('index.html', tarefas=tarefas)

@main.route('/criar', methods=['GET', 'POST'])
def criar():
    if request.method == 'POST':
        titulo = request.form['titulo']
        descricao = request.form['descricao']
        nova = Tarefa(titulo=titulo, descricao=descricao)
        db.session.add(nova)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('create.html')

@main.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    tarefa = Tarefa.query.get_or_404(id)
    if request.method == 'POST':
        tarefa.titulo = request.form['titulo']
        tarefa.descricao = request.form['descricao']
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('edit.html', tarefa=tarefa)

@main.route('/deletar/<int:id>')
def deletar(id):
    tarefa = Tarefa.query.get_or_404(id)
    db.session.delete(tarefa)
    db.session.commit()
    return redirect(url_for('main.index'))