#!/usr/bin/env python3
import uuid
import mysql.connector
import csv


def connect_db():
    connection = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="kiddie",
        password="Password@123!"
    )
    return connection


def create_database(connection):
    cursor = connection.cursor()
    try:
        cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev")
    except Exception as e:
        print("Database creation error:", e)
    finally:
        connection.close()


def connect_to_prodev():
    try:
        connection = mysql.connector.connect(
            host="127.0.0.1",
            port=3306,
            user="kiddie",
            password='Password@123!',
            database='ALX_prodev'
        )

        if connection.is_connected():
            print("Connected to ALX_prodev database")
            return connection

    except mysql.connector.Error as e:
        print("Error while connecting to MySQL:", e)
        return None


def create_table(connection):
    cursor = connection.cursor()
    try:
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS user_data (
                user_id CHAR(36) PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL,
                age DECIMAL NOT NULL,
                INDEX idx_user_id (user_id)
            )
            """
        )
    except mysql.connector.Error as e:
        print("Table creation error:", e)


def insert_data(connection, data):
    try:
        cursor = connection.cursor()
        add_user_data = 'INSERT INTO user_data (user_id, name, email, age) VALUES (%s, %s, %s, %s)'

        with open(data, mode='r') as file:
            csvfile = csv.DictReader(file)
            for line in csvfile:
                user_id = str(uuid.uuid4())  # generate UUID
                values = (user_id, line['name'], line['email'], line['age'])
                cursor.execute(add_user_data, values)

        connection.commit()
        print("Data inserted successfully.")

    except Exception as e:
        print("Error inserting data:", e)

