import jwt from "jsonwebtoken";

const generateToken = (data) => {
  const token = jwt.sign({ sub: data }, process.env.JWT_SECRET, {
    expiresIn: "1h",
  });
  return token;
};

export default generateToken;
