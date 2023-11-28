@app.route('/submitData/<id>', methods=['GET'])
def get_one_submit_data(id):
    session = db_session.create_session()
    submit_data = session.query(SubmitData).get(id)
    if not submit_data:
        abort(404)
    return jsonify('submit_data': submit_data.to_dict(
        only=('id', 'name', 'surname', 'city_from', 'city_to', 'status',
              'departure_date', 'arrival_date', 'weight', 'volume', 'user_id')))


@app.route('/submitData/', methods=['GET'])
def get_submit_data_by_email():
    if not request.args:
        abort(400)
    session = db_session.create_session()
    user = session.query(User).filter(User.email == request.args.get('user__email')).first()
    if not user:
        abort(404)
    submit_data = session.query(SubmitData).filter(SubmitData.user_id == user.id).all()
    if not submit_data:
        abort(404)
    return jsonify('submit_data': [item.to_dict(
        only=('id', 'name', 'surname', 'city_from', 'city_to', 'status',
              'departure_date', 'arrival_date', 'user_id')) for item in submit_data])


@app.route('/submitData/<id>', methods=['PATCH'])
def edit_submit_data(id):
    session = db_session.create_session()
    submit_data = session.query(SubmitData).get(id)
    if not submit_data:
        abort(404)
    if submit_data.status != 'new':
        return jsonify('state': 0, 'message': 'Cannot edit a submit data that is not in "new" status')
    data = request.json
    if not data:
        abort(400)
    for key, value in data.items():
        if key not in ('name', 'surname', 'city_from', 'city_to', 'departure_date', 'arrival_date'):
            setattr(submit_data, key, value)
    session.commit()
    return jsonify('state': 1, 'message': "")

        @app.route('/submitData/', methods=['GET'])
        def get_submit_data_by_user_email():
            email = request.args.get('user__email')
            if not email:
                abort(400)
            session = db_session.create_session()
            user = session.query(User).filter(User.email == email).first()
            if not user:
                return jsonify('state': 1, 'data': [])
                submit_data = session.query(SubmitData).filter(SubmitData.user_id == user.id).all()
                return jsonify('state': 1,
                'data': ['id': d.id,
                'name': d.name,
                'surname': d.surname,
                'city_from': d.city_from,
                'city_to': d.city_to,
                'departure_date': d.departure_date,
                'arrival_date': d.arrival_date,
                for d in submit_data])


