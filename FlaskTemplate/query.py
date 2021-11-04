import pyodbc
import os
sqlResponse = []
with pyodbc.connect(os.environ['ConnectionString']) as conn:
    with conn.cursor() as cursor:
        cursor.execute("SELECT [CustomerID],[Title],[FirstName],[MiddleName],[LastName],[CompanyName],[EmailAddress],[Phone] FROM [SalesLT].[Customer] WHERE [CustomerID] < '21'")
        row = cursor.fetchone()
        while row is not None:
            sqlResponse.append('<tr>')
            for i in row:
                sqlResponse.append(f'<td>{i}</td>')
            sqlResponse.append('</tr>')
            row = cursor.fetchone()

print(*sqlResponse[:])