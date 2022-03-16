from app.database import get_db


def output_formatter(results):
    out = []
    for result in results:
        res_dict={}
        res_dict["id"] = result[0]
        res_dict["make"] = result[1]
        res_dict["model"] = result[2]
        res_dict["color"] = result[3]
        res_dict["active"] = result[4]
        out.append(res_dict)
    return out

def insert(vehicle_dict):
    value_tuple = (
        vehicle_dict["make"],
        vehicle_dict["model"],
        vehicle_dict["color"],
    )

    stmt = """
        INSERT INTO vehicle (
            make,
            model,
            color
            ) VALUES (?, ?, ?)
        """
    cursor = get_db()
    last_row_id = cursor.execute(stmt, value_tuple)
    cursor.commit()
    cursor.close()

def scan():
    cursor = get_db().execute(
        "SELECT * FROM vehicle WHERE active=1", ())
    results = cursor.fetchall()
    cursor.close()
    return output_formatter(results)

def select_by_id(pk):
    cursor = get_db().execute("SELECT * FROM vehicle WHERE id=?", (pk, ))
    results = cursor.fetchall()
    cursor.close()
    return output_formatter(results)

def update(pk, vehicle_data):
    value_tuple = (
        vehicle_data["make"],
        vehicle_data["model"],
        vehicle_data["color"],
        pk
    )
    stmt = """
        UPDATE vehicle
        SET make=?,
        model=?,
        color=?
        WHERE id=?
    """
    cursor = get_db()
    cursor.execute(stmt, value_tuple)
    cursor.commit()


def deactivate(pk):
    # select_by_id(pk)
    # curser = get_db().execute("SELECT id=? FROM vehicle WHERE active=1", (pk, ))
    # is_active = (
    #     vehicle_data["active"],
    #     pk
    # )
    stmt = """
        UPDATE vehicle
        SET active=0
        WHERE id=?
    """
    cursor = get_db()
    cursor.execute(stmt, (pk, ))
    cursor.commit()
    cursor.close()
    
