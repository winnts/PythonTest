import sqlite3
import sys
import logging

cdm_path = '/home/adyachenko/IdeaProjects/PythonTest/'
con = None
logging.basicConfig(filename='sqlite.log', level=logging.DEBUG)
try:
    con = sqlite3.connect(cdm_path+'cdm.db')
    cur = con.cursor()
    cur.execute('select * from "orm::models::installertasks::installertasks"')
    logging.info(cur.fetchone())
    con.execute('DELETE FROM "orm::models::installertasks::installertasks"')
    con.commit()
except sqlite3.Error, e:
    print "Error %s:" % e.args[0]
    sys.exit(1)
finally:
    if con:
        con.close()
