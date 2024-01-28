# Paweł Drzyzga, Patryk Doniec, Justyna Bartyzel

create database project_bank;

use project_bank;


### TABLES

##TABELA KLIENCI
create or replace table klienci(
login varchar(10) primary key,
first_name varchar(100),
last_name varchar(100),
email varchar(100),
date_birth date,
PostalCode varchar(100),
phone_number varchar (50),
City varchar(100),
address varchar(200));

##TABELA WALUTY
create or replace table waluty(
id_waluty int auto_increment primary key,
symbol_waluty varchar(10));


insert into waluty(id_waluty, symbol_waluty) values (1,"EUR");
insert into waluty(id_waluty, symbol_waluty) values (2,"USD");
insert into waluty(id_waluty, symbol_waluty) values (3,"NOK");
insert into waluty(id_waluty, symbol_waluty) values (4,"CZK");


##TABELA TRANSAKCJE
create or replace table transakcje(
id_transakcje int auto_increment primary key, 
nazwa varchar(40));


insert into transakcje (nazwa) values ('Kupno'),('Sprzedaz');


##TABELA TERMIMNY
create or replace table terminy(
id_terminy int auto_increment primary key,
ilosc_miesiecy int);


insert into terminy(id_terminy, ilosc_miesiecy) values (1, 1);
insert into terminy(id_terminy, ilosc_miesiecy) values (2, 3);
insert into terminy(id_terminy, ilosc_miesiecy) values (3, 9);
insert into terminy(id_terminy, ilosc_miesiecy) values (4, 12);


##TABELA KURS_NBP
create or replace table kurs_nbp(
id_kurs_nbp int auto_increment primary key,
oprocentowanie double,
id_terminy int, 
foreign key (id_terminy)references terminy(id_terminy)
);


insert into kurs_nbp(oprocentowanie, id_terminy) values (5.70, 1);
insert into kurs_nbp(oprocentowanie, id_terminy) values (5.60, 2);
insert into kurs_nbp(oprocentowanie, id_terminy) values (5.55, 3);
insert into kurs_nbp(oprocentowanie, id_terminy) values (5.40, 4);



create or replace table kurs_walut(
id_kurs_walut int auto_increment primary key,
kurs double,
id_waluty int,
id_transakcje int,
waznosc bool,
foreign key (id_waluty)references waluty(id_waluty),
foreign key (id_transakcje)references transakcje(id_transakcje)
);

##TABELA PRODUKTY
create or replace table produkty(
id_produktu int auto_increment primary key,
oprocentowanie double,
id_terminy int,
foreign key (id_terminy) references terminy(id_terminy)
);



insert into produkty (oprocentowanie, id_terminy) values (0.0525,1);
insert into produkty (oprocentowanie, id_terminy) values (0.05,2);
insert into produkty (oprocentowanie, id_terminy) values (0.045,3);
insert into produkty (oprocentowanie, id_terminy) values (0.04,4);


##TABELA STATUS
create or replace table status(
id_status int primary key auto_increment,
nazwa_status varchar(50)
);


insert into status (nazwa_status) values
("Odblokowane"),
("Zablokowane");


##TABELA DEPOZYTY TERMINOWE
create or replace table depozyty_terminowe(
id_depozyty int auto_increment primary key,
kwota_wplacona float,
id_terminy int,
data_rozpoczecia date,
data_zakonczenia date,
id_produkty int,
id_status int,
login varchar(10),
kwota_wyplacana float,
foreign key (id_terminy) references terminy(id_terminy),
foreign key (id_produkty) references produkty(id_produktu),
foreign key (login) references klienci(login),
foreign key (id_status) references status(id_status)
);

##TABELA TRANSAKCJE WALUTOWE
create or replace table transakcje_walutowe(
id_trans_wal int auto_increment primary key,
login varchar(10),
kwota_wplacona float,
kwota_wyplacona float,
data_wpisu date,
id_transakcje int,
id_kurs_walut int,
foreign key (login) references klienci(login),
foreign key (id_transakcje) references transakcje(id_transakcje),
foreign key (id_kurs_walut) references kurs_walut(id_kurs_walut)
);

