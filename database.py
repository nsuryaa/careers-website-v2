from sqlalchemy import create_engine,text
import os


db_connection_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(db_connection_string)

def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs"))
        jobs = []
        for row in result.fetchall():
            jobs.append(dict(zip(result.keys(), row)))
        return jobs

def load_job_from_db(id):
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM jobs WHERE id = :id").bindparams(id=id))
        rows = result.all()
        if len(rows) == 0:
            return None
        else:
            job_dict = dict(zip(result.keys(), rows[0]))

            return job_dict