import sqlite3
import anyToText
import info_extract
import con1

class Database_common_operations:
    """
        This is base class for all other database classes, This class will have all classmethods only.
    """

    @classmethod
    def run_query(cls, query: str):
        """
        This method is used to run a query.
        :param query: Must be in valid SQL syntax.
        :return: None
        """

        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        cursor.close()
        conn.close()

    @classmethod
    def run_query_and_return_all_data(cls, query):
        """
               This method is used to run a query.
               :param query: Must be in valid SQL syntax.
               :return: None
               """

        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute(query)
        data = cursor.fetchall()
        conn.commit()
        cursor.close()
        conn.close()
        return data
    

def input(name: str, email: str, res_path: str, file_name: str):
    print('here!')

    flag = anyToText.convert_to_text(res_path, name)
    if flag:
        print("Yersss")
    match_per, skills = con1.temp(f'output/{name}.txt')
    print('hello there')
    skill_fin = ""

    for i in skills:
        skill_fin = f"{i},{skill_fin}"

    
    query = f"insert into Master values('{name}', '{email}', '{res_path}', {match_per}, 'J30', '{skill_fin}');"
    print(query)
    x = Database_common_operations.run_query(query)
    print('boooyaahhh!')
    info_extract.temp(f'output/{name}.txt', name)
    return x 

def get_all():
    query = 'select * from Master;'
    data = Database_common_operations.run_query_and_return_all_data(query)
    return data

def get_uni_id():
    query = 'select * from ID;'
    data = Database_common_operations.run_query_and_return_all_data(query)[0][0]
    x = int(data)+1
    query1 = f"update ID set val = {x} where val = {data};"
    res = Database_common_operations.run_query(query1)
    return data

def add_job(jobName: str, jobDes: str, req: str):
    jobID = f"J{get_uni_id()}"
    query = f"insert into Job values('{jobID}','{jobName}','{jobDes}','{req}');"
    result = Database_common_operations.run_query(query)
    return jobID

def add_skill(skill):
    skillID = f"S{get_uni_id()}"
    query = f"insert into Skills values('{skillID}','{skill}');"
    result = Database_common_operations.run_query(query)
    return skillID

def get_all_skills():
    query = "select * from skills;"
    data = Database_common_operations.run_query_and_return_all_data(query)
    return data

def get_jobs():
    data = Database_common_operations.run_query_and_return_all_data("select * from Job;")
    fin_data = []
    for i in data:
        skills = ()
        skills_id = i[3].split(',') 
        skills_id = skills_id[1:]
        for j in skills_id:
            x = Database_common_operations.run_query_and_return_all_data(f"select * from Skills where SkillID = '{j}';")
            skills = skills + (x[0][1], )
        i_s = i[0:-1] + (skills, )
        fin_data.append(i_s)
    
    return fin_data