##TABELA ZYSK_Z_WALUT
create or replace table zysk_waluty(
id_zysk_trans int auto_increment primary key,
login varchar(10),
zysk float,
id_trans_wal int,
foreign key (login) references klienci(login),
foreign key (id_trans_wal) references transakcje_walutowe(id_trans_wal)
);


###TRIGGERY


/* this trigger automatically generates and assigns an email address for each new client being inserted into 
the "klienci" table based on their first name, last name, login, and the specified domain. */

create or replace trigger dopisz_email 
before insert on klienci
for each row
begin
  SET new.email = lower(CONCAT(new.first_name, '.', new.last_name, new.login, '@BDDInvestments.com'));
end;


/*
This trigger is designed to execute after an insertion operation on the "transakcje_walutowe" table for each row. 
It calculates the profit ("zysk") based on the type of transaction ("Kupno" or "Sprzedaz") and inserts the relevant 
information into the "zysk_waluty" table. The trigger uses variables to store intermediate values, such as the transaction ID, 
currency exchange rate, user login, and calculated profit. 
*/

create or replace trigger zysk
after insert on transakcje_walutowe
for each row
begin 
	declare vid_transakcje int;
	declare zysk float;
	declare vKurs float;
	declare vlogin varchar(50);
	set vid_transakcje = (select t.id_transakcje  from transakcje t where t.nazwa  like 'Kupno');
	set vKurs = (select kw.kurs from kurs_walut kw where kw.id_kurs_walut = new.id_kurs_walut);
	set vlogin = (select login from transakcje_walutowe tw order by tw.id_trans_wal desc limit 1);
	if (new.id_transakcje = vid_transakcje) then
		set zysk = new.kwota_wplacona*0.05;
	else 
		set zysk = new.kwota_wyplacona*0.05;
	end if;
	insert into zysk_waluty (login,zysk,id_trans_wal) values (vlogin,round(zysk,2),new.id_trans_wal);
end;


/* Procedura ktora bedzie generowala login. Po pierwsze, musi ona przyjmowac wartosci imie, nazwisko,
 * data urodzenia, kod pocztowy, numer telefonu, miasto, adres. Za pomoca daty bedziemy generowac login.
 * np wezmiemy date i dodamy do niej 1, bo to przekonwertuje date na liczbe. Nastepnie tworzymy petle 
 * ze zmienna z true w warunku, no i w srodku najpierw instrukcja warunkowa sprawadza ostatnia literke imienia
 * jeśli to jest a to jest to kobieta, w srodku tego robimy kolejna instrukcje warunkowa, ktora bedzie
 * sprawdzac ta liczbe dzialaniem %2, jesli da wynik 0, to sprawdzamy czy w calej tabeli istnieje taki login, 
 * jesli tak to dodajemy 2 i powtarzamy operacje sprawdzania, do skutku. jesli juz nie bedzie to zapisujemy
 * ta liczbe jako login. analogicznie trzeba zrobic w momencie kiedy ostatnia litera nie bedzie a.
 */

# ADDING NEW CLIENT

/*
This stored procedure, named "nowy_klient," is designed to create a new client entry in the "klienci" table with a unique login. 
The uniqueness of the login is determined based on the conditions related to the client's first name and whether 
it contains the letter 'a'. The procedure generates a login value by concatenating the current date, time, and a constant, 
and then it iterates until finding a unique login according to the specified conditions. 
The new client information is then inserted into the "klienci" table.
*/


