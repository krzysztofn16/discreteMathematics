import sqlite3 as sl
from sqlite3 import Error
import os
import itertools

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

def delete_student(conn, surname):
    """
    Delete a student by surname
    :param conn: Connection to the SQLite database
    :param surname: surname of the student
    :return:
    """
    sql = 'DELETE FROM tasks WHERE Nazwisko_ucznia=?'
    #delete all rows 'DELETE FROM students'
    cur = conn.cursor()
    cur.execute(sql, (surname,))
    conn.commit()

def displayDB(conn):
    curr = conn.cursor()
    curr.execute('SELECT * FROM  register')
    print("Register:\n"+str(curr.fetchall())+"\n")
    curr.execute('SELECT * FROM students')
    print("Students:\n"+str(curr.fetchall())+"\n")
    curr.execute('SELECT * FROM teachers')
    print("Teacherss:\n"+str(curr.fetchall())+"\n")
    curr.execute('SELECT * FROM subjects')
    print("Subjects:\n"+str(curr.fetchall())+"\n")

def wariant5pytanie1(conn):
    """
    1.	Wybierz Nazwiska uczniów grupy IA-01, którzy otrzymali, 
    i naucicieli, którzy wpisali, 
    oceny 2 lub 5 z przedmiotów MD lub BD
    """
    # 1.Znajdź ID_przedmiotu bazując na Nazwa_przedmiotu
    sql = 'SELECT rowid FROM subjects WHERE Nazwa_przedmiotu="MD" OR Nazwa_przedmiotu="BD"'
    cur = conn.cursor()
    cur.execute(sql)
    id_przed = cur.fetchall()
    # 2.Wyszukanie interesujących nas informacji. Zwraca wiersz z register spełniający oczekiwania
    cur = conn.cursor()
    cur.execute('SELECT ID_ucznia AND ID_nauczyciela FROM register WHERE (Ocena=2 OR Ocena=5)AND(ID_przedmiotu=? OR ID_przedmiotu=?)',(*id_przed[0],*id_przed[1]))
    sql = cur.fetchall()
    # 3.Wyciągnięcie ID_nauczyciela i ID_ucznia z wierszy db register
    id_nauczyciela=[]
    id_ucznia=[]
    for elem in sql:
        cur1 = conn.cursor()
        cur1.execute('SELECT ID_nauczyciela FROM register WHERE rowid = ?',(*elem,))
        id_nauczyciela.append(cur1.fetchall())
        cur2 = conn.cursor()
        cur2.execute('SELECT ID_ucznia FROM register WHERE rowid = ?',(*elem,))
        id_ucznia.append(cur2.fetchall())
    # 4.Sprawdzenie czy uczniowie należą do grupy IA-01 i wyciagniecie nazwisk
    nazwisko_ucznia=[]
    for elem in id_ucznia[0]:
        cur = conn.cursor()
        cur.execute('SELECT Nazwisko_ucznia FROM students WHERE Grupa="IA-01" AND rowid=?',(*elem,))
        nazwisko_ucznia.append(cur.fetchall())
    # 5. Wyciagniecie nazwisk nauczycieli
    nazwisko_nauczyciela=[]
    for elem in id_nauczyciela[0]:
        cur = conn.cursor()
        cur.execute('SELECT Nazwisko_nauczyciela FROM teachers WHERE rowid=?',(*elem,))
        nazwisko_nauczyciela.append(cur.fetchall())

    nazwisko_ucznia = list(itertools.chain.from_iterable(nazwisko_ucznia))
    nazwisko_nauczyciela = list(itertools.chain.from_iterable(nazwisko_nauczyciela))
    return "Uczeniowie to: \n"+str(nazwisko_ucznia)+", \na nauczyciele to: \n"+str(nazwisko_nauczyciela)+"."

