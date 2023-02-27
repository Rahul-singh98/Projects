const express = require('express')
const mongoDB = require('./db')

const app = express()
const port = 5000
mongoDB();
app.use(express.json())
app.use((req, res, next)=>{
  res.setHeader("Access-Control-Allow-Origin", "http://localhost:3000");
  res.header(
    "Access-Control-Allow-Headers",
    "Origin, X-Requested-With, Content-Type, Accept"
  );

  next();
})

app.get('/', (req, res) => {
  res.send('Hello World!')
})


app.use('/api', require('./routes/CRUDUser'))
app.use('/api', require('./routes/DisplayData'))

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})