from flask import Flask, jsonify, request
from werkzeug.exceptions import HTTPException
from model.tournament import Tournament
from model import db

import config

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config.alchemy_uri()
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.app_context().push()
db.init_app(app)


# db.create_all()


@app.errorhandler(Exception)
def handle_error(e):
    """ Handle all exceptions and always return json """
    code = 500
    if isinstance(e, HTTPException):
        code = e.code
    return jsonify(error=str(e), code=code), code


@app.route('/', methods=['GET'])
def index():
    return jsonify({
        'service': 'working',
    })


@app.route('/tournament', methods=['GET'])
def get_tournament_list():
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))

    t = Tournament.query.order_by(Tournament.id.desc()).paginate(page, per_page, error_out=False)
    result = [i.as_dict() for i in t.items]

    return jsonify({
        'page': page,
        'per_page': per_page,
        'total': t.total,
        'result': result,
    })
    pass


@app.route('/tournament', methods=['POST'])
def create_tournament():
    params = request.get_json()

    app.logger.info(params)

    if not params:
        return jsonify({'data': None,
                        'message': 'Arguments Missed'}), 400

    if 'title' not in params:
        return jsonify({'data': None,
                        'message': 'TITLE_REQUIRED'}), 400

    if len(params['title']) == 0:
        return jsonify({'data': None,
                        'message': 'TITLE_IS_EMPTY'}), 400

    if 'gameName' not in params \
            or 'location' not in params:
        return jsonify({'error': 'Arguments Missed'}), 400

    tm = Tournament(
        title=params['title'],
        gameName=params['gameName'],
        playerCount=params.get('playerCount', 0),
        location=params['location'],
        address=params.get('address'),
        startAt=params.get('startAt'),
        endAt=params.get('endAt')
    )

    db.session.add(tm)
    db.session.commit()
    db.session.flush()

    return jsonify({'data': tm.as_dict(), 'message': 'OK'}), 201


@app.route('/tournament/<int:id>', methods=['GET'])
def get_tournament(id):
    tm = Tournament.query.get(id)
    if not tm:
        return jsonify({'data': None, 'message': 'TOURNAMENT_NOT_FOUND'}), 404

    return jsonify({'data': tm.as_dict(), 'message': 'OK'}), 200


@app.route('/tournament/<int:id>', methods=['PATCH'])
def update_tournament(id):
    params = request.get_json()

    tm = Tournament.query.get(id)
    for key, value in params.items():
        setattr(tm, key, value)
    db.session.commit()

    return jsonify({'data': tm.as_dict(), 'message': 'OK'}), 200


@app.route('/tournament/<int:id>', methods=['DELETE'])
def delete_tournament(id):
    if Tournament.query.filter_by(id=id).count() == 0:
        return jsonify({'data': None, 'message': 'TOURNAMENT_NOT_FOUND'}), 404

    Tournament.query.filter_by(id=id).delete()
    db.session.commit()
    return jsonify({'data': None, 'message': 'OK'}), 200


@app.route('/search', methods=['GET'])
def search_tournament():
    keyword = request.args.get('keyword', '')
    if len(keyword) == 0:
        return jsonify({
            'data': [],
            'message': 'OK'
        })

    search = "%{}%".format(keyword)

    rs = Tournament.query.filter(Tournament.title.like(search)).all()
    result = [i.as_dict() for i in rs]

    return jsonify({
        'data': result,
        'message': 'OK'
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
