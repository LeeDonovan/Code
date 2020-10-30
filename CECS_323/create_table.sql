CREATE TABLE Shift(
    dayOfWeek varchar(50) NOT NULL,
    typeOfShift varchar(50) NOT NULL,
    PRIMARY KEY (dayOfWeek, typeOfShift)
);

CREATE TABLE Staff(
    dayOfWeek varchar(50) NOT NULL,
    typeOfShift varchar(50) NOT NULL,
    staffID int NOT NULL,
    staffFirstName varchar(50),
    staffLastName varchar(50),
    staffPhone varchar(20),
    staffDOB date,
    PRIMARY KEY (staffID),
    FOREIGN KEY (dayOfWeek, typeOfShift) REFERENCES Shift(dayOfWeek, typeOfShift)
);

CREATE UNIQUE INDEX staffuid on Staff(staffFirstName, staffLastName, staffPhone);

CREATE TABLE Vacation(
    staffID int NOT NULL,
    startDate date NOT NULL,
    endDate date,
    reason varchar(150),
    PRIMARY KEY (staffID, startDate),
    FOREIGN KEY (staffID) REFERENCES Staff(staffID)
);

CREATE TABLE Chef(
    staffID int NOT NULL,
    salary double,
    PRIMARY KEY (staffID),
    FOREIGN KEY (staffID) REFERENCES Staff(staffID)
);

CREATE TABLE MaitreD(
    staffID int NOT NULL,
    hourlyRate double,
    PRIMARY KEY (staffID),
    FOREIGN KEY (staffID) REFERENCES Staff(staffID)
);

CREATE TABLE WaitStaff(
    staffID int NOT NULL,
    hourlyRate double,
    PRIMARY KEY (staffID),
    FOREIGN KEY (staffID) REFERENCES Staff(staffID)
);

CREATE TABLE Tables(
    staffID int NOT NULL,
    tableNumber int NOT NULL,
    PRIMARY KEY (tableNumber),
    FOREIGN KEY (staffID) REFERENCES Staff(staffID)
);

CREATE TABLE Dishwasher(
    staffID int NOT NULL,
    hourlyRate double,
    PRIMARY KEY (staffID),
    FOREIGN KEY (staffID) REFERENCES Staff(staffID)
);

CREATE TABLE Manager(
    staffID int NOT NULL,
    salary double,
    PRIMARY KEY (staffID),
    FOREIGN KEY (staffID) REFERENCES Staff(staffID)
);

CREATE TABLE HealthBenefitsChef(
    staffID int NOT NULL,
    healthCareBenefit varchar(50) NOT NULL,
    PRIMARY KEY (staffID, healthCareBenefit),
    FOREIGN KEY (staffID) REFERENCES Chef(staffID)
);

CREATE TABLE HealthBenefitsManager(
    staffID int NOT NULL,
    healthCareBenefit varchar(50) NOT NULL,
    PRIMARY KEY (staffID, healthCareBenefit),
    FOREIGN KEY (staffID) REFERENCES Manager(staffID)
);

CREATE TABLE HeadChef(
    staffID int NOT NULL,
    PRIMARY KEY (staffID),
    FOREIGN KEY (staffID) REFERENCES Chef(staffID)
);

CREATE TABLE SousChef(
    staffID int NOT NULL,
    PRIMARY KEY (staffID),
    FOREIGN KEY (staffID) REFERENCES Chef(staffID)
);

CREATE TABLE LineCook(
    staffID int NOT NULL,
    PRIMARY KEY (staffID),
    FOREIGN KEY (staffID) REFERENCES Chef(staffID)
);

CREATE TABLE Recipe(
    staffID int NOT NULL,
    recipeName varchar(50) NOT NULL,
    PRIMARY KEY (staffID, recipeName),
    FOREIGN KEY (staffID) REFERENCES HeadChef(staffID)
);

CREATE TABLE Station(
    stationName varchar(30) NOT NULL,
    PRIMARY KEY (stationName)
);

CREATE TABLE StationCook(
    staffID int NOT NULL,
    stationName varchar(30) NOT NULL,
    PRIMARY KEY (staffID, stationName),
    FOREIGN KEY (staffID) REFERENCES LineCook(staffID),
    FOREIGN KEY (stationName) REFERENCES Station(stationName)
);

CREATE TABLE Menu(
    menuType varchar(30) NOT NULL,
    PRIMARY KEY (menuType)
);

CREATE TABLE SpiceLevel(
    spiceLevel varchar(20) NOT NULL,
    PRIMARY KEY (spiceLevel)
);

