import sqlite3

class SQLiteDependency:
    def __init__(self):
        self.con = sqlite3.connect("data/address.db")
        self.cur = self.con.cursor()
    
    def create(self, data):
        query = """
            INSERT INTO address 
                (name, longitude, latitude, address) 
                VALUES(?,?,?,?) RETURNING *;
        """
        # query = "SELECT * FROM address;"

        values = tuple(e for e in data.get('values', []))

        r = self.cur.execute(query, values)

        result = r.fetchall()
        self.con.commit()

        print(f"Result: {result}")
        print(f"Result: {r.fetchone()}")
        return result

    def read(self,data={}):
        record_id = data.get('id',None)

        if record_id is None:
            query = "SELECT * FROM address;"
            r = self.cur.execute(query)
            result = r.fetchall()

        else:
            query = "SELECT * FROM address WHERE id = ?;"

            r = self.cur.execute(query, (record_id,))
            result = r.fetchall()
            self.con.commit()

        print(f"Result: {result}")
        return result
    
    def update(self,data):
        record_id = data.get('id')
        initial_values = data.get('values', [])
        initial_values.append(record_id)
        query = """

            UPDATE address
            SET name = ?,
                longitude = ?,
                latitude = ?,
                address = ?
            WHERE
                id = ? 
            RETURNING *;
        
        """
        values = tuple(e for e in initial_values)
        r = self.cur.execute(query, values)
        # r = cur.execute(query)

        result = r.fetchall()
        self.con.commit()

        print(f"Result: {result}")
        return result
    
    def delete(self,data):
        record_id = (data.get('id',None),)
        query = "DELETE FROM address WHERE id =? RETURNING *;"

        r = self.cur.execute(query, record_id)
        result = r.fetchall()
        self.con.commit()

        print(f"Result: {result}")
        return result
    
    def proximity(self, data):
        proximity = data.get('proximity',0)
        longitude = data.get('longitude',0)
        latitude = data.get('latitude',0)
        query = "SELECT * FROM address WHERE ;"
        r = self.cur.execute(query)
        result = r.fetchall()

# test = SQLiteDependency()

# # # x = test.create({"values": ["name test", 140, 14, "test address"]})
# x = test.read({"id": 1})
# # x = test.read()
# # # x = test.update({"id": 1, "values": ["changed", 100, 20, "changed"]})
# # # x = test.delete({"id":3})

# print(f"Final: {x}")