create or replace procedure nowy_klient(
in vfirst_name varchar(50),
in vlast_name varchar(50),
in vdate_birth varchar(50),
in vPostalcode varchar(50),
in vphone_number varchar(20),
in vCity varchar(50),
in vaddress varchar(50)
)
begin 
	declare vlogin INT;
	declare petla bool;
	set petla = true;
	set vlogin = curdate()+1+curtime()+1;
	while petla DO
		if vfirst_name LIKE '%a' and vlogin%2=0 then
			while (length((select login from klienci where login like vlogin))!=0) DO
				set vlogin=vlogin+2;
			end while;
			insert into klienci(login,first_name,last_name,date_birth,Postalcode,phone_number,City,address)
			values (replace(format(vlogin,0),',',''),vfirst_name,vlast_name,vdate_birth,vPostalcode,vphone_number,vCity,vaddress);
			set petla = false;
		elseif vfirst_name LIKE '%a' and vlogin%2=1 then
			set vlogin=vlogin+1;
			while length((select login from klienci where login like vlogin))!=0 DO
				set vlogin=vlogin+2;
			end while;	
			insert into klienci(login,first_name,last_name,date_birth,Postalcode,phone_number,City,address)
			values (replace(format(vlogin,0),',',''),vfirst_name,vlast_name,vdate_birth,vPostalcode,vphone_number,vCity,vaddress);
			set petla = false;
		elseif vfirst_name not like '%a' and vlogin%2=0 then
			set vlogin=vlogin+1;
			while length((select login from klienci where login like vlogin))!=0 DO
				set vlogin=vlogin+2;
			end while;	
			insert into klienci(login,first_name,last_name,date_birth,Postalcode,phone_number,City,address)
			values (replace(format(vlogin,0),',',''),vfirst_name,vlast_name,vdate_birth,vPostalcode,vphone_number,vCity,vaddress);
			set petla = false;
		elseif vfirst_name not like '%a' and vlogin%2=1 then
			while length((select login from klienci where login like vlogin))!=0 DO
				set vlogin=vlogin+2;
			end while;	
			insert into klienci(login,first_name,last_name,date_birth,Postalcode,phone_number,City,address)
			values (replace(format(vlogin,0),',',''),vfirst_name,vlast_name,vdate_birth,vPostalcode,vphone_number,vCity,vaddress);
			set petla = false;
		end if;
	end while;
				
end;


/*
This stored procedure, named "nowy_kurs," is designed to update and insert currency exchange rates based on the provided parameters. 
It retrieves the transaction and currency IDs, invalidates existing rates for the specified currency, 
and inserts a new rate with the given values. Additionally, it adjusts rates for opposite transactions 
(e.g., 'Sprzedaz' and 'Kupno') by inserting new rates with adjusted values.
*/

create or replace procedure nowy_kurs(
in vKurs double,
in vSymbol varchar(3),
in vTransakcja varchar(15)
)
begin 
	declare vid_transakcja int;
	declare vid_waluty int;
	set vid_transakcja = (select id_transakcje from transakcje where nazwa like vTransakcja);
	set vid_waluty = (select id_waluty from waluty where symbol_waluty like vSymbol);
	update kurs_walut set waznosc = false
	where id_waluty=vid_waluty;
	insert into kurs_walut (kurs,id_waluty,id_transakcje,waznosc) 
	values (vKurs, vid_waluty,vid_transakcja,true);
	if vTransakcja like 'Sprzedaz' then
		insert into kurs_walut (kurs,id_waluty,id_transakcje,waznosc) 
		values (vKurs+0.05, vid_waluty,(select id_transakcje from transakcje where nazwa not like vTransakcja),true);
	elseif vTransakcja like 'Kupno' then
		insert into kurs_walut (kurs,id_waluty,id_transakcje,waznosc) 
		values (vKurs+0.05, vid_waluty,(select id_transakcje from transakcje where nazwa not like vTransakcja),true);
	end if;
end;

/*
The stored procedure named "nowa_transakcja" is designed to facilitate the creation of new currency transactions. 
It retrieves the necessary information, such as currency ID, transaction ID, and the valid currency exchange rate ID, 
based on the provided parameters. The procedure then calculates the withdrawn amount using a custom function ("przelicz") 
and inserts a new record into the "transakcje_walutowe" table, capturing details such as login, deposited amount, 
withdrawn amount, date of entry, transaction ID, and currency exchange rate ID.
*/



