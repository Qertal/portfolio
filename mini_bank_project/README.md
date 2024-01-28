**Database Description:**

The provided script outlines the creation of a relational database named "project_bank." 
This database appears to be designed for managing financial transactions, client information, 
currency exchange rates, and fixed-term deposits. It incorporates various tables, triggers, stored procedures, 
functions, views, and events to facilitate the organization and retrieval of financial data.

### **Tables:**

1. **Clients Table (`klienci`):**
   - Stores client information such as login, first name, last name, email, date of birth, address, etc.

2. **Currencies Table (`waluty`):**
   - Contains information about different currencies, each identified by a unique symbol.

3. **Transactions Table (`transakcje`):**
   - Represents transaction types, including 'Kupno' (Purchase) and 'Sprzedaz' (Sale).

4. **Terms Table (`terminy`):**
   - Specifies different term periods in months for financial products.

5. **NBP Exchange Rate Table (`kurs_nbp`):**
   - Stores National Bank of Poland (NBP) exchange rates for different term periods.

6. **Currency Exchange Rates Table (`kurs_walut`):**
   - Manages currency exchange rates, considering transaction types and validity.

7. **Products Table (`produkty`):**
   - Contains financial product information with interest rates for various term periods.

8. **Status Table (`status`):**
   - Records status information, such as 'Odblokowane' (Unblocked) and 'Zablokowane' (Blocked).

9. **Fixed-Term Deposits Table (`depozyty_terminowe`):**
   - Captures details of fixed-term deposits, including deposit amounts, terms, and statuses.

10. **Currency Transactions Table (`transakcje_walutowe`):**
    - Manages details of currency transactions, including deposited and withdrawn amounts.

11. **Currency Profit Table (`zysk_waluty`):**
    - Records profits from currency transactions.

### **Triggers:**

1. **Auto-generate Email Trigger (`dopisz_email`):**
   - Automatically generates and assigns an email address for each new client based on specific criteria.

2. **Calculate Currency Profit Trigger (`zysk`):**
   - Calculates and records profits for each currency transaction.

### **Stored Procedures:**

1. **Create New Client (`nowy_klient`):**
   - Creates a new client entry with a unique login based on specific conditions.

2. **Create New Currency Exchange Rate (`nowy_kurs`):**
   - Updates and inserts currency exchange rates based on provided parameters.

3. **Create New Currency Transaction (`nowa_transakcja`):**
   - Facilitates the creation of new currency transactions, considering currency rates and types.

4. **Create New Fixed-Term Deposit (`nowy_depozyt`):**
   - Creates a new fixed-term deposit entry with relevant details and calculates withdrawal amounts.

5. **Check and Update Deposit Status (`sprawdz_date`):**
   - Checks and updates the status of fixed-term deposits based on their end dates.

### **Functions:**

1. **Calculate Currency Transaction Amount (`przelicz`):**
   - Calculates currency transaction amounts based on provided parameters.

2. **Calculate Deposit Amount (`licz_depozyt`):**
   - Iteratively calculates the deposit amount over a specified time period with compounding interest.

### **Views:**

1. **Current Currency Exchange Rates View (`aktualne_kursy`):**
   - Selects and displays information about current currency exchange rates.

2. **Latest Currency Transactions View (`ostatnie_transakcje`):**
   - Retrieves and displays information about the latest currency transactions.

3. **Fixed-Term Deposits View (`depozyty`):**
   - Compiles information about fixed-term deposits, including client details and financial information.

### **Events:**

1. **Scheduled Event (`sprawdzanie_depozytow`):**
   - Scheduled to run daily, checks and updates the status of fixed-term deposits based on their end dates.

### **Indexes:**

1. **Index on Deposit Term ID (`idx_id_terminy`):**
   - Optimizes queries involving deposit terms in the 'depozyty_terminowe' table.

2. **Index on Transaction ID (`idx_id_transakcje`):**
   - Optimizes queries involving transactions in the 'transakcje' table.

### **Partitioned Table:**

1. **Partitioned Currency Exchange Rate Table (`kurs_walut_partycja`):**
   - Utilizes LIST partitioning on the 'id_waluty' column for efficient data retrieval.

### **Event Scheduler:**

- The event scheduler is enabled globally, allowing scheduled events to be executed.

### **Additional Procedure:**

1. **Generate Multiple Exchange Rates (`duzo_kursow`):**
   - Calls the 'nowy_kurs' procedure multiple times to insert additional exchange rates.

### **Check Partitioned Table Rows:**

- Checks the number of rows in the partitioned table 'kurs_walut_partycja.'

---

This relational database appears comprehensive and is tailored for managing various financial aspects, including client data, currency exchange rates, 
transactions, fixed-term deposits, and associated calculations. The use of triggers, stored procedures, functions, views, 
and events enhances the functionality and automation of financial processes within the system. 
The provided script showcases a well-structured schema with a focus on data integrity and efficiency.
