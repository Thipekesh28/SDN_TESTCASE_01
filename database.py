from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://2tbapi8bc3m9cvx8pnww:pscale_pw_10YnHMfHSznFMKXdkv2uL0FzkGIzEKh9Dx9hyjKJmol@aws.connect.psdb.cloud/sdn_test01?charset=utf8mb4"

engine = create_engine(db_connection_string,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem"
                       }})


def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs = []
    for row in result.all():
      jobs.append(dict(row))
    return jobs