create or replace procedure nowa_transakcja(
in vlogin varchar(40),
in vwplacona_kwota double,
in vTransakcja varchar(15),
in vSymbol varchar(3))
begin
	declare vid_waluty int;
	declare vid_transakcje int;
	declare vKurs double;
	declare vwyplacona_kwota float;
	declare vid_kurs_walut int;
	set vid_waluty = (select id_waluty from waluty where waluty.symbol_waluty like vSymbol);
	set vid_transakcje = (select id_transakcje from transakcje where transakcje.nazwa like vTransakcja);
	set vid_kurs_walut = (select kurs_walut.id_kurs_walut from kurs_walut 
	where kurs_walut.id_waluty = vid_waluty and kurs_walut.id_transakcje = vid_transakcje
	and waznosc = true);
	set vKurs = (select kurs_walut.kurs from kurs_walut where id_kurs_walut = vid_kurs_walut);
	set vwyplacona_kwota = round((select przelicz(vKurs, vwplacona_kwota, vTransakcja)),2);
-- 	select vwyplacona_kwota;
	insert into transakcje_walutowe (login, kwota_wplacona, kwota_wyplacona, data_wpisu, id_transakcje,
	id_kurs_walut) values
	(vlogin,vwplacona_kwota,vwyplacona_kwota, CURDATE(), vid_transakcje, vid_kurs_walut);
end;


### FUNKCJA PRZELICZ

/*
The function named "przelicz" takes three parameters: "kurs" (exchange rate), "kwota" (amount), and "transakcja" (transaction type). 
It calculates and returns the result based on the provided exchange rate and transaction type. If the transaction type is 'Kupno' (Purchase), 
the function returns the result of multiplying the exchange rate by the amount, rounded to two decimal places. 
If the transaction type is 'Sprzedaz' (Sale), the function returns the result of dividing the amount by the exchange rate, also rounded to two decimal places.
*/

create or replace function przelicz(kurs float, kwota float, transakcja varchar(20))
returns float 
begin
	if transakcja like 'Kupno' then 
		return round((kurs * kwota),2);
	elseif transakcja like 'Sprzedaz' then 
		return round((kwota / kurs),2);
	end if;
end;


/*
The function named "licz_depozyt" takes three parameters: "kwota" (initial deposit amount), 
"oprocentowanie" (interest rate), and "czas" (time in months). It iteratively calculates 
the deposit amount over the specified time period based on the given interest rate, assuming interest is compounded monthly. 
The function then returns the result, rounded to two decimal places.
*/

create or replace function licz_depozyt(kwota float, oprocentowanie double, czas int) returns float
begin 
	while (czas > 0) DO
		set kwota = kwota + kwota*oprocentowanie/12;
		set czas = czas-1;
	end while;
	return round(kwota,2);
end;	

/*
The stored procedure named "nowy_depozyt" is designed to create a new fixed-term deposit. 
It retrieves necessary information, such as the ID of the deposit term, product, interest rate, and status, 
based on the provided parameters. It then calculates the amount to be withdrawn at the end of the deposit 
term using the "licz_depozyt" function. Finally, the procedure inserts a new record into the "depozyty_terminowe" 
table with details including the deposited amount, term ID, start and end dates, product ID, status ID, user login, 
and the calculated withdrawal amount.
*/