def wariant5pytanie2(conn):
    """
    Wybierz ID i nazwiska naucicieli, którzy wpisali oceny 2 lub 5 uczniom grupy IA-01.
    """
    # 1.Wybrać uczniów, którzy należą do grupy 'IA-01'
    cur = conn.cursor()
    cur2 = conn.cursor()
    cur.execute('SELECT ID_ucznia FROM students WHERE Grupa="IA-01"')
    IAstudents = cur.fetchall()
    # 2.Wybrać nauczycieli, którzy dali ocene 2 lub 5 dla uczniów z grupy 'IA-01'
    rowIDNauczyciela=[]
    for student in IAstudents:
        cur.execute('SELECT ID_nauczyciela FROM register WHERE (Ocena=2 OR Ocena=5)AND(ID_ucznia=?)',(*student,))
        rowIDNauczyciela.append(cur.fetchall())
    rowIDNauczyciela = list(itertools.chain.from_iterable(rowIDNauczyciela)) #moreover, it remove empy position in list
    # 3.Wybrać naziwska i ID nauczycieli, którzy zostali wcześniej wybrani
    nazw_naucz=[]
    id_naucz=[]
    for rowid in rowIDNauczyciela:
        cur.execute('SELECT Nazwisko_nauczyciela FROM teachers WHERE rowid=?',(*rowid,))
        cur2.execute('SELECT ID_nauczyciela FROM teachers WHERE rowid=?',(*rowid,))
        nazw_naucz.append(cur.fetchall())
        id_naucz.append(cur2.fetchall())
    nazw_naucz=list(itertools.chain.from_iterable(nazw_naucz))
    id_naucz=list(itertools.chain.from_iterable(id_naucz))
    return "Szukani nauczyciele to: \n"+str(nazw_naucz)+"\nO odpowienim ID:\n"+str(id_naucz)+"."
    
def wariant5pytanie3(conn):
    """
    Wybierz nazwy i ID przedmiotów, z których uczniów grupy IA-01 otrzymali od naucicieli Telenyka lub Czaikowskiego oceny od 3. 
    """
    # 1.Wybrać uczniów, którzy należą do grupy 'IA-01'
    cur = conn.cursor()
    cur2 = conn.cursor()
    cur.execute('SELECT ID_ucznia FROM students WHERE Grupa="IA-01"')
    IAstudents = cur.fetchall()
    # 2.Wybrać ID nauczyciela Telenyk i Czaikowski
    cur.execute('SELECT rowid FROM teachers WHERE Nazwisko_nauczyciela="Telenyk" OR Nazwisko_nauczyciela="Czajkowski"')
    rowIDnaucz = cur.fetchall()
    # 3.Wybrać rowid przedmiotu względem, uczniów, naucz i ocen.
    IDprzed=[]
    for IDucz in IAstudents:
        for IDnau in rowIDnaucz:
            cur.execute('SELECT ID_przedmiotu FROM register WHERE ID_ucznia=? AND ID_Nauczyciela=? AND Ocena>=3',(*IDucz,*IDnau,))
            IDprzed.append(cur.fetchall())
    IDprzed=list(itertools.chain.from_iterable(IDprzed))
    actIDprzed=[]
    [actIDprzed.append(elem) for elem in IDprzed if elem not in actIDprzed]
    # 4.Wybrać nazwę i ID_przedmiotów
    nazw_przed=[]
    id_przed=[]
    for rowid in actIDprzed:
        cur.execute('SELECT Nazwa_przedmiotu FROM subjects WHERE rowid=?',(*rowid,))
        cur2.execute('SELECT ID_przedmiotu FROM subjects WHERE rowid=?',(*rowid,))
        nazw_przed.append(cur.fetchall())
        id_przed.append(cur2.fetchall())
    nazw_przed=list(itertools.chain.from_iterable(nazw_przed))
    id_przed=list(itertools.chain.from_iterable(id_przed))
    return "Szukane przedmioty to: \n"+str(nazw_przed)+"\no odpowienim ID:\n"+str(id_przed)+"."

