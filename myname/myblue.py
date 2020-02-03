from flask import (
    Blueprint, redirect, render_template, request, url_for
)
from .db import get_db
bp = Blueprint('myblue', __name__)

@bp.route("/")
def index():
    con = get_db()
    data = con.execute(
        'SELECT * FROM data'
        ).fetchall()
    return render_template('myblue/index.html', data=data)

@bp.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        date = request.form['date']
        value = request.form['value']

        con = get_db()
        con.execute(
            'INSERT INTO data (date, value)'
            ' VALUES (?, ?)',
            (date, value)
        )
        con.commit()
        return redirect(url_for('myblue.index'))

    return render_template('myblue/create.html')

