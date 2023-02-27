import express from "express";
import generateToken from "./middlewares/generateToken.js";
import dotenv from "dotenv";
import cookieParser from "cookie-parser";
import verifyToken from "./middlewares/verifyToken.js";

dotenv.config();

const app = express();

app.set("view engine", "ejs");

app.use(express.urlencoded({ extended: true }));
app.use(cookieParser());

app.get("/", (req, res) => {
  res.redirect("login");
});

app.get("/register", (req, res) => {
  res.render("register");
});

app.get("/login", (req, res) => {
  res.render("login", { message: "" });
});

app.post("/login", (req, res) => {
  const { username, password } = req.body;
  if (username === "zombo" && password === "zombo") {
    const token = generateToken({
      admin: false,
      data: {
        username,
        password,
      },
    });
    res.cookie("token", token, { httpOnly: true, maxAge: 3600000 });
    res.redirect("home");
  } else {
    res.render("login", { message: "Invalid Username or Password" });
  }
});

app.get("/home", (req, res) => {
  const token = req.cookies.token;
  const decoded = verifyToken(token);
  if (!decoded) {
    res.render("login", { message: "Login to access to home page" });
  }
  const { admin } = decoded.sub;
  if (admin) {
    return res.render("home", { flag: "shellmates{w34k_JwT_$3CR3T}" });
  } else {
    return res.render("home", { flag: "" });
  }
});

app.use((req, res) => {
  res.status(404).render("404", { title: "404" });
});

app.listen(8080, () => {
  console.log("Server started on port 8080");
});
