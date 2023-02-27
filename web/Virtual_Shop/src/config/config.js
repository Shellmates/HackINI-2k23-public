const sqlite3 = require('sqlite3').verbose()
const articles = require("./articles.json").articles;
const db = new sqlite3.Database('/src/myDB.db') ;

password = "shellmates{Gg_b0Y_you_kNOW_w3ll_H0w_T0_uSe_uNiOn_4tTacK}"

articles.forEach(article=>{
    var val = [`'${article.name}'`,`'${article.category}'`,article.price,article.quantity].join(',');
    db.run(`INSERT INTO articles (name,category, price, quantity) VALUES (${val})`)
});

db.run(`INSERT INTO users (username, password) VALUES ('admin', '${password}')`)

db.close();