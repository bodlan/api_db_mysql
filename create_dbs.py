from mysql.connector import connect, Error
from random import randint
try:
    with connect(
        user="root",
        host="192.168.0.105",
        password="bodlan123987",
        port="3306"
    ) as connection:
        print(connection)
        create_delivery_db_query="CREATE DATABASE delivery"
        create_coffee_shod_db_query="CREATE DATABASE coffee_shop"
        show_db_query="SHOW DATABASES"
        with connection.cursor() as cursor:
            cursor.execute(create_delivery_db_query)
            cursor.execute(create_coffee_shod_db_query)
            cursor.fetchall()
except Error as e:
    print(e)

try:
    with connect(
        user="root",
        host="192.168.0.105",
        password="bodlan123987",
        port="3306",
        database="delivery"
    ) as connection:
        print("Connected to delivery db!")
        drop_customer_table_query="DROP TABLE IF EXISTS customer;"
        drop_order_table_query="DROP TABLE IF EXISTS customer_order;"
        drop_feedback_table_query="DROP TABLE IF EXISTS feedback;"
        drop_courier_table_query = "DROP TABLE IF EXISTS courier;"
        drop_support_table_query="DROP TABLE IF EXISTS support;"
        create_table_customer_query="""
        CREATE TABLE customer(
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(50),
        address VARCHAR(100),
        email VARCHAR(50),
        phone VARCHAR(14)
        )
        """
        create_table_courier_query="""
        CREATE TABLE courier(
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(50),
        address VARCHAR(100),
        phone VARCHAR(14)
        )
        """
        create_table_order_query="""
        CREATE TABLE customer_order(
        id INT AUTO_INCREMENT PRIMARY KEY,
        price INT NOT NULL,
        time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        type VARCHAR(100),
        amount INT NOT NULL,
        courier_id INT,
        FOREIGN KEY(courier_id) REFERENCES courier(id)
        )
        """
        create_feedback_table_query="""
        CREATE TABLE feedback(
        id INT AUTO_INCREMENT PRIMARY KEY,
        description VARCHAR(200),
        customer_id INT,
        topic VARCHAR(100),
        FOREIGN KEY(customer_id) REFERENCES customer(id)
        )
        """
        create_support_table_query="""
        CREATE TABLE support(
        name VARCHAR(50),
        address VARCHAR(100),
        phone VARCHAR(14)
        )
        """

        insert_customer_query="""
        Insert INTO customer
        (name, address, email, phone)
        VALUES (%s,%s,%s,%s)
        """
        customer_data=[
            ("Ramiro","7503 Mountainview St.Owosso, MI 48867",
             "rami.mcclee@consolidated-farm-research.net","(691)-356-9271"),
            ("Afra","8699 South Hill Rd.East Orange, NJ 07017",
             "afra_bump@arketmay.com","(717)-384-2384"),
            ("Simba","928 Division St.Deland, FL 32720",
             "sim-pe@egl-inc.info", "(893)-203-1629"),
            ("Niel","969 North Augusta CourtFranklin, MA 02038",
             "nie.morl@egl-inc.info", "(470)-212-2477"),
        ]
        insert_courier_query="""
        INSERT INTO courier
        (name,address,phone)
        VALUES(%s,%s,%s)
        """
        courier_data=[
            ("Jake","6 Hall St.Farmington, MI 48331","(552)-678-8729"),
            ("Andrew","412 Crescent St.Peabody, MA 01960","(550)-835-2286")
        ]
        insert_order_query="""
        INSERT INTO customer_order
        (price,type,amount,courier_id)
        VALUES (%s, %s,%s,%s)
        """
        order_data=[
            (randint(10,100),"latte",randint(1,5),randint(1,2)),
            (randint(10, 100), "mocha", randint(1, 5), randint(1, 2)),
            (randint(10, 100), "cappucino", randint(1, 5), randint(1, 2)),
            (randint(10, 100), "americano", randint(1, 5), randint(1, 2))
        ]
        insert_feedback_query="""
        INSERT INTO feedback
        (description,customer_id,topic)
        VALUES (%s,%s,%s)
        """
        feedback_data=[
            ("Requesting to use ecological ways to deliver your products.",randint(1,4),"Ecology")
        ]
        insert_support_query="""
        INSERT INTO support
        (name,address,phone)
        VALUES (%s,%s,%s)
        """
        support_data=[
            ("Jeremy","20 Taylor Ave.Woodside, NY 11377","(636)-372-9544"),
            ("Mark","9261 East Harvard Road Easton, PA 18042","(290)-508-5192")
        ]
        with connection.cursor() as cursor:
            cursor.execute(drop_feedback_table_query)
            cursor.execute(drop_customer_table_query)
            cursor.execute(drop_order_table_query)
            cursor.execute(drop_courier_table_query)
            cursor.execute(drop_support_table_query)

            cursor.execute(create_table_courier_query)
            cursor.execute(create_table_customer_query)
            cursor.execute(create_table_order_query)
            cursor.execute(create_feedback_table_query)
            cursor.execute(create_support_table_query)
            connection.commit()
            print("Tables for delivery Created!")

            cursor.executemany(insert_customer_query,customer_data)
            cursor.executemany(insert_courier_query,courier_data)
            cursor.executemany(insert_order_query,order_data)
            cursor.executemany(insert_feedback_query,feedback_data)
            cursor.executemany(insert_support_query,support_data)
            connection.commit()
            print("Tables populated!")
