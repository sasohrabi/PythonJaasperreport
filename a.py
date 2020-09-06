# -*- coding: utf-8 -*-

from platform import python_version
from pyreportjasper import JasperPy
import sqlite3
import pandas as pd

def advanced_example_using_database():
    input_file = 'C:/output/report2.jrxml'
    output = 'c:/output/examples'
    con = sqlite3.connect('C:/output/checkrecived.sqlite')
    data = pd.read_sql_query("select code,PartyAccount from tblPartyAccount", con)
    print(data)
    jasper = JasperPy()
    jasper.process(
        input_file,
        output_file=output,
        format_list=["pdf", "rtf"],
        db_connection=con
    )

advanced_example_using_database()
