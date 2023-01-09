import logging
import pdb

import pandas as pd

from flask_restful import Resource, request

import config

class UpdateEmployee(Resource):
    def post(self):
        try:
            data = request.get_json()
            conn = config.connection()
            cur = conn.cursor()


            # conn_data = {
            #     "user": ['postgres'],
            #     "password": ['Nitish'],
            #     "host": ['localhost'],
            #     "port": ['5432']
            # }
            # df = pd.DataFrame(conn_data)
            # print(df)
            # convert_js = df.to_json(orient='records')
            # print(convert_js)


            if "userid" not in data or data['userid'] == '':
                return {'res_status': False, 'msg': 'pls enter user_name'}
            if "password" not in data or data['password'] == '':
                return {'res_status': False, 'msg': 'pls enter password'}
            # if "host" not in data or data['host'] == '':
            #     return {'res_status': False, 'msg': 'pls enter host_id'}
            # if "port" not in data or data['port'] == '':
            #     return {'res_status': False, 'msg': 'pls enter port_id'}
            userid = data['userid']
            password = data['password']
            # host = data['host']
            # port = data['port']
            logging.info(f"Database-UpdateDatabase:{userid, password}")
            cur.execute(f"update Update set userid='{userid}', password = {password} where userid = {data['userid']}")

            return {'res_status': True, 'Status_code': 200,
                    'msg': f'Database connection successful{userid, password}'}
        except Exception as e:
            logging.error(f'Database-Updatedatabase:Error:{e}')
            return {'res_status': False, 'msg': str(e)}
        finally:
            print("Final block close")
            cur.close()
            conn.close()