except Error as e:
    print(e)
try:
    with connect(
        user="root",
        host="192.168.0.105",
        password="bodlan123987",
        port="3306",
        database="coffee_shop"
    ) as connection:
        print("Connected to coffee shop db!")
        create_employee_table_query="""
        CREATE TABLE employee(
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(50),
        surname VARCHAR(50),
        email VARCHAR(50),
        address VARCHAR(100),
        phone_number VARCHAR(14),
        salary INT
        )
        """
        create_report_table_query="""
        CREATE TABLE report(
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(50),
        contects VARCHAR(200),
        created_by INT,
        FOREIGN KEY(created_by) REFERENCES employee(id)
        )
        """
        create_order_item_table_query="""
        CREATE TABLE order_item(
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(50),
        description VARCHAR(200)
        )
        """
        create_order_table_query="""
        CREATE TABLE employee_order(
        id INT AUTO_INCREMENT PRIMARY KEY,
        sum INT,
        created_by INT,
        item_id INT,
        FOREIGN KEY(created_by) REFERENCES employee(id),
        FOREIGN KEY(item_id) REFERENCES order_item(id)
        )
        """
        create_inventory_table_query="""
        CREATE TABLE inventory(
        id INT AUTO_INCREMENT PRIMARY KEY,
        type VARCHAR(50),
        price_per_piece INT
        )
        """
        create_inventory_request_table_query="""
        CREATE TABLE inventory_request(
        id INT AUTO_INCREMENT PRIMARY KEY,
        inventory_id INT,
        amount INT,
        created_by INT,
        FOREIGN KEY(inventory_id) REFERENCES inventory(id),
        FOREIGN KEY(created_by) REFERENCES employee(id)
        )
        """
        create_role_table_query="""
        CREATE TABLE role(
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(50)
        )
        """
        create_user_table_query="""
        CREATE TABLE user(
        id INT AUTO_INCREMENT PRIMARY KEY,
        login VARCHAR(50),
        password VARCHAR(50),
        employee_id INT,
        role_id INT,
        FOREIGN KEY(employee_id) REFERENCES employee(id),
        FOREIGN KEY(role_id) REFERENCES role(id)
        )
        """
        with connection.cursor() as cursor:
            cursor.execute(create_employee_table_query)
            cursor.execute(create_report_table_query)
            cursor.execute(create_order_item_table_query)
            cursor.execute(create_order_table_query)
            cursor.execute(create_inventory_table_query)
            cursor.execute(create_inventory_request_table_query)
            cursor.execute(create_role_table_query)
            cursor.execute(create_user_table_query)
            connection.commit()
            print("Created tables!")
except Error as e:
    print(e)