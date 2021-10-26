import sqlite3 as sl
from sqlite3 import Error

def create_connection(db_file):
    """ create a database connection to a SQLite database
    :param db_file: database file
    :return: Connection object or None
    """
    con = None
    try:
        con = sl.connect(db_file)
        return con
    except Error as e:
        print(e)
    return con

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def add_register(conn,register):
    """
    Add a new register
    :param conn:
    :param register:
    :return:
    """
    sql = ''' INSERT INTO register(ID_ucznia,ID_przedmiotu,ID_nauczyciela,Data,Ocena)
            VALUES(?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql,register)
    conn.commit()

    return cur.lastrowid

def add_teacher(conn,teacher):
    """
    Add a new teacher
    :param conn:
    :param task:
    :return:
    """
    sql = ''' INSERT INTO teachers(ID_nauczyciela,Nazwisko_nauczyciela)
            VALUES(?,?) '''
    cur = conn.cursor()
    cur.execute(sql,teacher)
    conn.commit()
    
    return cur.lastrowid

def add_subject(conn,subject):
    """
    Add a new subject
    :param conn:
    :param task:
    :return:
    """
    sql = ''' INSERT INTO subjects(ID_przedmiotu,Nazwa_przedmiotu)
            VALUES(?,?) '''
    cur = conn.cursor()
    cur.execute(sql,subject)
    conn.commit()
    
    return cur.lastrowid

def add_student(conn,student):
    """
    Add a new student
    :param conn:
    :param task:
    :return:
    """
    sql = ''' INSERT INTO students(ID_ucznia,Nazwisko_ucznia,Imie_ucznia,Rok,Grupa)
            VALUES(?,?,?,?,?) '''
    curr = conn.cursor()
    curr.execute(sql,student)
    conn.commit()

    return curr.lastrowid

def main():
    database = r"C:\Users\krzys\PK\matDyskretna\projekt1\my_school.db"

    sql_create_register_table = """CREATE TABLE IF NOT EXISTS register (
                                    ID_ucznia integer NOT NULL,
                                    ID_przedmiotu integer NOT NULL,
                                    ID_nauczyciela integer NOT NULL,
                                    Data text NOT NULL,
                                    Ocena integer NOT NULL,
                                    FOREIGN KEY (ID_nauczyciela) REFERENCES teachers (ID_nauczyciela),
                                    FOREIGN KEY (ID_przedmiotu) REFERENCES subjects (ID_przedmiotu)
                                );
                                """
    sql_create_teachers_table = """CREATE TABLE IF NOT EXISTS teachers (
                                    ID_nauczyciela integer NOT NULL,
                                    Nazwisko_nauczyciela text NOT NULL
                                );    
                                """
    sql_create_subjects_table = """CREATE TABLE IF NOT EXISTS subjects (
                                    ID_przedmiotu integer NOT NULL,
                                    Nazwa_przedmiotu text NOT NULL
                                );    
                                """
    sql_create_students_table = """CREATE TABLE IF NOT EXISTS students (
                                    ID_ucznia integer NOT NULL,
                                    Nazwisko_ucznia text NOT NULL,
                                    Imie_ucznia text NOT NULL,
                                    Rok integer NOT NULL,
                                    Grupa text NOT NULL
                                );    
                                """
    #create database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        create_table(conn,sql_create_register_table)
        create_table(conn,sql_create_teachers_table)
        create_table(conn,sql_create_subjects_table)
        create_table(conn,sql_create_students_table)
    else:
        print("Error! cannot create the database cennection.")

    with conn:
        #create new teacher
        teacher1 = (43,'Drabovski');
        teacher2 = (42,'Czajkowski');
        teacher3 = (44,'Dorota');
        teacher4 = (41,'Telenyk');

        teacher1 = add_teacher(conn,teacher1)
        teacher2 = add_teacher(conn,teacher2)
        teacher3 = add_teacher(conn,teacher3)
        teacher4 = add_teacher(conn,teacher4)

        #create new subject
        subject1 = (101,'MD');
        subject2 = (102,'BD');
        subject3 = (103,'SO');
        subject4 = (104,'ISI');

        subject1 = add_subject(conn,subject1)
        subject2 = add_subject(conn,subject2)
        subject3 = add_subject(conn,subject3)
        subject4 = add_subject(conn,subject4)

        #create new  student
        student1 = (1,'Nowacki','Andrzej',2000,'IA-01');
        student2 = (2,'Mazur','Anna',2001,'IA-01');
        student3 = (3,'Pawlowski','Piotr',2002,'IB-01');
        student4 = (4,'Zajac','Anna',2001,'IC-01');
        student5 = (5,'Król','Marzena',2000,'IC-01');
        student6 = (6,'Tomczyk','Witold',2002,'IA-01');

        student1 = add_student(conn,student1)
        student2 = add_student(conn,student2)
        student3 = add_student(conn,student3)
        student4 = add_student(conn,student4)
        student5 = add_student(conn,student5)
        student6 = add_student(conn,student6)

        #create register
        register1 = (student1,subject1,teacher4,'11.01.18',5);
        register2 = (student1,subject2,teacher2,'15.01.18',4);
        register3 = (student2,subject1,teacher4,'11.01.18',3);
        register4 = (student2,subject2,teacher2,'15.01.18',4);
        register5 = (student3,subject3,teacher1,'22.01.18',3.5);
        register6 = (student3,subject2,teacher2,'15.01.18',4);
        register7 = (student1,subject3,teacher1,'22.01.18',4);
        register8 = (student2,subject3,teacher1,'22.01.18',5);

        register1 = add_register(conn,register1)
        register2 = add_register(conn,register2)
        register3 = add_register(conn,register3)
        register4 = add_register(conn,register4)
        register5 = add_register(conn,register5)
        register6 = add_register(conn,register6)
        register7 = add_register(conn,register7)
        register8 = add_register(conn,register8)

        

if __name__ == '__main__':
    main()