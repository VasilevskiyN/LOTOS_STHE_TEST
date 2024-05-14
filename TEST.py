import sqlite3 as sq
task_id = "9e3497cf-3bb6-4389-8aef-286a1971cf7b"
def result_status (task_id):
    task_now = None
    print(task_id)
    with sq.connect("key.db") as con:
        cur = con.cursor()
        cur.execute('SELECT status FROM history '
                    'WHERE task_number = ?', (task_id,))

        row = cur.fetchone()
        if row:
            task_now = row[0]
            print(task_now)
    cur.close()
    print(task_now)
    return task_now