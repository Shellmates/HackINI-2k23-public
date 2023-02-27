const sqlite3 = require('sqlite3').verbose() ;
const db = new sqlite3.Database('/src/myDB.db') ;

db.run("CREATE TABLE articles (name TINYTEXT, category TINYTEXT,price int, quantity int)");

db.run("CREATE TABLE UsEErrSS1337987 (usnme324 TINYTEXT, pw789 TINYTEXT)");

db.close() ;