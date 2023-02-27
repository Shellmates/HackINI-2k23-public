const sqlite3 = require('sqlite3').verbose()
const express = require("express");

const db = new sqlite3.Database('/src/myDB.db') ;

const app = express() ;

app.use(express.static('public'));
app.use(express.urlencoded({ extended: true }));
app.set("view engine", "ejs");
app.set("views",'views');

app.get("/",(req,res)=>{
    res.render('index', {title: 'Home', articles: []}) ;
})

app.get("/filter",(req,res)=>{
    db.all(`SELECT * FROM articles WHERE category='${req.query.category}'`,(err,rows)=>{
        if (err){
            console.log(err);
            res.status(500).render('500', {title: 500}) ;
        } else {
            res.render("index", {
                title: `${req.query.category}`,
                articles: rows
            })
        }
    }) ;
})

app.use((req,res)=>{
    res.status(404).render('404', {title: '404'});
})

app.listen(8000,()=>{
    console.log("Listenning on port 8000");
})