def wariant5pytanie4(conn):
    """
    Wybierz ID i nazwiska uczniow, którzym wpisane oceny od 3.5 do 4.5.
    """
    # 1.Wybierz ID ucznia w zakresie ocen
    cur = conn.cursor()
    cur2 = conn.cursor()
    cur.execute('SELECT ID_ucznia FROM register WHERE Ocena>=3.5 AND Ocena<=4.5')
    rowID=cur.fetchall()
    # 2.Wybrać nazwę i ID_przedmiotów
    nazw_ucznia=[]
    id_ucznia=[]
    for rowid in rowID:
        cur.execute('SELECT Nazwisko_ucznia FROM students WHERE rowid=?',(*rowid,))
        cur2.execute('SELECT ID_ucznia FROM students WHERE rowid=?',(*rowid,))
        nazw_ucznia.append(cur.fetchall())
        id_ucznia.append(cur2.fetchall())
    nazw_ucznia=list(itertools.chain.from_iterable(nazw_ucznia))
    id_ucznia=list(itertools.chain.from_iterable(id_ucznia))
    
    actNazw_ucznia=[]
    actID_ucznia=[]
    [actNazw_ucznia.append(elem) for elem in nazw_ucznia if elem not in actNazw_ucznia]
    [actID_ucznia.append(elem) for elem in id_ucznia if elem not in actID_ucznia]

    return "Lista uczniów z ocenami w zakresie to: \n"+str(actNazw_ucznia)+"\no odpowiednim ID:\n"+str(actID_ucznia)+"."
def main():
    path = os.getcwd()
    database = os.path.join(path,"my_school.db")
    #create database connection
    conn = create_connection(database)

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

    # create tables
    # if conn is not None:
    #     create_table(conn,sql_create_register_table)
    #     create_table(conn,sql_create_teachers_table)
    #     create_table(conn,sql_create_subjects_table)
    #     create_table(conn,sql_create_students_table)
    # else:
    #     print("Error! cannot create the database cennection.")

    # with conn:
    #     #create new teacher
    #     teacher1 = (43,'Drabovski');
    #     teacher2 = (42,'Czajkowski');
    #     teacher3 = (44,'Dorota');
    #     teacher4 = (41,'Telenyk');

    #     teacher1 = add_teacher(conn,teacher1)
    #     teacher2 = add_teacher(conn,teacher2)
    #     teacher3 = add_teacher(conn,teacher3)
    #     teacher4 = add_teacher(conn,teacher4)

    #     #create new subject
    #     subject1 = (101,'MD');
    #     subject2 = (102,'BD');
    #     subject3 = (103,'SO');
    #     subject4 = (104,'ISI');

    #     subject1 = add_subject(conn,subject1)
    #     subject2 = add_subject(conn,subject2)
    #     subject3 = add_subject(conn,subject3)
    #     subject4 = add_subject(conn,subject4)

    #     #create new  student
    #     student1 = (1,'Nowacki','Andrzej',2000,'IA-01');
    #     student2 = (2,'Mazur','Anna',2001,'IA-01');
    #     student3 = (3,'Pawlowski','Piotr',2002,'IB-01');
    #     student4 = (4,'Zajac','Anna',2001,'IC-01');
    #     student5 = (5,'Król','Marzena',2000,'IC-01');
    #     student6 = (6,'Tomczyk','Witold',2002,'IA-01');

    #     student1 = add_student(conn,student1)
    #     student2 = add_student(conn,student2)
    #     student3 = add_student(conn,student3)
    #     student4 = add_student(conn,student4)
    #     student5 = add_student(conn,student5)
    #     student6 = add_student(conn,student6)

    #     #create register
    #     register1 = (student1,subject1,teacher4,'11.01.18',5);
    #     register2 = (student1,subject2,teacher2,'15.01.18',4);
    #     register3 = (student2,subject1,teacher4,'11.01.18',3);
    #     register4 = (student2,subject2,teacher2,'15.01.18',4);
    #     register5 = (student3,subject3,teacher1,'22.01.18',3.5);
    #     register6 = (student3,subject2,teacher2,'15.01.18',4);
    #     register7 = (student1,subject3,teacher1,'22.01.18',4);
    #     register8 = (student2,subject3,teacher1,'22.01.18',5);

    #     register1 = add_register(conn,register1)
    #     register2 = add_register(conn,register2)
    #     register3 = add_register(conn,register3)
    #     register4 = add_register(conn,register4)
    #     register5 = add_register(conn,register5)
    #     register6 = add_register(conn,register6)
    #     register7 = add_register(conn,register7)
    #     register8 = add_register(conn,register8)

    displayDB(conn)

    print("\nPytanie 1:\n"+wariant5pytanie1(conn))
    print("\nPytanie 2:\n"+wariant5pytanie2(conn))
    print("\nPytanie 3:\n"+wariant5pytanie3(conn))
    print("\nPytanie 4:\n"+wariant5pytanie4(conn))
         

if __name__ == '__main__':
    main()