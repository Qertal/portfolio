create database bank;

use bank;

create table not_checked_transactions(
id_not_checked_transactions int,
Time double,
V1 double,
V2 double,
V3 double,
V4 double,
V5 double,
V6 double,
V7 double,
V8 double,
V9 double,
V10 double,
V11 double,
V12 double,
V13 double,
V14 double,
V15 double,
V16 double,
V17 double,
V18 double,
V19 double,
V20 double,
V21 double,
V22 double,
V23 double,
V24 double,
V25 double,
V26 double,
V27 double,
V28 double,
Amount double
);

create table status(
id_status int primary key,
name varchar(10));

insert into status (id_status,name)
values
(0,'Not fraud'),
(1,'Fraud');

create table checked_transactions(
id_checked_transactions int,
Time double,
V1 double,
V2 double,
V3 double,
V4 double,
V5 double,
V6 double,
V7 double,
V8 double,
V9 double,
V10 double,
V11 double,
V12 double,
V13 double,
V14 double,
V15 double,
V16 double,
V17 double,
V18 double,
V19 double,
V20 double,
V21 double,
V22 double,
V23 double,
V24 double,
V25 double,
V26 double,
V27 double,
V28 double,
Amount double,
`status` int,
foreign key (`status`) references status(id_status)
);

LOAD DATA INFILE '/docker-entrypoint-initdb.d/test.csv'
INTO TABLE not_checked_transactions 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

create table clients(
id_client int primary key,
FirstName varchar(30),
LastName varchar(30),
Addres varchar(30),
Postcode varchar(30),
email varchar(80)
);



CREATE table transactions(
id_checked_transactions int,
id_client int,
foreign key (id_client) references clients(id_client)
);

DELIMITER //

CREATE trigger new_email
before insert on clients
for each ROW 
BEGIN 
	set new.email = CONCAT(new.FirstName,'.',new.LastName,new.id_client,'@BankQ.com');
END//

DELIMITER ;


INSERT INTO clients (id_client, FirstName, LastName, Addres, Postcode)
VALUES
(1, 'John', 'Doe', '123 Main St', '12345'),
(2, 'Jane', 'Smith', '456 Oak Ave', '54321'),
(3, 'Bob', 'Johnson', '789 Pine Ln', '67890'),
(4, 'Alice', 'Williams', '101 Maple Blvd', '09876'),
(5, 'Charlie', 'Davis', '202 Elm Dr', '13579'),
(6, 'Eva', 'Martinez', '303 Cedar St', '24680'),
(7, 'Frank', 'Taylor', '404 Birch Rd', '75319'),
(8, 'Grace', 'Miller', '505 Redwood Ave', '86420'),
(9, 'Henry', 'Brown', '606 Walnut Ln', '97135'),
(10, 'Ivy', 'Clark', '707 Sycamore Dr', '46802'),
(11, 'Jack', 'White', '808 Cedar Rd', '15937'),
(12, 'Katie', 'Moore', '909 Pine Ave', '24680'),
(13, 'Leo', 'Jackson', '1010 Oak St', '35791'),
(14, 'Mia', 'Garcia', '1111 Birch Blvd', '46802'),
(15, 'Noah', 'Lopez', '1212 Maple Ln', '57913');

DELIMITER //
create trigger checkin after insert on checked_transactions for EACH ROW 
BEGIN 
	declare vid_client int;
	delete from not_checked_transactions 
	where id_not_checked_transactions = new.id_checked_transactions;
	set vid_client = (SELECT FLOOR(1 + RAND() * 15));
	insert into transactions values (new.id_checked_transactions,vid_client);
END//

DELIMITER ;

create view frauds as
select c.id_client as `Id of client`, c.FirstName as `Firstname`, c.`LastName` as Lastname,
CONCAT(c.Addres, ', ', c.Postcode) AS Address,ct.id_checked_transactions AS 'Id of transaction'
from transactions t 
inner join clients c on t.id_client=c.id_client
inner join checked_transactions ct on t.id_checked_transactions = ct.id_checked_transactions
inner join status s on s.id_status = ct.status
where ct.status = 1;