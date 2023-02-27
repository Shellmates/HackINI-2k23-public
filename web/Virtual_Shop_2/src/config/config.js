const sqlite3 = require('sqlite3').verbose()
const articles = require("./articles.json").articles;
const db = new sqlite3.Database('/src/myDB.db') ;

password = "shellmates{iT_W4$_Not_TH4T_S3cuRE_4T_THe_END}"

articles.forEach(article=>{
    var val = [`'${article.name}'`,`'${article.category}'`,article.price,article.quantity].join(',');
    db.run(`INSERT INTO articles (name,category, price, quantity) VALUES (${val})`)
});

db.run(`INSERT INTO UsEErrSS1337987 (usnme324, pw789) VALUES ('admin', '${password}')`)

db.close();