create or replace procedure nowy_depozyt(
in vlogin varchar(10),
in vkwota float,
in vczas int # chcemy zeby to byla po prostu liczba miesiecy
)
begin 
	declare voprocentowanie double;
	declare vid_terminy int;
	declare vkwota_wyplacana float;
	declare vid_produkty int;
	declare vid_status int;
	set vid_terminy = (select id_terminy from terminy t where t.ilosc_miesiecy=vczas);
	set vid_produkty = (select p.id_produktu from produkty p where p.id_terminy =vid_terminy);
	set voprocentowanie = (select p.oprocentowanie from produkty p where p.id_produktu = vid_produkty);
	set vid_status = (select s.id_status from status s where nazwa_status like 'Zablokowane');
	set vkwota_wyplacana = (select licz_depozyt(vkwota,voprocentowanie,vczas));
	insert into depozyty_terminowe
	(kwota_wplacona,id_terminy,data_rozpoczecia,data_zakonczenia,id_produkty,id_status,login,kwota_wyplacana)
	values
	(vkwota,vid_terminy,CURDATE(),(select date_add(CURDATE(),interval 1 MONTH)),vid_produkty,vid_status,vlogin,
	vkwota_wyplacana);

end;



/*
The stored procedure named "sprawdz_date" is designed to check and update the status of fixed-term deposits. 
It retrieves the ID of the 'Odblokowane' status from the "status" table. Subsequently, 
it updates the status of fixed-term deposits in the "depozyty_terminowe" table where the end date is on or before 
the current date to the retrieved status ID. This is a mechanism to ensure that deposits are updated or unblocked based on their end dates.
*/

create or replace procedure sprawdz_date()
begin 
	declare vid_status int;
	set vid_status = (select id_status from status s where s.nazwa_status like 'Odblokowane');
	update depozyty_terminowe set depozyty_terminowe.id_status = vid_status where data_zakonczenia <= curdate();
end;

# show variables like 'event_scheduler';

/*
The statement SET GLOBAL event_scheduler = ON; globally enables the event scheduler, allowing scheduled events to be executed.
 */

set global event_scheduler = on;

/*
This event is scheduled to run every day starting from January 10, 2024, at midnight (00:00:00). T
he event executes the stored procedure sprawdz_date() as its action, 
checking and updating the status of fixed-term deposits based on their end dates.
*/

create or replace event sprawdzanie_depozytow
on schedule every 1 day
STARTS TIMESTAMP('2024-01-10 00:00:00')
do
begin 
	call sprawdz_date();
end;


/*
This view selects and displays information about current currency exchange rates. 
The view includes columns for currency symbol ('Waluta'), exchange rate in Polish zlotys ('Kurs [zl]'), 
and the type of transaction ('Rodzaj transakcji'). The view is constructed by joining the 'kurs_walut,' 'waluty,' and 'transakcje' 
tables based on their corresponding IDs. The condition waznosc = TRUE filters only the valid (current) exchange rates.
*/

create or replace view aktualne_kursy as select waluty.symbol_waluty as Waluta, kurs_walut.kurs as 'Kurs [zl]',
transakcje.nazwa as 'Rodzaj transakcji' from kurs_walut
inner join waluty on kurs_walut.id_waluty = waluty.id_waluty 
inner join transakcje on kurs_walut.id_transakcje = transakcje.id_transakcje 
where waznosc = true;

/*
The view retrieves and displays information about the latest currency transactions. 
It provides details about clients, currencies, exchange rates, and transaction types. 
The view includes columns such as 'Imie' (First name), 'Nazwisko' (Last name), 'Email' (Email address), 
'Waluta' (Currency symbol), 'Kurs' (Exchange rate), 'Rodzaj transakcji' (Transaction type), 'Kwota wplacona' (Deposited amount), 
'Kwota wyplacona' (Withdrawn amount), and 'Data wpisu' (Date of transaction entry).
*/

create or replace view ostatnie_transakcje as 
select k.first_name as Imie, k.last_name as Nazwisko, k.email as Email, w.symbol_waluty as 'Waluta',
kw.kurs as Kurs, t.nazwa as 'Rodzaj transakcji',tw.kwota_wplacona as 'Kwota wplacona', 
tw.kwota_wyplacona as 'Kwota wyplacona' ,tw.data_wpisu as 'Data wpisu'
from transakcje_walutowe tw
inner join klienci k on tw.login = k.login
inner join kurs_walut kw on tw.id_kurs_walut = kw.id_kurs_walut
inner join waluty w on kw.id_waluty = w.id_waluty
inner join transakcje t on tw.id_transakcje = t.id_transakcje 
order by tw.id_trans_wal 
desc limit 10;

