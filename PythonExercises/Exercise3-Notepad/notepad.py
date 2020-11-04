import sqlite3

def select():
    conector = sqlite3.connect("notepad.db")
    cursor = conector.cursor()
    sql = "SELECT * FROM notes"
    cursor.execute(sql)
    data = cursor.fetchall() # return all records produced by SELECT
    cursor.close()
    conector.close()

    print("\nTable data: \n")
    print("="*55)
    print("{:7}{:20}{:>6}".format("id","title","description"))
    print()
    for d in data:
        print("{:<7}{:20}{:>6}".format(d[0],d[1],d[2]))
    print("="*55)
    print("Found {} records".format(len(data)))
    main()

def insert():
    title = str(input("Enter title: "))
    description = str(input("Enter description: "))

    conector = sqlite3.connect("notepad.db")
    cursor = conector.cursor()
    sql = """
        CREATE TABLE IF NOT EXISTS notes(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            description TEXT
        );
    """
    cursor.execute(sql)

    sql = f"""
        INSERT INTO notes (title, description) values('{title}', '{description}');
    """
    cursor.execute(sql)

    conector.commit()
    print("Note added successfully!")

    cursor.close
    conector.close()
    main()

def update():
    try:
        noteID = int(input("Enter note ID: "))
        newTitle = str(input("Enter new note name: "))
        newDescription = str(input("Enter new note description: "))
    except:
        print("Error")
        update()
        
    conector = sqlite3.connect("notepad.db")
    cursor = conector.cursor()
    
    
    cursor.execute("""
        UPDATE notes
        SET title = ?, description = ?
        WHERE id=?
    """, (newTitle,newDescription,noteID))
    conector.commit()

    cursor.close
    conector.close()
    main()

    
def delete():
    try:
        noteID = int(input("Enter note ID: "))
        op = int(input(f"Are you sure you want to delete the note {noteID}?\n1 - yes\n2 - not\n>>> "))
        if(op == 1):
            conector = sqlite3.connect("notepad.db")
            cursor = conector.cursor()
            cursor.execute("""
                DELETE FROM notes
                WHERE id = ?
            """, (noteID,))
            conector.commit()
            
            cursor.close
            conector.close()
            print("\nNote successfully deleted")
            main()
        else:
            main()
    except:
        print("Error")
        delete()


        
def main():
    print("\nOptions:")
    print("(1) - To check your notes")
    print("(2) - To add a note")
    print("(3) - To update a note")
    print("(4) - To delete a nota")

    try:
        op = int(input(">>> "))

        if( op > 0 and op < 5):
            if(op == 1):
                select()
            elif(op == 2):
                insert()
            elif(op == 3):
                update()
            elif(op == 4):
                delete()
        else:
            print("Invalid option")
            main()
    except:
        print("Error")
        main()


print("-"*24)
print("Simple notepad in python")
print("-"*24)
main()