CREATE TABLE MenuItem(
    itemName varchar(40) NOT NULL,
    spiceLevel varchar(20) NOT NULL,
    PRIMARY KEY (itemName, spiceLevel),
    FOREIGN KEY (spiceLevel) REFERENCES SpiceLevel(spiceLevel)
);

CREATE TABLE Meat(
    meatType varchar(30) NOT NULL,
    PRIMARY KEY (meatType)
);

CREATE TABLE Entree(
    itemName varchar(40) NOT NULL,
    meatType varchar(30) NOT NULL,
    PRIMARY KEY (itemName, meatType),
    FOREIGN KEY (itemName) REFERENCES MenuItem(itemName),
    FOREIGN KEY (meatType) REFERENCES Meat(meatType)
);

CREATE TABLE Appetizer(
    itemName varchar(40) NOT NULL,
    PRIMARY KEY (itemName),
    FOREIGN KEY (itemName) REFERENCES MenuItem(itemName)
);

CREATE TABLE Soup(
    itemName varchar(40) NOT NULL,
    volume varchar(20) NOT NULL,
    PRIMARY KEY (itemName, volume),
    FOREIGN KEY (itemName) REFERENCES MenuItem(itemName)
);

CREATE TABLE MeatEntree(
    itemName varchar(40),
    meatType varchar(30) NOT NULL,
    PRIMARY KEY (meatType),
    FOREIGN KEY (itemName) REFERENCES MenuItem(itemName)
);

CREATE TABLE ItemMenu(
    itemName varchar(40) NOT NULL,
    menuType varchar(30) NOT NULL,
    price double,
    portion varchar(40),
    PRIMARY KEY(itemName, menuType),
    FOREIGN KEY(itemName) REFERENCES MenuItem(itemName),
    FOREIGN KEY(menuType) REFERENCES Menu(menuType)
);


CREATE TABLE Customer(
    custID int NOT NULL,
    custFirstName varchar(40),
    custLastName varchar(40),
    custAddress varchar(100),
    custDOB date, 
    mimingMoney int,
    custEmail varchar(60),
    PRIMARY KEY(custID)
);

CREATE UNIQUE INDEX custuid on Customer(custFirstName, custLastName, custAddress);

CREATE TABLE Corporation(
    custID int NOT NULL,
    corpName varchar(50) NOT NULL,
    orgName varchar(50),
    officeAddress varchar(100),
    contactEmail varchar(100),
    PRIMARY KEY(custID, corpName),
    FOREIGN KEY(custID) REFERENCES Customer(custID)
);

CREATE TABLE Mentorship(
    itemName varchar(40) NOT NULL,
    staffID int NOT NULL,
    mentorID int NOT NULL,
    startDate date NOT NULL,
    endDate date,
    PRIMARY KEY(itemName, staffID, mentorID, startDate),
    FOREIGN KEY(itemName) REFERENCES MenuItem(itemName),
    FOREIGN KEY(staffID) REFERENCES SousChef(staffID), 
    FOREIGN KEY(mentorID) REFERENCES SousChef(staffID)
);

CREATE TABLE Orders(
    orderNumber int NOT NULL,
    staffID int,
    custID int,
    orderDate date,
    orderTime time,
    tip double,
    totalPrice double,
    PRIMARY KEY(orderNumber),
    FOREIGN KEY(staffID) REFERENCES WaitStaff(staffID),
    FOREIGN KEY(custID) REFERENCES Customer(custID)
);

CREATE UNIQUE INDEX orderuid on Orders(staffID, custID, orderDate);

CREATE TABLE OrderItemMenu(
    itemName varchar(40) NOT NULL,
    menuType varchar(30) NOT NULL,
    orderNumber int NOT NULL,
    quantity int,
    PRIMARY KEY(itemName, menuType, orderNumber),
    FOREIGN KEY(itemName) REFERENCES ItemMenu(itemName),
    FOREIGN KEY(menuType) REFERENCES ItemMenu(menuType),
    FOREIGN KEY(orderNumber) REFERENCES Orders(orderNumber)
);


CREATE TABLE WebOrder(
    orderNumber int NOT NULL,
    pickUpTime time,
    PRIMARY KEY(orderNumber),
    FOREIGN KEY(orderNumber) REFERENCES Orders(orderNumber)
);

CREATE TABLE EatInOrder(
    orderNumber int NOT NULL,
    paymentType varchar(40),
    tableNumber int,
    PRIMARY KEY(orderNumber),
    FOREIGN KEY(orderNumber) REFERENCES Orders(orderNumber)
);

CREATE TABLE PhoneOrder(
    orderNumber int NOT NULL,
    paymentType varchar(40),
    pickUpTime time,
    PRIMARY KEY(orderNumber),
    FOREIGN KEY(orderNumber) REFERENCES Orders(orderNumber)
);