/*
This view compiles information about fixed-term deposits, including details about clients, 
deposit terms, products, status, and financial details. The view includes the following columns:
*/

create or replace view depozyty as 
select
k.first_name Imie,k.last_name Nazwisko,k.email Email,dt.data_rozpoczecia 'Data wplaty', 
dt.data_zakonczenia 'Data wyplaty', dt.kwota_wplacona 'Wplata', p.oprocentowanie Oprocentowanie,
dt.kwota_wyplacana 'Wyplata', s.nazwa_status Status
from depozyty_terminowe dt 
inner join terminy t on dt.id_terminy = t.id_terminy
inner join produkty p on dt.id_produkty = p.id_produktu 
inner join status s on dt.id_status = s.id_status 
inner join klienci k on dt.login = k.login;


/*
This statement creates or replaces an index named 'idx_id_terminy' on the 'depozyty_terminowe' table. 
The index is specifically created on the 'id_terminy' column. Indexing on this column aims to enhance 
the performance of queries involving search, filtering, or sorting based on deposit terms. 
It improves data retrieval efficiency by providing faster access to rows based on the indexed column.
*/

create or replace index idx_id_terminy on depozyty_terminowe(id_terminy);

/*
This statement creates or replaces an index named 'idx_id_transakcje' on the 'transakcje' table.
*/

create or replace index idx_id_transakcje on transakcje(id_transakcje);


create or replace procedure duzo_kursow(
	in vilosc int
)
BEGIN
	declare i int;
	set i = 0;
	while (i < vilosc) DO
		call nowy_kurs(4.02,'USD','Kupno');
		call nowy_kurs(4.70,'EUR','Kupno');
		call nowy_kurs(0.38,'NOK','Kupno');
		call nowy_kurs(0.18,'CZK','Kupno');
		set i = i+1;
	end while;
END;

call duzo_kursow(10);

/*
This SQL statement creates a table named 'kurs_walut_partycja' using the InnoDB storage engine. 
The table has five columns: 'id_kurs_walut,' 'kurs,' 'id_waluty,' 'id_transakcje,' and 'waznosc.'

The table utilizes LIST partitioning on the 'id_waluty' column, dividing the data into partitions based on specified values. 
In this case, there are four partitions ('p1,' 'p2,' 'p3,' and 'p4') corresponding to distinct values of 'id_waluty' (1, 2, 3, and 4).

This partitioning scheme can help optimize queries that involve filtering or searching based on the 'id_waluty' column, 
as it allows for more efficient data retrieval within each partition.
*/

CREATE or replace TABLE kurs_walut_partycja (
id_kurs_walut INT NOT NULL,
kurs double NOT NULL,
id_waluty INT NOT NULL,
id_transakcje int NOT NULL,
waznosc int NOT NULL
) ENGINE=InnoDB
PARTITION BY LIST(id_waluty) (
	PARTITION p1 VALUES IN (1),
	PARTITION p2 VALUES IN (2),
	PARTITION p3 VALUES IN (3),
	PARTITION p4 VALUES IN (4)
	);
/*
SQL statement inserts data into the partitioned table 'kurs_walut_partycja' by selecting data from the non-partitioned table 'kurs_walut.' 
It copies values from the columns 'id_kurs_walut,' 'kurs,' 'id_waluty,' 'id_transakcje,' and 'waznosc.'
*/

INSERT INTO kurs_walut_partycja (id_kurs_walut, kurs, id_waluty, id_transakcje, waznosc)
SELECT id_kurs_walut, kurs, id_waluty, id_transakcje, waznosc
FROM kurs_walut;

SELECT table_name, table_rows
FROM information_schema.partitions
WHERE table_schema = 'projekt_bank' AND table_name = 'kurs_walut_partycja';

